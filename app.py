from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import (QAction, QMessageBox, QCalendarWidget, QFontDialog,
QColorDialog, QTextEdit, QFileDialog, QCheckBox, QProgressBar, QComboBox,
QLabel, QStyleFactory, QLineEdit, QInputDialog, QApplication, QWidget,
QMainWindow, QPushButton)
import pandas as pd
import sys
import traceback

from ui.table import Ui_Table_Window
from ui.manual import Ui_Manual
from ui.license import Ui_Licence
from graphing import GraphBuilder

class Application(QMainWindow, Ui_Table_Window):
    def __init__(self):
        super(Application, self).__init__()
        self.setupUi(self)

        self.change_btn.clicked.connect(self.select_save_location)
        self.open_btn.clicked.connect(self.open_file)
        self.run_btn.clicked.connect(self.compute)

        self.manual = QMainWindow()
        self.manPage = Ui_Manual()
        self.manPage.setupUi(self.manual)

        self.about = QMainWindow()
        self.aboutPage = Ui_Licence()
        self.aboutPage.setupUi(self.about)

        self.divBool = {}
        self.divInt = {}
        self.divBoolFlags = {"Shannon": "-shannon", "Simpson": "-simpson", "Fisher": "-fisher", "Equitability": "-equitability"}
        self.divIntFlags = {"Hurlbert": 0}

        self.open_file()
        self.show()
        self.select_save_location()

    def open_file(self):
        try:
            fileName = QFileDialog.getOpenFileName(self, 'Input preadsheet file')
            fileName = str(fileName[0])
            if ".xls" not in fileName:
                raise ValueError("Not a spreadsheet. Please try again.")
        except(ValueError):
            wrongFile = QMessageBox.warning(self, "Error", "Please select a spreadsheet")
            self.open_file()
        try:
            self.columns = pd.read_excel(fileName, index_col=None, header=None, names=None)
            self.speciesNames = self.columns.get([0]).values.tolist()
            self.speciesNames.pop(0)
            self.sampleLabels = self.columns.loc[0]
            self.sampleLabels.pop(0)
            self.columns = self.columns.drop([0], axis=1)
            self.columns = self.columns.drop([0], axis=0)
            self.columns.columns = range(len(self.columns.T))
        except:
            colError = QMessageBox.warning(self, "Formatting error", 
                "The spread sheet contains invalid cells, rows or columns which are taken into account.\n\n" + 
                "Check that data cells containt exclusively numerical data and retry.")
            sys.exit()
        pass
    
    def select_save_location(self):
        dialog = QtWidgets.QFileDialog()
        savePath = dialog.getExistingDirectory(self, "Select Folder")
        self.savePath = savePath
        self.save_edit.setText(savePath)
        pass

    def compute(self):
        pass

def run():
    app = QtWidgets.QApplication(sys.argv)
    Gui = Application()
    sys.exit(app.exec_())
