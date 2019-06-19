# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table_Window(object):
    def setupUi(self, Table_Window):
        Table_Window.setObjectName("Table_Window")
        Table_Window.setEnabled(True)
        Table_Window.resize(1108, 592)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Table_Window.sizePolicy().hasHeightForWidth())
        Table_Window.setSizePolicy(sizePolicy)
        Table_Window.setMinimumSize(QtCore.QSize(1108, 592))
        Table_Window.setMaximumSize(QtCore.QSize(1108, 592))
        self.centralwidget = QtWidgets.QWidget(Table_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(20, 10, 291, 521))
        self.toolBox.setObjectName("toolBox")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 291, 416))
        self.page_1.setObjectName("page_1")
        self.shannon_check = QtWidgets.QCheckBox(self.page_1)
        self.shannon_check.setGeometry(QtCore.QRect(10, 10, 161, 29))
        self.shannon_check.setObjectName("shannon_check")
        self.fisher_check = QtWidgets.QCheckBox(self.page_1)
        self.fisher_check.setGeometry(QtCore.QRect(10, 90, 151, 29))
        self.fisher_check.setObjectName("fisher_check")
        self.simpson_check = QtWidgets.QCheckBox(self.page_1)
        self.simpson_check.setGeometry(QtCore.QRect(10, 50, 151, 29))
        self.simpson_check.setObjectName("simpson_check")
        self.equit_check = QtWidgets.QCheckBox(self.page_1)
        self.equit_check.setGeometry(QtCore.QRect(10, 130, 161, 29))
        self.equit_check.setObjectName("equit_check")
        self.hurl_check = QtWidgets.QCheckBox(self.page_1)
        self.hurl_check.setGeometry(QtCore.QRect(10, 170, 161, 29))
        self.hurl_check.setObjectName("hurl_check")
        self.rel_check = QtWidgets.QCheckBox(self.page_1)
        self.rel_check.setGeometry(QtCore.QRect(10, 210, 191, 29))
        self.rel_check.setObjectName("rel_check")
        self.rel_spin = QtWidgets.QSpinBox(self.page_1)
        self.rel_spin.setGeometry(QtCore.QRect(220, 210, 71, 31))
        self.rel_spin.setObjectName("rel_spin")
        self.hurl_spin = QtWidgets.QSpinBox(self.page_1)
        self.hurl_spin.setGeometry(QtCore.QRect(220, 170, 71, 31))
        self.hurl_spin.setObjectName("hurl_spin")
        self.toolBox.addItem(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 291, 416))
        self.page_2.setObjectName("page_2")
        self.dendrog_check = QtWidgets.QCheckBox(self.page_2)
        self.dendrog_check.setGeometry(QtCore.QRect(10, 10, 191, 29))
        self.dendrog_check.setObjectName("dendrog_check")
        self.nmds_check = QtWidgets.QCheckBox(self.page_2)
        self.nmds_check.setGeometry(QtCore.QRect(10, 50, 106, 29))
        self.nmds_check.setObjectName("nmds_check")
        self.dim_label = QtWidgets.QLabel(self.page_2)
        self.dim_label.setGeometry(QtCore.QRect(70, 80, 101, 21))
        self.dim_label.setObjectName("dim_label")
        self.run_label = QtWidgets.QLabel(self.page_2)
        self.run_label.setGeometry(QtCore.QRect(70, 114, 67, 21))
        self.run_label.setObjectName("run_label")
        self.dim_spin = QtWidgets.QSpinBox(self.page_2)
        self.dim_spin.setGeometry(QtCore.QRect(163, 76, 121, 30))
        self.dim_spin.setObjectName("dim_spin")
        self.run_spin = QtWidgets.QSpinBox(self.page_2)
        self.run_spin.setGeometry(QtCore.QRect(162, 110, 121, 30))
        self.run_spin.setObjectName("run_spin")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 291, 416))
        self.page_3.setObjectName("page_3")
        self.pb_check = QtWidgets.QCheckBox(self.page_3)
        self.pb_check.setGeometry(QtCore.QRect(10, 10, 106, 29))
        self.pb_check.setObjectName("pb_check")
        self.epiinf_check = QtWidgets.QCheckBox(self.page_3)
        self.epiinf_check.setGeometry(QtCore.QRect(10, 50, 181, 29))
        self.epiinf_check.setObjectName("epiinf_check")
        self.epiinfdet_check = QtWidgets.QCheckBox(self.page_3)
        self.epiinfdet_check.setGeometry(QtCore.QRect(10, 90, 261, 29))
        self.epiinfdet_check.setObjectName("epiinfdet_check")
        self.morpho_check = QtWidgets.QCheckBox(self.page_3)
        self.morpho_check.setGeometry(QtCore.QRect(10, 130, 251, 29))
        self.morpho_check.setObjectName("morpho_check")
        self.bfoi_check = QtWidgets.QCheckBox(self.page_3)
        self.bfoi_check.setGeometry(QtCore.QRect(10, 170, 241, 29))
        self.bfoi_check.setObjectName("bfoi_check")
        self.toolBox.addItem(self.page_3, "")
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(340, 60, 121, 41))
        self.change_btn.setObjectName("change_btn")
        self.save_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.save_edit.setGeometry(QtCore.QRect(480, 60, 611, 41))
        self.save_edit.setObjectName("save_edit")
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setGeometry(QtCore.QRect(340, 10, 121, 41))
        self.open_btn.setObjectName("open_btn")
        self.file_table = QtWidgets.QTableWidget(self.centralwidget)
        self.file_table.setGeometry(QtCore.QRect(340, 110, 750, 421))
        self.file_table.setObjectName("file_table")
        self.file_table.setColumnCount(0)
        self.file_table.setRowCount(0)
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setGeometry(QtCore.QRect(480, 10, 121, 41))
        self.run_btn.setObjectName("run_btn")
        Table_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Table_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 29))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuManual = QtWidgets.QMenu(self.menubar)
        self.menuManual.setObjectName("menuManual")
        Table_Window.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuManual.menuAction())

        self.retranslateUi(Table_Window)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Table_Window)

    def retranslateUi(self, Table_Window):
        _translate = QtCore.QCoreApplication.translate
        Table_Window.setWindowTitle(_translate("Table_Window", "MainWindow"))
        self.shannon_check.setText(_translate("Table_Window", "Shannon div."))
        self.fisher_check.setText(_translate("Table_Window", "Fisher div."))
        self.simpson_check.setText(_translate("Table_Window", "Simpson div."))
        self.equit_check.setText(_translate("Table_Window", "Equitability"))
        self.hurl_check.setText(_translate("Table_Window", "Hurlbert index"))
        self.rel_check.setText(_translate("Table_Window", "Rel. abundance for row"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), _translate("Table_Window", "Counts, univariate"))
        self.dendrog_check.setText(_translate("Table_Window", "Dendrogram"))
        self.nmds_check.setText(_translate("Table_Window", "NMDS"))
        self.dim_label.setText(_translate("Table_Window", "Dimensions"))
        self.run_label.setText(_translate("Table_Window", "Runs"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Table_Window", "Counts, multivariate"))
        self.pb_check.setText(_translate("Table_Window", "P/B ratio"))
        self.epiinf_check.setText(_translate("Table_Window", "Epif./Inf. proportions"))
        self.epiinfdet_check.setText(_translate("Table_Window", "Epif./Inf. proportions (detailed)"))
        self.morpho_check.setText(_translate("Table_Window", "Morphogroup abundances"))
        self.bfoi_check.setText(_translate("Table_Window", "BFOI Index"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Table_Window", "Specialized input required"))
        self.change_btn.setText(_translate("Table_Window", "Save location"))
        self.open_btn.setText(_translate("Table_Window", "Open file"))
        self.run_btn.setText(_translate("Table_Window", "Compute"))
        self.menuAbout.setTitle(_translate("Table_Window", "Abo&ut"))
        self.menuManual.setTitle(_translate("Table_Window", "Ma&nual"))
