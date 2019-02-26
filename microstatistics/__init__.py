from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import (QAction, QMessageBox, QCalendarWidget, QFontDialog,
QColorDialog, QTextEdit, QFileDialog, QCheckBox, QProgressBar, QComboBox,
QLabel, QStyleFactory, QLineEdit, QInputDialog, QApplication, QWidget,
QMainWindow, QPushButton)
from .gui_microstatistics import Ui_MainWindow
from .gui_manual import Ui_Manual
from .gui_licence import Ui_Licence
from .diversities import *
from .graphing_functions import *
import pandas as pd
import sys
import traceback

class Application(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(Application, self).__init__()
		self.setupUi(self)
		#self.setStyle(QStyleFactory.create('Plastique'))
		self.buttonCalculate.clicked.connect(self.work)
		self.buttonSave.clicked.connect(self.file_save)
		self.buttonOpen.clicked.connect(self.file_reopen)

		self.manual = QMainWindow()
		self.manPage = Ui_Manual()
		self.manPage.setupUi(self.manual)
		self.toolManual.triggered.connect(self.manual.show)

		self.about = QMainWindow()
		self.aboutPage = Ui_Licence()
		self.aboutPage.setupUi(self.about)
		self.toolAbout.triggered.connect(self.about.show)

		# Sets up the user interface and links the toolbar buttons to the
		# license and manual

		try:
			self.path = self.file_open()

		except FileNotFoundError:
			wrongFile = QMessageBox.warning(self, 'Error', 'Please select a' +
			' spreadsheet.')
			sys.exit()

		try:
			self.columns = pd.read_excel(self.path, index_col=None, header=None,
			names=None)
			self.speciesNames = self.columns.get([0]).values.tolist()
			self.speciesNames.pop(0)
			self.sampleLabels = self.columns.loc[0]
			self.sampleLabels.pop(0)
			self.columns = self.columns.drop([0], axis=1)
			self.columns = self.columns.drop([0], axis=0)
			self.columns.columns = range(len(self.columns.T))

		except ValueError:
			colError = QMessageBox.warning(self, 'Input error','The spreadsheet'
			' contains invalid cells, rows or columns which are taken into ' +
			'account.\n\n Please verify that all cells contain exclusively '
			+ 'numerical data and retry.', )
			sys.exit()

		self.show()

	def file_open(self):
		try:
			fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
			fileName = str(fileName[0])
			if '.xls' not in fileName:
				raise ValueError("Not a spreadsheet.")
		except(ValueError):
			wrongFile = QMessageBox.warning(self, 'Error', 'Please select a ' +
			'spreadsheet.')
			sys.exit()
		return fileName

	def file_reopen(self):
		try:
			self.path = self.file_open()
			self.columns = pd.read_excel(self.path, index_col=None, header=None,
			names=None)
			self.speciesNames = self.columns.get([0]).values.tolist()
			self.speciesNames.pop(0)
			self.sampleLabels = self.columns.loc[0]
			self.sampleLabels.pop(0)
			self.columns = self.columns.drop([0], axis=1)
			self.columns = self.columns.drop([0], axis=0)
			self.columns.columns = range(len(self.columns.T))
		except(ValueError):
			wrongFile = QMessageBox.warning(self, 'Error', 'Please select a ' +
			'spreadsheet.')

	def file_save(self):
		dialog = QtWidgets.QFileDialog()
		savePath = dialog.getExistingDirectory(None, "Select Folder")
		self.saveLocation.setText(savePath)

	def work(self):
		try:
			if self.saveLocation.text() == "Choose a save location:":
				raise ValueError('Invalid save location.')
		except(ValueError):
			saveError = QMessageBox.warning(self, "No save folder chosen",
			"Please choose a folder to save to by clicking the correct button.")
		else:
			self.calculate()

	def calculate(self):
		try:
			savePath = self.saveLocation.text()

			if self.checkboxFisher.isChecked():
				graphIndex(dfFisher(self.columns), 'Fisher diversity',
				savePath, self.sampleLabels)

			if self.checkboxSimpson.isChecked():
				graphIndex(dfSimpson(self.columns), 'Simpson diversity',
				savePath, self.sampleLabels)

			if self.checkboxShannon.isChecked():
				graphIndex(dfShannon(self.columns), 'Shannon diversity',
				savePath, self.sampleLabels)

			if self.checkboxEquitability.isChecked():
				graphIndex(dfEquitability(self.columns), 'Equitability',
				savePath, self.sampleLabels)

			if self.checkboxHurlbert.isChecked():
				corr = self.spinBoxHurlbert.value()
				graphIndex(dfHurlbert(self.columns, corr), f'Hurlbert '
				+ 'diversity, size {corr}', savePath, self.sampleLabels)

			if self.checkboxBFOI.isChecked():
				graphIndex(dfBFOI(self.columns), 'BFOI', savePath,
				self.sampleLabels)

			if self.checkboxRelAbundance.isChecked():
				row = self.spinBoxRelAbundance.value()
				try:
					if(row > self.columns.shape[0]+1 or row <= 1):
						raise ValueError("The chosen row is invalid")
					species = self.speciesNames[row-2]
					graphPercentages(self.columns, row-2, f'Abundance of ' +
					'species {species}', savePath, self.sampleLabels)
				except(ValueError):
					colError = QMessageBox.warning(self, 'Invalid row', 'An '
					'invalid row was chosen when attempting to calculate the'
					' relative abundance. Please make sure the row is in the '
					'spreadsheet and try again.')

			if self.checkboxPlankBent.isChecked():
				try:
					if(len(self.columns) != 2): # 2 rows required
						raise ValueError("The required formatting has not been"
						" respected. Please consult the documentation.")
					graphPercentages(self.columns, 0, 'P-B ratio', savePath,
					self.sampleLabels)
				except(ValueError):
					colError = QMessageBox.warning(self, 'Input error', 'The '
					'required formatting has not been respected. Please consult'
					'the documentation for the proper formatting required for '
					'graphing the Planktonic to Benthic ratio.')

			if self.checkboxEpifaunalInfauntal.isChecked():
				try:
					if(len(self.columns) != 2): # 2 rows required
						raise ValueError("The required formatting has not been"
						" respected. Please consult the documentation.")
					graphPercentages(self.columns, 0, 'Epifaunal-Infaunal' +
					' ratio', savePath, self.sampleLabels)
				except(ValueError):
					colError = QMessageBox.warning(self, 'Input error', 'The '
					'required formatting has not been respected. Please consult'
					' the documentation for the proper formatting required for '
					'graphing the Epifaunal to Infaunal ratio.')

			if self.checkboxEpifaunalInf3.isChecked():
				try:
					if(len(self.columns) != 4):
						raise ValueError("The required formatting has not been"
						" respected. Please consult the documentation.")
					graphEpiInfDetailed(self.columns, savePath)
				except(ValueError):
					colError = QMessageBox.warning(self, 'Input error', 'The '
					'required formatting has not been respected. Please consult'
					' the documentation for the proper formatting required for '
					'graphing the detailed Epifaunal to Infaunal ratio.')

			try:
				if self.checkboxMorphogroups.isChecked():
					try:
						if(len(self.columns) != 9):
							raise ValueError("The required formatting has not "
							"been respected. Please consult the documentation.")
						graphMorphogroups(self.columns, savePath,
						self.sampleLabels)
					except(ValueError):
						colError = QMessageBox.warning(self, 'Input error',
						'The requied formatting has not been respected. Please '
						'consult the documentation for the proper formatting '
						'required for graphing Morphogroup abundances.')
			except(ValueError):
				colError = QMessageBox.warning(self, 'Input error', 'The requir'
				'ed formatting has not been respected. Please consult the docum'
				'entation for the proper formatting required for graphing '
				'morphogroup abundances.')


			if self.checkboxDendrogram.isChecked():
				graphSampleDendrogram(self.columns, savePath, self.sampleLabels)
				graphSpeciesDendrogram(self.columns, savePath)

			if self.checkboxNMDS.isChecked():
				dimens = self.spinBoxDimensions.value()
				runs = self.spinBoxRuns.value()
				graphNMDS(self.columns, dimens, runs, savePath,
				self.sampleLabels)

			finished = QMessageBox.information (self, 'Finished',
			'The selected operations have been performed. The plots have been'
			'saved in '+ self.saveLocation.text())

		except (TypeError, ValueError):
			traceback.print_exc()
			colError = QMessageBox.warning(self, 'Input error', 'The '
			'spreadsheet contains empty cells, rows or columns which are taken '
			'into account.\n\n Please verify that all cells contain exclusively'
			'numerical data, and then copy the input data into a new .xlsx '
			'file\n', )
			# sys.exit()

def run():
	app = QtWidgets.QApplication(sys.argv)
	Gui = Application()
	sys.exit(app.exec_())
run()
