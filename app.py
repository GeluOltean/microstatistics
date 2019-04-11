from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import QIcon, QColor, QStandardItemModel, QStandardItem
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QAction, QMessageBox, QCalendarWidget, QFontDialog,
QColorDialog, QTextEdit, QFileDialog, QCheckBox, QProgressBar, QComboBox,
QLabel, QStyleFactory, QLineEdit, QInputDialog, QApplication, QWidget,
QMainWindow, QPushButton, QTableWidgetItem)
import pandas as pd
import sys
import traceback

from ui.table import Ui_Table_Window
from ui.manual import Ui_Manual
from ui.license import Ui_Licence
from util.graphing import GraphBuilder
from util.dispatching import SubprocDispatcher


class Application(QMainWindow, Ui_Table_Window):
    def __init__(self):
        # ui setup
        super(Application, self).__init__()
        self.setupUi(self)

        self.change_btn.clicked.connect(self.select_save_path)
        self.open_btn.clicked.connect(self.read_spreadsheet)
        self.run_btn.clicked.connect(self.compute)

        self.manual = QMainWindow()
        self.manPage = Ui_Manual()
        self.manPage.setupUi(self.manual)

        self.about = QMainWindow()
        self.aboutPage = Ui_Licence()
        self.aboutPage.setupUi(self.about)

        self.save_edit.setText("Please choose a save location first.")

        # flags for bin use
        self.divBoolFlags = {"Shannon": "-shannon", "Simpson": "-simpson", "Fisher": "-fisher", 
                            "Equitability": "-equitability"}
        self.divIntFlags = {"Hurlbert": "-hurlbert="}
        self.divs = []

        # read file and set save location
        self.savePath = None
        self.read_spreadsheet() # sets self.columns, self.sampleLabels, self.speciesNames
        self.show()
        self.select_save_path() # sets self.savePath

    def read_spreadsheet(self):
        try:
            fileName = QFileDialog.getOpenFileName(self, 'Input preadsheet file')
            fileName = str(fileName[0])
            if ".xls" not in fileName:
                raise ValueError("Not a spreadsheet. Please try again.")
        except ValueError as e:
            print(e)
            wrongFile = QMessageBox.warning(self, "Error", "Please select a spreadsheet")
        try:
            self.columns = pd.read_excel(fileName, index_col=None, header=None, names=None)
           
            self.speciesNames = self.columns.get([0])
            self.speciesNames = [str(x[0]) for x in self.speciesNames.values]
            self.speciesNames.pop(0)

            self.sampleLabels = self.columns.loc[0]
            self.sampleLabels.pop(0)
            self.sampleLabels = [str(x) for x in self.sampleLabels.values]

            self.columns = self.columns.drop([0], axis=1)
            self.columns = self.columns.drop([0], axis=0)
            self.columns.columns = range(len(self.columns.T))

            # create services
            self.dispatcher = SubprocDispatcher(self.columns)
            self.plotter = GraphBuilder(self.columns, self.speciesNames, self.sampleLabels, self.savePath)

            # populate table
            self.__set_table()

        except Exception as e:
            print(e)
            colError = QMessageBox.warning(self, "Formatting error", 
                "The spread sheet contains invalid cells, rows or columns which are taken into account.\n\n" + 
                "Check that data cells containt exclusively numerical data and retry.")
            sys.exit()
        pass

    def __set_table(self):
        self.file_table.setColumnCount(len(self.sampleLabels)+1)
        self.file_table.setHorizontalHeaderLabels([""] +self.sampleLabels)

        for row_number, row_data in enumerate(self.columns.values):
            self.file_table.insertRow(row_number)
            # name = QTableWidgetItem(str(self.speciesNames[row_number]))
            name = QTableWidgetItem(self.speciesNames[row_number])
            self.file_table.setItem(row_number, 0, name)

            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.file_table.setItem(row_number, column_number+1, item)
        pass
    
    def select_save_path(self):
        dialog = QtWidgets.QFileDialog()
        savePath = dialog.getExistingDirectory(self, "Select Folder")
        self.savePath = savePath
        self.save_edit.setText(savePath)

        # update the graphing service save path
        self.plotter.savelocation = self.savePath
        pass

    def compute(self):
        if self.savePath is None:
            saveError = QMessageBox.warning(self, "No save folder chosen",
            "Please choose a folder to save to by clicking the correct button.")
            return

        self.divs = []
        if self.shannon_check.isChecked():
            self.divs.append(self.divBoolFlags["Shannon"])

        if self.fisher_check.isChecked():
            self.divs.append(self.divBoolFlags["Fisher"])

        if self.simpson_check.isChecked():
            self.divs.append(self.divBoolFlags["Simpson"])

        if self.equit_check.isChecked():
            self.divs.append(self.divBoolFlags["Equitability"])

        if self.hurl_check.isChecked():
            self.divs.append(self.divIntFlags["Hurlbert"] + str(self.hurl_spin.value()))

        a = self.dispatcher.exec_univariate(self.divs)
        self.plotter.graphIndexBatch(a)
        
        # "raw" plotter use
        if self.rel_check.isChecked():
            ind = self.rel_spin.value()
            species = self.speciesNames[ind-2]
            self.plotter.graphPercentages(ind-2, f"Abundance of species {species}")
        
        if self.pb_check.isChecked():
            self.plotter.graphPercentages(0, "Planktonic-Benthic ratio")
        
        if self.epiinf_check.isChecked():
            self.plotter.graphPercentages(0, "Epifaunal-Infaunal ratio")

        if self.epiinfdet_check.isChecked():
            self.plotter.graphEpiInfDetailed()
        
        if self.morpho_check.isChecked():
            self.plotter.graphMorphogroups()
       
        if self.bfoi_check.isChecked():
            self.plotter.graphIndex(self.plotter.df_bfoi(self.columns), "BFOI")

        if self.dendrog_check.isChecked():
            self.plotter.graphSampleDendrogram()
            self.plotter.graphSpeciesDendrogram()

        if self.nmds_check.isChecked():
            dim = self.dim_spin.value()
            run = self.run_spin.value()
            self.plotter.graphNMDS(self.columns, dim, run, self.savePath, self.sampleLabels)

        finished = QMessageBox.information (self, 'Finished',
            'The selected operations have been performed. The plots have been'
            'saved in '+ self.savePath)
        pass

def run():
    app = QtWidgets.QApplication(sys.argv)
    Gui = Application()
    sys.exit(app.exec_())
