import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
import pandas as pd

from microstatistics.gui.license import License
from microstatistics.gui.manual import Manual
from microstatistics.gui.table import Table_Window


class Application(QMainWindow, Table_Window):
    def __init__(self):
        # data state
        self.save_path: str = ""
        self.columns: pd.DataFrame = pd.DataFrame()
        self.sample_labels: list = []
        self.species_labels: list = []

        # ui setup
        super(Application, self).__init__()
        self.setupUi(self)

        self.change_btn.clicked.connect(self.select_save_path)
        self.open_btn.clicked.connect(self.read_spreadsheet)
        self.run_btn.clicked.connect(self.compute)

        self.manual = QMainWindow()
        self.manPage = Manual()
        self.manPage.setupUi(self.manual)

        self.about = QMainWindow()
        self.aboutPage = License()
        self.aboutPage.setupUi(self.about)

        self.save_edit.setText("Please choose a save location first.")

        self.read_spreadsheet()
        self.select_save_path()
        self.show()

    def read_spreadsheet(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Input preadsheet file')
            file_name = str(file_name[0])
            if ".xls" not in file_name:
                raise ValueError("Not a spreadsheet. Please try again.")
        except ValueError as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please select a spreadsheet")
        try:
            self.columns = pd.read_excel(file_name, index_col=None, header=None, names=None)

            self.species_labels = self.columns.get([0]).values.tolist()
            self.species_labels.pop(0)
            self.sample_labels = self.columns.loc[0]
            self.sample_labels.pop(0)

            self.columns = self.columns.drop([0], axis=1)
            self.columns = self.columns.drop([0], axis=0)
            self.columns.columns = range(len(self.columns.T))
        except Exception as e:
            print(e)

    def select_save_path(self):
        dialog = QtWidgets.QFileDialog()
        self.save_path = dialog.getExistingDirectory(self, "Select Folder")
        self.save_edit.setText(self.save_path)

    def compute(self):
        if self.shannon_check.isChecked():
            pass

        if self.fisher_check.isChecked():
            pass

        if self.simpson_check.isChecked():
            pass

        if self.equit_check.isChecked():
            pass

        if self.hurl_check.isChecked():
            pass

        if self.rel_check.isChecked():
            pass

        if self.pb_check.isChecked():
            pass

        if self.epiinf_check.isChecked():
            pass

        if self.epiinfdet_check.isChecked():
            pass

        if self.morpho_check.isChecked():
            pass

        if self.bfoi_check.isChecked():
            pass

        if self.dendrog_check.isChecked():
            pass

        if self.nmds_check.isChecked():
            pass

        # Once finished:
        QMessageBox.information(self, 'Finished', f'The selected operations have been performed. The plots have been '
                                f'saved in {self.savePath}')


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Application()  # assignment required by PyQt, do not remove
    sys.exit(app.exec_())
