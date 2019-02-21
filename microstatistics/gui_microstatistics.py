from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 633)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
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

        self.checkboxFisher = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxFisher.setGeometry(QtCore.QRect(40, 20, 261, 31))
        self.checkboxFisher.setObjectName("checkboxFisher")
        self.checkboxFisher.setText("Fisher alpha diversity")

        self.label_2 = QtWidgets.QLabel(self.pageSpeciesCount)
        self.label_2.setGeometry(QtCore.QRect(680, 0, 111, 24))
        self.label_2.setObjectName("label_2")

        self.checkboxShannon = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxShannon.setGeometry(QtCore.QRect(40, 60, 261, 31))
        self.checkboxShannon.setObjectName("checkboxShannon")
        self.checkboxShannon.setText("Shannon-Wiener index")

        self.checkboxSimpson = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxSimpson.setGeometry(QtCore.QRect(40, 100, 261, 31))
        self.checkboxSimpson.setObjectName("checkboxSimpson")
        self.checkboxSimpson.setText("Simpson")

        self.checkboxHurlbert = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxHurlbert.setGeometry(QtCore.QRect(40, 140, 261, 31))
        self.checkboxHurlbert.setObjectName("checkboxHurlbert")
        self.checkboxHurlbert.setText(
            "Hurlbert diversity \n(select correction factor)")

        self.spinBoxHurlbert = QtWidgets.QSpinBox(self.pageSpeciesCount)
        self.spinBoxHurlbert.setGeometry(QtCore.QRect(220, 140, 71, 33))
        self.spinBoxHurlbert.setMinimum(1)
        self.spinBoxHurlbert.setMaximum(99999)
        self.spinBoxHurlbert.setProperty("value", 100)
        self.spinBoxHurlbert.setObjectName("spinBoxHurlbert")

        self.checkboxEquitability = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxEquitability.setGeometry(QtCore.QRect(40, 180, 261, 31))
        self.checkboxEquitability.setObjectName("checkboxEquitability")
        self.checkboxEquitability.setText("Equitability")

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

        self.checkboxRelAbundance = QtWidgets.QCheckBox(self.pageSpeciesCount)
        self.checkboxRelAbundance.setGeometry(QtCore.QRect(300, 20, 261, 31))
        self.checkboxRelAbundance.setObjectName("checkboxRelAbundance")
        self.checkboxRelAbundance.setText("Relative Abundance for row:")

        self.spinBoxRelAbundance = QtWidgets.QSpinBox(self.pageSpeciesCount)
        self.spinBoxRelAbundance.setGeometry(QtCore.QRect(500, 20, 71, 33))
        self.spinBoxRelAbundance.setMinimum(1)
        self.spinBoxRelAbundance.setMaximum(9999)
        self.spinBoxRelAbundance.setProperty("value", 2)
        self.spinBoxRelAbundance.setObjectName("spinBoxRelAbundance")

        self.toolBox.addItem(self.pageSpeciesCount, "Univariate - "
                             + "Species Count")

        self.pageSpecificInput = QtWidgets.QWidget()
        self.pageSpecificInput.setGeometry(QtCore.QRect(0, 0, 1147, 240))
        self.pageSpecificInput.setObjectName("pageSpecificInput")

        self.checkboxPlankBent = QtWidgets.QCheckBox(self.pageSpecificInput)
        self.checkboxPlankBent.setGeometry(QtCore.QRect(40, 20, 261, 31))
        self.checkboxPlankBent.setObjectName("checkboxPlankBent")
        self.checkboxPlankBent.setText("P/B ratio")

        self.checkboxEpifaunalInfauntal = QtWidgets.QCheckBox(
            self.pageSpecificInput)
        self.checkboxEpifaunalInfauntal.setGeometry(QtCore.QRect(40, 60, 261,
                                                                 31))
        self.checkboxEpifaunalInfauntal.setObjectName(
            "checkboxEpifaunalInfauntal")
        self.checkboxEpifaunalInfauntal.setText("Epifaunal/Infaunal proportion")

        self.checkboxEpifaunalInf3 = QtWidgets.QCheckBox(self.pageSpecificInput)
        self.checkboxEpifaunalInf3.setGeometry(QtCore.QRect(280, 60, 281, 31))
        self.checkboxEpifaunalInf3.setObjectName("checkboxEpifaunalInf3")
        self.checkboxEpifaunalInf3.setText("Epifaunal/Infaunal (detailed)" +
                                           " proportion")

        self.checkboxMorphogroups = QtWidgets.QCheckBox(self.pageSpecificInput)
        self.checkboxMorphogroups.setGeometry(QtCore.QRect(40, 100, 391, 31))
        self.checkboxMorphogroups.setObjectName("checkboxMorphogroups")
        self.checkboxMorphogroups.setText("Morphogroup abundances")

        self.toolBox.addItem(self.pageSpecificInput, "Univariate - Specific " +
                             "input required")

        self.checkboxBFOI = QtWidgets.QCheckBox(self.pageSpecificInput)
        self.checkboxBFOI.setGeometry(QtCore.QRect(40, 140, 121, 31))
        self.checkboxBFOI.setObjectName("checkboxBFOI")
        self.checkboxBFOI.setText("BFOI")

        self.buttonCalculate = QtWidgets.QToolButton(self.centralWidget)
        self.buttonCalculate.setGeometry(QtCore.QRect(1000, 30, 170, 51))
        self.buttonCalculate.setObjectName("buttonCalculate")
        self.buttonCalculate.setText("Calculate indices")

        # ///// multivariate page

        self.pageMultivariate = QtWidgets.QWidget()
        self.pageMultivariate.setGeometry(QtCore.QRect(0,0,1147,240))
        self.pageMultivariate.setObjectName("pageMultivariate")
        self.toolBox.addItem(self.pageMultivariate, "Multivariate")

        self.checkboxDendrogram = QtWidgets.QCheckBox(self.pageMultivariate)
        self.checkboxDendrogram.setGeometry(QtCore.QRect(40, 20, 261, 31))
        self.checkboxDendrogram.setObjectName("checkboxDendrogram")
        self.checkboxDendrogram.setText("Hierarchical Clustering (Dendrogram)")

        self.checkboxNMDS = QtWidgets.QCheckBox(self.pageMultivariate)
        self.checkboxNMDS.setGeometry(QtCore.QRect(40, 60, 261, 31))
        self.checkboxNMDS.setObjectName("checkboxNMDS")
        self.checkboxNMDS.setText("NMDS")

        self.spinBoxDimensions = QtWidgets.QSpinBox(self.pageMultivariate)
        self.spinBoxDimensions.setGeometry(QtCore.QRect(160, 96, 71, 33))
        self.spinBoxDimensions.setMinimum(1)
        self.spinBoxDimensions.setMaximum(9999)
        self.spinBoxDimensions.setProperty("value", 2)
        self.spinBoxDimensions.setObjectName("spinBoxDimensions")

        self.spinBoxRuns = QtWidgets.QSpinBox(self.pageMultivariate)
        self.spinBoxRuns.setGeometry(QtCore.QRect(160, 137, 71, 33))
        self.spinBoxRuns.setMinimum(1)
        self.spinBoxRuns.setMaximum(30000000)
        self.spinBoxRuns.setProperty("value", 5)
        self.spinBoxRuns.setObjectName("spinBoxRuns")

        self.label_5 = QtWidgets.QLabel(self.pageMultivariate)
        self.label_5.setGeometry(QtCore.QRect(80, 100, 101, 24))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Dimensions")

        self.label_6 = QtWidgets.QLabel(self.pageMultivariate)
        self.label_6.setGeometry(QtCore.QRect(80, 140, 101, 24))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Runs")


        # ///////////////

        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 490, 911, 41))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Thank you for using our software! We would " +
                             "appreciate a citation to the following paper:")

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
