import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
import pandas as pd

from microstatistics.gui.license import License
from microstatistics.gui.manual import Manual
from microstatistics.gui.table import Table_Window
from microstatistics.util.diversities import SHANNON, FISHER, SIMPSON, EQUITABILITY, HURLBERT
from microstatistics.util.diversityService import DiversityService
from microstatistics.util.graphingService import GraphingService


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
        self.rel_spin.setMinimum(1)
        self.dim_spin.setMinimum(1)
        self.run_spin.setMinimum(1)
        self.rel_spin.setValue(1)
        self.dim_spin.setValue(1)
        self.run_spin.setValue(1)

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
            self.species_labels = [x[0] for x in self.species_labels]

            self.sample_labels = self.columns.loc[0]
            self.sample_labels.pop(0)

            self.columns = self.columns.drop([0], axis=1)
            self.columns = self.columns.drop([0], axis=0)
            self.columns.columns = range(len(self.columns.T))

            # modify interface
            self.__set_table()
            self.rel_spin.setMaximum(len(self.species_labels))
        except Exception as e:
            print(e)

    def __set_table(self):
        self.file_table.setColumnCount(len(self.sample_labels) + 1)
        self.file_table.setHorizontalHeaderLabels([""] + self.sample_labels)

        for row_number, row_data in enumerate(self.columns.values):
            self.file_table.insertRow(row_number)
            name = QTableWidgetItem(self.species_labels[row_number])
            self.file_table.setItem(row_number, 0, name)

            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.file_table.setItem(row_number, column_number + 1, item)

    def select_save_path(self):
        dialog = QtWidgets.QFileDialog()
        self.save_path = dialog.getExistingDirectory(self, "Select Folder")
        self.save_edit.setText(self.save_path)

    def compute(self):
        if self.shannon_check.isChecked():
            GraphingService.graph_index(
                save_path=self.save_path,
                title=SHANNON,
                labels=self.sample_labels,
                data=DiversityService.compute_index(self.columns, SHANNON)
            )

        if self.fisher_check.isChecked():
            GraphingService.graph_index(
                save_path=self.save_path,
                title=FISHER,
                labels=self.sample_labels,
                data=DiversityService.compute_index(self.columns, FISHER)
            )

        if self.simpson_check.isChecked():
            GraphingService.graph_index(
                save_path=self.save_path,
                title=SIMPSON,
                labels=self.sample_labels,
                data=DiversityService.compute_index(self.columns, SIMPSON)
            )

        if self.equit_check.isChecked():
            GraphingService.graph_index(
                save_path=self.save_path,
                title=EQUITABILITY,
                labels=self.sample_labels,
                data=DiversityService.compute_index(self.columns, EQUITABILITY)
            )

        if self.hurl_check.isChecked():
            size = self.hurl_spin.value()
            GraphingService.graph_index(
                save_path=self.save_path,
                title=f"{HURLBERT}, size = {size}",
                labels=self.sample_labels,
                data=DiversityService.compute_index(self.columns, HURLBERT, size)
            )

        if self.rel_check.isChecked():
            target_row = self.rel_spin.value()
            GraphingService.graph_index(
                save_path=self.save_path,
                title=f"Abundance of species {self.species_labels[target_row-1]}",
                labels=self.sample_labels,
                data=(DiversityService.compute_percentages(self.columns)).loc[target_row]
            )

        if self.pb_check.isChecked():
            GraphingService.graph_index(
                save_path=self.save_path,
                title="Planktonic-Benthic Ration",
                labels=self.sample_labels,
                data=DiversityService.compute_percentages(self.columns)[0]
            )

        if self.epiinf_check.isChecked():
            GraphingService.graph_index(
                save_path=self.save_path,
                title="Epifaunal-Infaunal Ration",
                labels=self.sample_labels,
                data=DiversityService.compute_percentages(self.columns)[0]
            )

        if self.epiinfdet_check.isChecked():
            GraphingService.graph_epi_inf_detailed(
                save_path=self.save_path,
                data=DiversityService.compute_percentages(self.columns)
            )

        if self.morpho_check.isChecked():
            GraphingService.graph_morphogroups(
                save_path=self.save_path,
                labels=self.sample_labels,
                data=DiversityService.compute_morphogroups(self.columns)
            )

        if self.bfoi_check.isChecked():
            GraphingService.graph_index(
                save_path=self.save_path,
                title="BFOI",
                labels=self.sample_labels,
                data=DiversityService.compute_bfoi(self.columns)[0]
            )

        if self.dendrog_check.isChecked():
            GraphingService.graph_dendrogram(
                save_path=self.save_path,
                title="R-mode Dendrogram (Bray-Curtis)",
                labels=[x for x in range(1, self.sample_labels.count() + 1)],
                data=DiversityService.compute_linkage(data=self.columns.T)
            )
            GraphingService.graph_dendrogram(
                save_path=self.save_path,
                title="Q-mode Dendrogram (Bray-Curtis)",
                labels=self.species_labels,
                data=DiversityService.compute_linkage(data=self.columns)
            )

        if self.nmds_check.isChecked():
            dimensions = self.dim_spin.value()
            runs = self.run_spin.value()
            GraphingService.graph_nmds(
                save_path=self.save_path,
                labels=self.sample_labels.values,
                data=DiversityService.compute_nmds(
                    data=self.columns,
                    dimensions=dimensions,
                    runs=runs
                )
            )

        # Once finished:
        QMessageBox.information(self, 'Finished', f'The selected operations have been performed. The plots have been '
                                f'saved in {self.save_path}')


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Application()  # assignment required by PyQt, do not remove
    sys.exit(app.exec_())
