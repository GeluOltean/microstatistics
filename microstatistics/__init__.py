from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QAction, QMessageBox, QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog, QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog, QApplication, QWidget, QMainWindow, QPushButton
from .diversities import *
from .gui_microstatistics import Ui_MainWindow
from .gui_manual import Ui_Manual
from .gui_licence import Ui_Licence
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
			self.columns = pd.read_excel(self.path)
			self.columns = self.columns.reset_index().T	
			self.columns = self.columns.drop(self.columns.index[:1], axis=0)
			self.sampleDistance = dist.pdist(self.columns.values, metric='braycurtis')
			self.columns = self.columns.values.tolist()

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
			self.columns = pd.read_excel(self.path, index=False)
			self.columns = self.columns.reset_index().T
			self.sampleDistance = dist.pdist(self.columns.values, metric='braycurtis')
			self.columns = self.columns.values.tolist()

		except:
			wrongFile = QMessageBox.warning(self, 'Error', 'Please select a spreadsheet.')

	def process_values_proportions(self, cln):
		values = []
		col = self.columns [cln]

		for i in range (0, len(col)): # ignore col[0] -- designated for strings
			# values.append(col[i].value)
			values.append(col[i])
		values = [i if i!=0 else 0.000000000001 for i in values]

		return values

	def process_values_indices(self, cln):
		values = []
		col = self.columns[cln]

		for i in range (0, len(col)):
			# values.append(col[i].value)
			values.append(col[i])

		while 0 in values:
			values.remove(0)
		return values

	def graph(self, targetList, title: str):
		targetList.insert(0,float('Nan')) # this enables setting the axis limits without
		# losing the first indexed item
		fig = plt.figure(dpi=500, figsize=(3,10))
		yaxis = list(range(len(targetList)))
		fig.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
		# this forces integers on the y axis

		plt.plot(targetList, yaxis, c='black')
		plt.yticks(yaxis) # this shows all the samples on the y axis
		plt.title(title)
		plt.xlabel("")
		plt.ylabel("Sample nr", fontsize=15)
		axes = plt.gca()
		axes.set_ylim([1,len(targetList)-1])
		# the above two lines remove uneeded whitespace, while also having the
		# plot start from 0 on the y axis
	#	plt.fill_betweenx(yaxis, targetList, facebolor='black')
		plt.savefig(self.saveLocation.text() +'/'+ title +'.svg' )


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
				fisherList = []
				for i in range (1, int(len(self.columns))):
					fisherList.append(fisher(self.process_values_indices(i)))
				#print(fisherList)
				self.graph(fisherList, 'Fisher diversity')

			try:
				if self.checkboxSimpson.isChecked():
					simpsonList = []
					for i in range (1, int(len(self.columns))):
						simpsonList.append(simpson(self.process_values_indices(i)))
					# print(simpsonList)
					self.graph(simpsonList, 'Simpson diversity')
			except ZeroDivisionError:
				colError = QMessageBox.warning(self, 'Input error', 'The spreadsheet'
			' contains empty cells, rows or columns which are taken into account.\n',
			'\nPlease verify that all cells contain exclusively numerical data.', )
				sys.exit()


			if self.checkboxShannon.isChecked():
				shannonList = []
				for i in range (1, int(len(self.columns))):
					shannonList.append(shannon(self.process_values_indices(i)))
				# print(shannonList)
				self.graph(shannonList, 'Shannon diversity')


			if self.checkboxEquitability.isChecked():
				equitabilityList = []
				for i in range (1, int(len(self.columns))):
					equitabilityList.append(equitability(
											self.process_values_indices(i)))
				# print(equitabilityList)
				self.graph(equitabilityList, 'Pielou Equitability')


			if self.checkboxHurlbert.isChecked():
				hurlbertList = []
				hurlbertCorrection = self.spinBoxHurlbert.value()
				for i in range (1, int(len(self.columns))):
					hurlbertList.append(hurlbert_diversity(self.process_values_indices(i), n=hurlbertCorrection))
				# print(hurlbertList)

				self.graph(hurlbertList, 'Hurlbert diversity')


			# PROPORTION -- CALCULATIONS ON ROWS -- ZEROES REPLACED BY 1 REQUIRED

			if self.checkboxRelAbundance.isChecked():
				relAbundanceRow = self.spinBoxRelAbundance.value()
				relAbundanceList = []
				for i in range (1, int(len(self.columns))):
					relAbundanceList.append(proportion(
											(self.process_values_proportions(i)),
											relAbundanceRow-2))
				# print(relAbundanceList)
				self.graph(relAbundanceList, "% for row " + str(relAbundanceRow))


			if self.checkboxBFOI.isChecked():
				BFOIList = []
				for i in range (1, int(len(self.columns))):
					BFOIList.append(bfoi_index(self.process_values_proportions(i),1))
				# print(BFOIList)
				self.graph(BFOIList, 'BFOI')


			if self.checkboxPlankBent.isChecked():
				plankBentList = []
				for i in range (1, int(len(self.columns))):
					plankBentList.append(proportion(
										(self.process_values_proportions(i)), 0))
				#print(plankBentList)
				self.graph(plankBentList, 'P-B ratio')


			if self.checkboxEpifaunalInfauntal.isChecked():
				EpifaunalInfauntalList = []
				for i in range (1, int(len(self.columns))):
					EpifaunalInfauntalList.append(proportion(
										(self.process_values_proportions(i)), 0))
				#print(plankBentList)
				self.graph(EpifaunalInfauntalList, 'Epifaunal-Infaunal ratio')

			if self.checkboxEpifaunalInf3.isChecked():
				epifaunalList = [float('Nan')]
				infDeepList = [float('Nan')]
				infShallowList = [float('Nan')]
				infUndetList = [float('Nan')]

				for i in range (1, int(len(self.columns))):
					epifaunalList.append(proportion(
										(self.process_values_proportions(i)), 0))
					infShallowList.append(proportion(
										(self.process_values_proportions(i)), 1))
					infDeepList.append(proportion(
										(self.process_values_proportions(i)), 2))
					infUndetList.append(proportion(
										(self.process_values_proportions(i)), 3))

				infShallowList = [sum(x) for x in zip(epifaunalList, infShallowList)]
				infDeepList = [sum(x) for x in zip(infShallowList, infDeepList)]
				infUndetList = [sum(x) for x in zip(infDeepList, infUndetList)]

				fig = plt.figure(dpi=200, figsize=(5,5))

				yaxis = list(range(len(epifaunalList)))
				axes = plt.gca()
				plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
				plt.yticks(yaxis)

				lineEpi = plt.plot(epifaunalList, yaxis,'#52A55C',label='Epifaunal')
				lineInfShallow = plt.plot(infShallowList, yaxis,'#236A62',label='Infaunal shallow')
				lineInfDeep = plt.plot(infDeepList, yaxis,'#2E4372',label='Infaunal deep')
				lineInfUndet = plt.plot(infUndetList, yaxis,'#535353',label='Infaunal undetermined')

				plt.fill_betweenx(yaxis, epifaunalList, facecolor='#52A55C')
				plt.fill_betweenx(yaxis, epifaunalList, infShallowList, facecolor='#236A62')
				plt.fill_betweenx(yaxis, infShallowList, infDeepList, facecolor='#2E4372')
				plt.fill_betweenx(yaxis, infDeepList, infUndetList, facecolor='#535353')

				axes.set_ylim([1,len(epifaunalList)-1])
				axes.set_xlim(0,100)

				plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           					ncol=2, mode="expand", borderaxespad=0.)
				plt.savefig(self.saveLocation.text() + '/' + 'Epifaunal-Infaunal detailed ratio.svg')


			if self.checkboxMorphogroups.isChecked():
				morphs = ['M1', 'M2a', 'M2b', 'M2c', 'M3a', 'M3b', 'M3c', 'M4a', 'M4b']
				morphogroupsList = []
				for x in range(0,9):
					morphogroupAbundance = []
					for i in range (1, len(self.columns)):
						morphogroupAbundance.append(proportion(
												(self.process_values_proportions(i)),
												x))
					morphogroupAbundance.insert(0,float('Nan'))
					morphogroupsList.append(morphogroupAbundance)

				morphDict = dict(zip(morphs, morphogroupsList))
				titles = list(morphDict.keys())

				fig = plt.subplots(nrows=1, ncols=9, sharey=True)
				plt.figure(dpi=500, figsize=(15,8))
				yaxis = list(range(len(morphDict['M1'])))
				plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
				#plt.title('Morphogroup abundances')

				for x in range(0,9):
					plt.subplot(1,9,x+1)
					plt.plot(morphDict[str(titles[x])], yaxis, c='black')
					plt.xlabel(titles[x])
					plt.yticks(yaxis)
					plt.gca().set_ylim([1,len(morphDict['M1'])-1])
					plt.fill_betweenx(yaxis, morphDict[str(titles[x])], facecolor='black')
				titleAx = plt.subplot(1,9,5)
				#plt.text(0.5, 1.08, 'Morphogroup abundances', horizontalalignment='center',fontsize=20,transform = titleAx.transAxes)
				#plt.suptitle('Morphogroup abundances\n', fontsize=20)
				plt.title("Morphogroup abundances\n")
				plt.tight_layout()
				plt.savefig(self.saveLocation.text() + '/' + 'Morphogroups.svg')


			# MULTIVARIATE


			if self.checkboxDendrogram.isChecked():
				fig = plt.figure(dpi=500)
				linkage = hc.linkage(self.sampleDistance, method='average')
				dendrog = hc.dendrogram(linkage, labels=list(range(0, len(self.columns)+2)))
				plt.suptitle('Dendrogram (Bray-Curtis)')
				plt.savefig(self.saveLocation.text() + '/Dendrogram.svg')


			if self.checkboxNMDS.isChecked():
				dimens = self.spinBoxDimensions.value()
				runs = self.spinBoxRuns.value()
				squareDist = dist.squareform(self.sampleDistance)

				nmds = MDS (n_components=dimens, metric=False, dissimilarity='precomputed',
				        max_iter=runs, n_init=30)
				pos = nmds.fit(squareDist).embedding_
				strs = nmds.fit(squareDist).stress_
				labels = list(range(1, len(self.columns)+1))

				pos0 = pos[:,0].tolist()
				pos1 = pos[:,1].tolist()

				fig, ax = plt.subplots()
				ax.scatter(pos0, pos1)
				for i, txt in enumerate(labels):
				    ax.annotate(txt, (pos0[i], pos1[i]))
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
