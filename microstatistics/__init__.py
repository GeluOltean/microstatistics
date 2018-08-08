from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QAction, QMessageBox, QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog, QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog, QApplication, QWidget, QMainWindow, QPushButton
from .gui_microstatistics import Ui_MainWindow
from .gui_manual import Ui_Manual
from .gui_licence import Ui_Licence
from .diversities import *
from .graphing_functions import *
from scipy.misc import comb
from math import log
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
from scipy.cluster import hierarchy as hc
from scipy.spatial import distance as dist
from sklearn.manifold import MDS
import sys
import math

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

		# Sets up the user interface and links the toolbar buttons to the licence and manual

		try:
			self.path = self.file_open()

		except FileNotFoundError:
			wrongFile = QMessageBox.warning(self, 'Error', 'Please select a spreadsheet.')
			sys.exit()

		try:
			self.columns = pd.read_excel(self.path, index_col=None, header=None, names=None, skiprows=1).drop([0], axis=1)
			self.columns.columns = range(len(self.columns.T))
			self.sampleDistance = dist.pdist(self.columns.values.T, metric='braycurtis')
			self.speciesDistance = dist.pdist(self.columns.values, metric='braycurtis')

		except ValueError:
			colError = QMessageBox.warning(self, 'Input error', 'The spreadsheet'
			' contains invalid cells, rows or columns which are taken into account.\n'
			'\nPlease verify that all cells contain exclusively numerical data and retry.', )
			sys.exit()

		self.show()

	def file_open(self):
		try:
			fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
			fileName = str(fileName[0])
			if '.xls' not in fileName:
				raise ValueError
		except:
			wrongFile = QMessageBox.warning(self, 'Error', 'Please select a spreadsheet.')
			sys.exit()
		return fileName

		# other spreadsheet formats could be added later on 

	def file_reopen(self):
		try:
			self.path = self.file_open()
			self.columns = pd.read_excel(self.path, index_col=None, header=None, names=None, skiprows=1).drop([0], axis=1)
			self.columns.columns = range(len(self.columns.T))
			self.sampleDistance = dist.pdist(self.columns.values.T, metric='braycurtis')
			self.speciesDistance = dist.pdist(self.columns.values, metric='braycurtis')

		except:
			wrongFile = QMessageBox.warning(self, 'Error', 'Please select a spreadsheet.')

	def file_save(self):
		dialog = QtWidgets.QFileDialog()
		savePath = dialog.getExistingDirectory(None, "Select Folder")
		self.saveLocation.setText(savePath)


	def work(self):
		try:
			if self.saveLocation.text() == "Choose a save location:":
				raise ValueError('Invalid save location.')
		except:
			saveError = QMessageBox.warning(self, "No save folder chosen",
			"Please choose a folder to save to by clicking the correct button.")
		else:
			self.calculate()

	def calculate(self):
		try:
			# UNIVARIATE INDICES
			if self.checkboxFisher.isChecked():
				graphIndex(dfFisher(self.columns), 'Fisher diversity')

			if self.checkboxSimpson.isChecked():
				graphIndex(dfSimpson(self.columns), 'Simpson diversity')

			if self.checkboxShannon.isChecked():
				graphIndex(dfShannon(self.columns), 'Shannon diversity')

			if self.checkboxEquitability.isChecked():
				graphIndex(dfEquitability(self.columns), 'Equitability')

			if self.checkboxHurlbert.isChecked():
				corr = self.spinBoxHurlbert.value()
				graphIndex(dfHurlbert(self.columns, corr), f'Hurlbert diversity, size {corr}')

			if self.checkboxBFOI.isChecked():
				graphIndex(dfBFOI(self.columns), 'BFOI')

			if self.checkboxRelAbundance.isChecked():
				row = self.spinBoxRelAbundance.value()
				graphPercentages(self.columns, row-2, f'Abundance of species on row {row}')

			if self.checkboxPlankBent.isChecked():
				graphPercentages(self.columns, 0, 'P/B ratio')

			if self.checkboxEpifaunalInfauntal.isChecked():
				graphPercentages(self.columns, 0, 'Epifaunal/Infaunal ratio')

			if self.checkboxEpifaunalInf3.isChecked():
				graphEpiInfDetailed(self.columns)

			if self.checkboxMorphogroups.isChecked():
				graphMorphogroups(self.columns)

			if self.checkboxDendrogram.isChecked():
				fig = plt.figure(dpi=500)
				linkage = hc.linkage(self.sampleDistance, method='average')
				dendrog = hc.dendrogram(linkage, labels=list(range(0, len(self.columns)+2)))
				plt.suptitle('Dendrogram for samples (Bray-Curtis)')
				plt.savefig(self.saveLocation.text() + '/Sample_Dendrogram.svg')

				fig = None
				fig = plt.figure(dpi=800)
				linkage = hc.linkage(self.speciesDistance, method='average')
				dendrog = hc.dendrogram(linkage, orientation='left', labels=list(range(0, len(linkage)+2)))
				plt.suptitle('Dendrogram for species (Bray-Curtis)')
				plt.savefig(self.saveLocation.text() + '/Species_Dendrogram.svg')


			if self.checkboxNMDS.isChecked():
				dimens = self.spinBoxDimensions.value()
				runs = self.spinBoxRuns.value()
				squareDist = dist.squareform(self.sampleDistance)

				nmds = MDS (n_components=dimens, metric=False, dissimilarity='precomputed',
				        max_iter=runs, n_init=30)
				pos = nmds.fit(squareDist).embedding_
				strs = nmds.fit(squareDist).stress_
				labels = list(range(0, len(self.columns.T)))

				pos0 = pos[:,0].tolist()
				pos1 = pos[:,1].tolist()

				fig, ax = plt.subplots()
				ax.scatter(pos0, pos1)
				for i, x in enumerate(labels):
					ax.annotate(x+1, (pos0[i], pos1[i]))
				fig.suptitle('nDMS (Bray-Curtis)', fontweight='bold')
				ax.set_title('Stress = ' + str(strs))

				plt.savefig(self.saveLocation.text() + '/' + 'nMDS.svg')

			finished = QMessageBox.information (self, 'Finished',
			'The selected operations have been performed. The plots have been'
			'saved in '+ self.saveLocation.text())

		except (TypeError, ValueError):
			colError = QMessageBox.warning(self, 'Input error', 'The spreadsheet'
			' contains empty cells, rows or columns which are taken into account.\n'
			'\nPlease verify that all cells contain exclusively numerical data, and', 
			'then copy the input data into a new .xlsx file\n', )
			sys.exit()


def run():
	app = QtWidgets.QApplication(sys.argv)
	Gui = Application()
	sys.exit(app.exec_())
run()
