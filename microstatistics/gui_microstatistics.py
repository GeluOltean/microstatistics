from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 633)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1197, 633))
        MainWindow.setMaximumSize(QtCore.QSize(1197, 633))
        MainWindow.setWindowTitle("microStatistics")


        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.toolBox = QtWidgets.QToolBox(self.centralWidget)
        self.toolBox.setGeometry(QtCore.QRect(20, 110, 1151, 361))
        self.toolBox.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.toolBox.setLineWidth(2)
        self.toolBox.setMidLineWidth(0)
        self.toolBox.setObjectName("toolBox")

        self.pageSpeciesCount = QtWidgets.QWidget()
        self.pageSpeciesCount.setEnabled(True)
        self.pageSpeciesCount.setGeometry(QtCore.QRect(0, 0, 1147, 240))
        self.pageSpeciesCount.setObjectName("pageSpeciesCount")

        self.label = QtWidgets.QLabel(self.pageSpeciesCount)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 24))
        self.label.setObjectName("label")
        self.label.setText("Univariate")

        self.checkboxFisher = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxFisher.setGeometry(QtCore.QRect(10, 30, 261, 31))
        self.checkboxFisher.setObjectName("checkboxFisher")
        self.checkboxFisher.setText("Fisher alpha diversity")

        self.label_2 = QtWidgets.QLabel(self.pageSpeciesCount)
        self.label_2.setGeometry(QtCore.QRect(680, 0, 111, 24))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Multivariate")

        self.checkboxShannon = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxShannon.setGeometry(QtCore.QRect(10, 70, 261, 31))
        self.checkboxShannon.setObjectName("checkboxShannon")
        self.checkboxShannon.setText("Shannon-Wiener index")

        self.checkboxHurlbert = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxHurlbert.setGeometry(QtCore.QRect(10, 150, 261, 31))
        self.checkboxHurlbert.setObjectName("checkboxHurlbert")
        self.checkboxHurlbert.setText("Hurlbert diversity")

        self.checkboxSimpson = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxSimpson.setGeometry(QtCore.QRect(10, 110, 261, 31))
        self.checkboxSimpson.setObjectName("checkboxSimpson")
        self.checkboxSimpson.setText("Simpson")

        self.checkboxEquitability = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxEquitability.setGeometry(QtCore.QRect(280, 30, 261, 31))
        self.checkboxEquitability.setObjectName("checkboxEquitability")
        self.checkboxEquitability.setText("Equitability")

        self.spinBoxHurlbert = QtWidgets.QSpinBox(self.pageSpeciesCount)
        self.spinBoxHurlbert.setGeometry(QtCore.QRect(180, 150, 71, 33))
        self.spinBoxHurlbert.setMinimum(1)
        self.spinBoxHurlbert.setMaximum(99999)
        self.spinBoxHurlbert.setProperty("value", 100)
        self.spinBoxHurlbert.setObjectName("spinBoxHurlbert")

        self.label_3 = QtWidgets.QLabel(self.pageSpeciesCount)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 211, 24))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("(select correction factor)")

        self.checkboxDendrogram = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxDendrogram.setGeometry(QtCore.QRect(680, 30, 261, 31))
        self.checkboxDendrogram.setObjectName("checkboxDendrogram")
        self.checkboxDendrogram.setText("Dendrogram")

        self.buttonOpen = QtWidgets.QToolButton(self.centralWidget)
        self.buttonOpen.setGeometry(QtCore.QRect(20, 30, 170, 51))
        self.buttonOpen.setObjectName("buttonOpen")
        self.buttonOpen.setText("Choose another file")

        self.buttonSave = QtWidgets.QToolButton(self.centralWidget)
        self.buttonSave.setGeometry(QtCore.QRect(200, 30, 170, 51))
        self.buttonSave.setObjectName("buttonSave")
        self.buttonSave.setText("Choose save location")


        self.saveLocation = QtWidgets.QLabel(self.centralWidget)
        self.saveLocation.setGeometry(QtCore.QRect(400, 30, 791, 51))
        self.saveLocation.setObjectName("saveLocation")
        self.saveLocation.setText("Choose a save location:")


        self.checkboxNMDS = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxNMDS.setGeometry(QtCore.QRect(680, 70, 261, 31))
        self.checkboxNMDS.setObjectName("checkboxNMDS")
        self.checkboxNMDS.setText("NMDS")

        self.checkboxRelAbundance = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxRelAbundance.setGeometry(QtCore.QRect(280, 70, 261, 31))
        self.checkboxRelAbundance.setObjectName("checkboxRelAbundance")
        self.checkboxRelAbundance.setText("Relative Abundance for row:")

        self.spinBoxRelAbundance = QtWidgets.QSpinBox(self.pageSpeciesCount)
        self.spinBoxRelAbundance.setGeometry(QtCore.QRect(530, 70, 71, 33))
        self.spinBoxRelAbundance.setMinimum(1)
        self.spinBoxRelAbundance.setMaximum(9999)
        self.spinBoxRelAbundance.setProperty("value", 8)
        self.spinBoxRelAbundance.setObjectName("spinBoxRelAbundance")

        self.toolBox.addItem(self.pageSpeciesCount, "Species Count")

        self.pagePBCount = QtWidgets.QWidget()
        self.pagePBCount.setGeometry(QtCore.QRect(0, 0, 1147, 240))
        self.pagePBCount.setObjectName("pagePBCount")

        self.checkboxPlankBent = QtWidgets.QCheckBox(self.pagePBCount)
        self.checkboxPlankBent.setGeometry(QtCore.QRect(40, 20, 261, 31))
        self.checkboxPlankBent.setObjectName("checkboxPlankBent")
        self.checkboxPlankBent.setText("P/B ratio")

        self.checkboxEpifaunalInfauntal = QtWidgets.QCheckBox(self.pagePBCount)
        self.checkboxEpifaunalInfauntal.setGeometry(QtCore.QRect(40, 60, 261, 31))
        self.checkboxEpifaunalInfauntal.setObjectName("checkboxEpifaunalInfauntal")
        self.checkboxEpifaunalInfauntal.setText("Epifaunal/Infaunal proportion")

        self.checkboxEpifaunalInf3 = QtWidgets.QCheckBox(self.pagePBCount)
        self.checkboxEpifaunalInf3.setGeometry(QtCore.QRect(280, 60, 281, 31))
        self.checkboxEpifaunalInf3.setObjectName("checkboxEpifaunalInf3")
        self.checkboxEpifaunalInf3.setText("Epifaunal/Infaunal (detailed) proportion")

        self.checkboxMorphogroups = QtWidgets.QCheckBox(self.pagePBCount)
        self.checkboxMorphogroups.setGeometry(QtCore.QRect(40, 100, 391, 31))
        self.checkboxMorphogroups.setObjectName("checkboxMorphogroups")
        self.checkboxMorphogroups.setText("Morphogroup abundances")

        self.toolBox.addItem(self.pagePBCount, 'Specific input required')

        self.checkboxBFOI = QtWidgets.QCheckBox(self.pagePBCount)
        self.checkboxBFOI.setGeometry(QtCore.QRect(40, 140, 121, 31))
        self.checkboxBFOI.setObjectName("checkboxBFOI")
        self.checkboxBFOI.setText("BFOI")

        self.buttonCalculate = QtWidgets.QToolButton(self.centralWidget)
        self.buttonCalculate.setGeometry(QtCore.QRect(1000, 30, 170, 51))
        self.buttonCalculate.setObjectName("buttonCalculate")
        self.buttonCalculate.setText("Calculate indices")

        self.spinBoxDimensions = QtWidgets.QSpinBox(self.pageSpeciesCount)
        self.spinBoxDimensions.setGeometry(QtCore.QRect(830, 100, 71, 33))
        self.spinBoxDimensions.setMinimum(1)
        self.spinBoxDimensions.setMaximum(9999)
        self.spinBoxDimensions.setProperty("value", 5)
        self.spinBoxDimensions.setObjectName("spinBoxDimensions")

        self.spinBoxRuns = QtWidgets.QSpinBox(self.pageSpeciesCount)
        self.spinBoxRuns.setGeometry(QtCore.QRect(830, 140, 111, 33))
        self.spinBoxRuns.setMinimum(1)
        self.spinBoxRuns.setMaximum(30000)
        self.spinBoxRuns.setProperty("value", 5)
        self.spinBoxRuns.setObjectName("spinBoxRuns")

        self.label_5 = QtWidgets.QLabel(self.pageSpeciesCount)
        self.label_5.setGeometry(QtCore.QRect(720, 100, 81, 24))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.pageSpeciesCount)
        self.label_6.setGeometry(QtCore.QRect(720, 140, 101, 41))
        self.label_6.setObjectName("label_6")
        self.label_5.setText("Dimensions")
        self.label_6.setText("Number of \nruns")

        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 490, 911, 41))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Thank you for using our software! We would appreciate a citation to the following paper:")

        MainWindow.setCentralWidget(self.centralWidget)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.toolManual = QtWidgets.QAction('Manual', self)
        self.toolAbout = QtWidgets.QAction('About', self)
        self.mainToolBar.addAction(self.toolAbout)
        self.mainToolBar.addAction(self.toolManual)



        # self.menuBar = QtWidgets.QMenuBar(MainWindow)
        # self.menuBar.setGeometry(QtCore.QRect(0, 0, 1197, 30))
        # self.menuBar.setObjectName("menuBar")

        # self.menuManual = QtWidgets.QMenu(self.menuBar)
        # self.menuManual.setObjectName("menuManual")
        # self.menuManual.setTitle("Manual")


        # self.menuAbout = QtWidgets.QMenu(self.menuBar)
        # self.menuAbout.setObjectName("menuAbout")
        # self.menuAbout.setTitle("About")


        # MainWindow.setMenuBar(self.menuBar)
   
        # self.menuBar.addAction(self.menuManual.menuAction())
        # self.menuBar.addAction(self.menuAbout.menuAction())