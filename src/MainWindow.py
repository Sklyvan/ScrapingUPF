# -*- coding: utf-8 -*-
# Created by: PyQt5 UI Code Generator 5.15.6

from PyQt5_Imports import *

class Ui_MainWindowDesign(object):
    def setupUi(self, MainWindowDesign, QtApplication):
        self.QtApplication = QtApplication
        MainWindowDesign.setObjectName("MainWindowDesign")
        MainWindowDesign.resize(602, 602)
        MainWindowDesign.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain))
        self.mainWindow = QtWidgets.QWidget(MainWindowDesign)
        self.mainWindow.setObjectName("mainWindow")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mainWindow)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.basicInformationBox = QtWidgets.QGroupBox(self.mainWindow)
        self.basicInformationBox.setObjectName("basicInformationBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.basicInformationBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.basicInformation = QtWidgets.QGroupBox(self.basicInformationBox)
        self.basicInformation.setObjectName("basicInformation")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.basicInformation)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.planEstudio = QtWidgets.QLabel(self.basicInformation)
        self.planEstudio.setObjectName("planEstudio")
        self.gridLayout_4.addWidget(self.planEstudio, 0, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.basicInformation)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_4.addWidget(self.saveButton, 7, 0, 1, 2)
        self.planDocente = QtWidgets.QLabel(self.basicInformation)
        self.planDocente.setObjectName("planDocente")
        self.gridLayout_4.addWidget(self.planDocente, 3, 0, 1, 1)
        self.codigoCentroText = QtWidgets.QLineEdit(self.basicInformation)
        self.codigoCentroText.setObjectName("codigoCentroText")
        self.gridLayout_4.addWidget(self.codigoCentroText, 4, 1, 1, 1)
        self.codigoEstudioText = QtWidgets.QLineEdit(self.basicInformation)
        self.codigoEstudioText.setObjectName("codigoEstudioText")
        self.gridLayout_4.addWidget(self.codigoEstudioText, 5, 1, 1, 1)
        self.trimestreSpinBox = QtWidgets.QSpinBox(self.basicInformation)
        self.trimestreSpinBox.setMinimum(1)
        self.trimestreSpinBox.setMaximum(3)
        self.trimestreSpinBox.setObjectName("trimestreSpinBox")
        self.gridLayout_4.addWidget(self.trimestreSpinBox, 2, 1, 1, 1)
        self.codigoEstudio = QtWidgets.QLabel(self.basicInformation)
        self.codigoEstudio.setObjectName("codigoEstudio")
        self.gridLayout_4.addWidget(self.codigoEstudio, 5, 0, 1, 1)
        self.curso = QtWidgets.QLabel(self.basicInformation)
        self.curso.setObjectName("curso")
        self.gridLayout_4.addWidget(self.curso, 6, 0, 1, 1)
        self.cursoSpinBox = QtWidgets.QSpinBox(self.basicInformation)
        self.cursoSpinBox.setMinimum(1)
        self.cursoSpinBox.setMaximum(4)
        self.cursoSpinBox.setObjectName("cursoSpinBox")
        self.gridLayout_4.addWidget(self.cursoSpinBox, 6, 1, 1, 1)
        self.codigoCentro = QtWidgets.QLabel(self.basicInformation)
        self.codigoCentro.setObjectName("codigoCentro")
        self.gridLayout_4.addWidget(self.codigoCentro, 4, 0, 1, 1)
        self.idiomaPais = QtWidgets.QLabel(self.basicInformation)
        self.idiomaPais.setObjectName("idiomaPais")
        self.gridLayout_4.addWidget(self.idiomaPais, 1, 0, 1, 1)
        self.idiomaPaisText = QtWidgets.QLineEdit(self.basicInformation)
        self.idiomaPaisText.setObjectName("idiomaPaisText")
        self.gridLayout_4.addWidget(self.idiomaPaisText, 1, 1, 1, 1)
        self.planEstudioText = QtWidgets.QLineEdit(self.basicInformation)
        self.planEstudioText.setObjectName("planEstudioText")
        self.gridLayout_4.addWidget(self.planEstudioText, 0, 1, 1, 1)
        self.trimestre = QtWidgets.QLabel(self.basicInformation)
        self.trimestre.setObjectName("trimestre")
        self.gridLayout_4.addWidget(self.trimestre, 2, 0, 1, 1)
        self.planDocenteText = QtWidgets.QLineEdit(self.basicInformation)
        self.planDocenteText.setObjectName("planDocenteText")
        self.gridLayout_4.addWidget(self.planDocenteText, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.basicInformation)
        self.groupBox = QtWidgets.QGroupBox(self.basicInformationBox)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.subjectsWidget1 = QtWidgets.QWidget()
        self.subjectsWidget1.setObjectName("subjectsWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.subjectsWidget1)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.subjectsInfoBox = QtWidgets.QGroupBox(self.subjectsWidget1)
        self.subjectsInfoBox.setTitle("")
        self.subjectsInfoBox.setObjectName("subjectsInfoBox")
        self.gridLayout = QtWidgets.QGridLayout(self.subjectsInfoBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.subjectSeminarsText = QtWidgets.QLineEdit(self.subjectsInfoBox)
        self.subjectSeminarsText.setObjectName("subjectSeminarsText")
        self.gridLayout.addWidget(self.subjectSeminarsText, 3, 1, 1, 1)
        self.subjectSeminars = QtWidgets.QLabel(self.subjectsInfoBox)
        self.subjectSeminars.setObjectName("subjectSeminars")
        self.gridLayout.addWidget(self.subjectSeminars, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.addButton = QtWidgets.QPushButton(self.subjectsInfoBox)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 4, 0, 1, 2)
        self.subjectTheory = QtWidgets.QLabel(self.subjectsInfoBox)
        self.subjectTheory.setObjectName("subjectTheory")
        self.gridLayout.addWidget(self.subjectTheory, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.subjectTheoryText = QtWidgets.QLineEdit(self.subjectsInfoBox)
        self.subjectTheoryText.setObjectName("subjectTheoryText")
        self.gridLayout.addWidget(self.subjectTheoryText, 1, 1, 1, 1)
        self.subjectCode = QtWidgets.QLabel(self.subjectsInfoBox)
        self.subjectCode.setObjectName("subjectCode")
        self.gridLayout.addWidget(self.subjectCode, 0, 0, 1, 1)
        self.subjectCodeText = QtWidgets.QLineEdit(self.subjectsInfoBox)
        self.subjectCodeText.setObjectName("subjectCodeText")
        self.gridLayout.addWidget(self.subjectCodeText, 0, 1, 1, 1)
        self.subjectPractice = QtWidgets.QLabel(self.subjectsInfoBox)
        self.subjectPractice.setObjectName("subjectPractice")
        self.gridLayout.addWidget(self.subjectPractice, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.subjectPracticesText = QtWidgets.QLineEdit(self.subjectsInfoBox)
        self.subjectPracticesText.setObjectName("subjectPracticesText")
        self.gridLayout.addWidget(self.subjectPracticesText, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.subjectsInfoBox)
        self.clearButton = QtWidgets.QPushButton(self.subjectsWidget1)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_4.addWidget(self.clearButton)
        self.tabWidget.addTab(self.subjectsWidget1, "")
        self.subjectsWidget2 = QtWidgets.QWidget()
        self.subjectsWidget2.setObjectName("subjectsWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.subjectsWidget2)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.subjectFilePathBox = QtWidgets.QGroupBox(self.subjectsWidget2)
        self.subjectFilePathBox.setObjectName("subjectFilePathBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.subjectFilePathBox)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.filePathText = QtWidgets.QLineEdit(self.subjectFilePathBox)
        self.filePathText.setObjectName("filePathText")
        self.verticalLayout_7.addWidget(self.filePathText)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verificationButton = QtWidgets.QPushButton(self.subjectFilePathBox)
        self.verificationButton.setObjectName("verificationButton")
        self.gridLayout_5.addWidget(self.verificationButton, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.subjectFilePathBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_5)
        self.useFileButton = QtWidgets.QPushButton(self.subjectFilePathBox)
        self.useFileButton.setObjectName("useFileButton")
        self.verticalLayout_7.addWidget(self.useFileButton)
        self.horizontalLayout_3.addWidget(self.subjectFilePathBox)
        self.tabWidget.addTab(self.subjectsWidget2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.datesBox = QtWidgets.QGroupBox(self.groupBox)
        self.datesBox.setTitle("")
        self.datesBox.setObjectName("datesBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.datesBox)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.calendarDates = QtWidgets.QWidget(self.datesBox)
        self.calendarDates.setAutoFillBackground(False)
        self.calendarDates.setObjectName("calendarDates")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.calendarDates)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.startDateLabel = QtWidgets.QLabel(self.calendarDates)
        self.startDateLabel.setObjectName("startDateLabel")
        self.gridLayout_2.addWidget(self.startDateLabel, 0, 1, 1, 1)
        self.endDateLabel = QtWidgets.QLabel(self.calendarDates)
        self.endDateLabel.setObjectName("endDateLabel")
        self.gridLayout_2.addWidget(self.endDateLabel, 1, 1, 1, 1)
        self.endDateEdit = QtWidgets.QDateEdit(self.calendarDates)
        self.endDateEdit.setMaximumDate(QtCore.QDate(2030, 1, 1))
        self.endDateEdit.setMinimumDate(QtCore.QDate(2020, 1, 1))
        self.endDateEdit.setObjectName("endDateEdit")
        self.gridLayout_2.addWidget(self.endDateEdit, 1, 2, 1, 1)
        self.startDateEdit = QtWidgets.QDateEdit(self.calendarDates)
        self.startDateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDateEdit.setMaximumDate(QtCore.QDate(2030, 1, 1))
        self.startDateEdit.setMinimumDate(QtCore.QDate(2020, 1, 1))
        self.startDateEdit.setCalendarPopup(False)
        self.startDateEdit.setObjectName("startDateEdit")
        self.gridLayout_2.addWidget(self.startDateEdit, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.calendarDates)
        self.verticalLayout_2.addWidget(self.datesBox)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout_3.addWidget(self.basicInformationBox, 0, 0, 1, 1)
        self.endBox = QtWidgets.QFrame(self.mainWindow)
        self.endBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.endBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.endBox.setObjectName("endBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.endBox)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deleteButton = QtWidgets.QPushButton(self.endBox)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.transferButton = QtWidgets.QPushButton(self.endBox)
        self.transferButton.setObjectName("transferButton")
        self.verticalLayout.addWidget(self.transferButton)
        self.gridLayout_3.addWidget(self.endBox, 2, 0, 1, 1)
        self.mainProgressBar = QtWidgets.QProgressBar(self.mainWindow)
        self.mainProgressBar.setProperty("value", 0)
        self.mainProgressBar.setObjectName("mainProgressBar")
        self.gridLayout_3.addWidget(self.mainProgressBar, 3, 0, 1, 1)
        MainWindowDesign.setCentralWidget(self.mainWindow)
        self.menuBar = QtWidgets.QMenuBar(MainWindowDesign)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 594, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindowDesign.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindowDesign)
        self.statusBar.setObjectName("statusBar")
        MainWindowDesign.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(MainWindowDesign)
        self.actionAbout.setObjectName("actionAbout")
        self.actionManual = QtWidgets.QAction(MainWindowDesign)
        self.actionManual.setObjectName("actionManual")
        self.actionQuit = QtWidgets.QAction(MainWindowDesign)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAgradecimientos = QtWidgets.QAction(MainWindowDesign)
        self.actionAgradecimientos.setObjectName("actionAgradecimientos")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAgradecimientos)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindowDesign)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowDesign)
        MainWindowDesign.setTabOrder(self.planEstudioText, self.idiomaPaisText)
        MainWindowDesign.setTabOrder(self.idiomaPaisText, self.trimestreSpinBox)
        MainWindowDesign.setTabOrder(self.trimestreSpinBox, self.planDocenteText)
        MainWindowDesign.setTabOrder(self.planDocenteText, self.codigoCentroText)
        MainWindowDesign.setTabOrder(self.codigoCentroText, self.codigoEstudioText)
        MainWindowDesign.setTabOrder(self.codigoEstudioText, self.cursoSpinBox)
        MainWindowDesign.setTabOrder(self.cursoSpinBox, self.saveButton)
        MainWindowDesign.setTabOrder(self.saveButton, self.tabWidget)
        MainWindowDesign.setTabOrder(self.tabWidget, self.subjectCodeText)
        MainWindowDesign.setTabOrder(self.subjectCodeText, self.subjectTheoryText)
        MainWindowDesign.setTabOrder(self.subjectTheoryText, self.subjectPracticesText)
        MainWindowDesign.setTabOrder(self.subjectPracticesText, self.subjectSeminarsText)
        MainWindowDesign.setTabOrder(self.subjectSeminarsText, self.addButton)
        MainWindowDesign.setTabOrder(self.addButton, self.filePathText)
        MainWindowDesign.setTabOrder(self.filePathText, self.clearButton)
        MainWindowDesign.setTabOrder(self.clearButton, self.startDateEdit)
        MainWindowDesign.setTabOrder(self.startDateEdit, self.endDateEdit)
        MainWindowDesign.setTabOrder(self.endDateEdit, self.deleteButton)
        MainWindowDesign.setTabOrder(self.deleteButton, self.transferButton)

        self.saveButton.clicked.connect(self.clickSaveButton)
        self.addButton.clicked.connect(self.clickAddButton)
        self.useFileButton.clicked.connect(self.clickUseFileButton)
        self.deleteButton.clicked.connect(self.clickRemoveSubjectsButton)
        self.transferButton.clicked.connect(self.clickAddSubjectsButton)
        self.clearButton.clicked.connect(self.clickClearSubjectsButton)
        self.verificationButton.clicked.connect(self.clickVerificationButton)

        self.actionQuit.triggered.connect(self.exitApplication)
        self.actionAbout.triggered.connect(self.openRepository)
        self.actionManual.triggered.connect(self.openManual)
        self.actionAgradecimientos.triggered.connect(self.runInformationWindow)

    def retranslateUi(self, MainWindowDesign):
        _translate = QtCore.QCoreApplication.translate
        MainWindowDesign.setWindowTitle(_translate("MainWindowDesign", "ScrapingUPF"))
        self.basicInformation.setTitle(_translate("MainWindowDesign", "Información Básica"))
        self.planEstudio.setText(_translate("MainWindowDesign", "Plan de Estudio"))
        self.saveButton.setText(_translate("MainWindowDesign", "Guardar"))
        self.planDocente.setText(_translate("MainWindowDesign", "<html><head/><body><p>Año Docente</p></body></html>"))
        self.codigoEstudio.setText(_translate("MainWindowDesign", "Código Estudio"))
        self.curso.setText(_translate("MainWindowDesign", "Curso"))
        self.codigoCentro.setText(_translate("MainWindowDesign", "Código Centro"))
        self.idiomaPais.setText(_translate("MainWindowDesign", "Idioma y País"))
        self.trimestre.setText(_translate("MainWindowDesign", "<html><head/><body><p>Trimestre</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindowDesign", "Información Variable"))
        self.subjectSeminars.setText(_translate("MainWindowDesign", "<html><head/><body><p>Grupo de Seminarios</p></body></html>"))
        self.addButton.setText(_translate("MainWindowDesign", "Añadir"))
        self.subjectTheory.setText(_translate("MainWindowDesign", "Grupo de Teoría"))
        self.subjectCode.setText(_translate("MainWindowDesign", "Código de Asignatura"))
        self.subjectPractice.setText(_translate("MainWindowDesign", "<html><head/><body><p>Grupo de Prácticas</p></body></html>"))
        self.clearButton.setText(_translate("MainWindowDesign", "Limpiar Asignaturas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subjectsWidget1), _translate("MainWindowDesign", "Método Manual"))
        self.subjectFilePathBox.setTitle(_translate("MainWindowDesign", "Introducir la ubicación del archivo:"))
        self.verificationButton.setText(_translate("MainWindowDesign", "Verificar Archivo"))
        self.useFileButton.setText(_translate("MainWindowDesign", "Usar Archivo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subjectsWidget2), _translate("MainWindowDesign", "Método Automático"))
        self.startDateLabel.setText(_translate("MainWindowDesign", "Fecha Inicial"))
        self.endDateLabel.setText(_translate("MainWindowDesign", "Fecha Final"))
        self.deleteButton.setText(_translate("MainWindowDesign", "Eliminar asignaturas de Google Calendar"))
        self.transferButton.setText(_translate("MainWindowDesign", "Transferir asignaturas a Google Calendar"))
        self.menuHelp.setTitle(_translate("MainWindowDesign", "Help"))
        self.actionAbout.setText(_translate("MainWindowDesign", "About"))
        self.actionManual.setText(_translate("MainWindowDesign", "Manual"))
        self.actionQuit.setText(_translate("MainWindowDesign", "Quit"))
        self.actionAgradecimientos.setText(_translate("MainWindowDesign", "Agradecimientos"))

        MainWindowDesign.setWindowIcon(QtGui.QIcon(APP_LOGO))

    def runOnInit(self):
        """
        This function is executed right after the GUI is generated.
        In this function, the GUI is populated with the information
        of the last saved file.
        """
        userPreferences = getUserPreferences(CONFIG_FILE)
        basicInformation, timeRange = extractRequestInformation(userPreferences)

        self.planEstudioText.setText(basicInformation['PlanEstudio'])
        self.idiomaPaisText.setText(basicInformation['IdiomaPais'])
        self.trimestreSpinBox.setValue(int(basicInformation['Trimestre']))
        self.planDocenteText.setText(basicInformation['PlanDocente'])
        self.codigoCentroText.setText(basicInformation['CodigoCentro'])
        self.codigoEstudioText.setText(basicInformation['CodigoEstudio'])
        self.cursoSpinBox.setValue(int(basicInformation['Curso']))
        self.startDateEdit.setDate(QtCore.QDate.fromString(timeRange[0], 'dd/MM/yyyy'))
        self.endDateEdit.setDate(QtCore.QDate.fromString(timeRange[1], 'dd/MM/yyyy'))
        if isUsingEspaiAulaFilePath(userPreferences): self.filePathText.setText(getEspaiAulaFilePath(userPreferences))
        self.mainProgressBar.setValue(0)

        self.startDateEdit.setDisplayFormat('dd/MM/yyyy')
        self.endDateEdit.setDisplayFormat('dd/MM/yyyy')

    def clickSaveButton(self):
        planEstudio = self.planEstudioText.text()
        idiomaPais = self.idiomaPaisText.text()
        trimestre = self.trimestreSpinBox.text()
        planDocente = self.planDocenteText.text()
        codigoCentro = self.codigoCentroText.text()
        codigoEstudio = self.codigoEstudioText.text()
        curso = self.cursoSpinBox.text()

        insertUserPreferences(CONFIG_FILE, planEstudio, idiomaPais, trimestre, planDocente, codigoCentro, codigoEstudio, curso)

        return planEstudio, idiomaPais, trimestre, planDocente, codigoCentro, codigoEstudio, curso

    def clickAddButton(self):
        newSubject = {}

        newSubject['Code'] = self.subjectCodeText.text()
        newSubject['T'] = self.subjectTheoryText.text()
        newSubject['P'] = self.subjectPracticesText.text()
        newSubject['S'] = self.subjectSeminarsText.text()

        self.subjectCodeText.clear()
        self.subjectTheoryText.clear()
        self.subjectPracticesText.clear()
        self.subjectSeminarsText.clear()

        insertSubjectPreferences(CONFIG_FILE, newSubject)

        return newSubject['Code'], newSubject['T'], newSubject['P'], newSubject['S']

    def clickUseFileButton(self):
        insertFilePath(CONFIG_FILE, self.filePathText.text())
        return self.filePathText.text()

    def clickRemoveSubjectsButton(self): # Remove subjects from Google Calendar
        fromDate, toDate = self.startDateEdit.text(), self.endDateEdit.text()
        insertTimeRange(CONFIG_FILE, fromDate, toDate)
        self.mainProgressBar.setFormat("%p%")
        mainLoop = True
        applicationIterator = RunApplication(deleteMode=True, replaceMode=False)
        while mainLoop:
            try: self.updateMainLoadingBar(round(next(applicationIterator)))
            except StopIteration: mainLoop = False

        if self.mainProgressBar.value() == self.mainProgressBar.maximum():
            self.mainProgressBar.setFormat('Asignaturas Eliminadas')

    def clickAddSubjectsButton(self): # Add subjects to Google Calendar
        fromDate, toDate = self.startDateEdit.text(), self.endDateEdit.text()
        insertTimeRange(CONFIG_FILE, fromDate, toDate)
        self.mainProgressBar.setFormat("%p%")
        mainLoop = True
        applicationIterator = RunApplication()
        while mainLoop:
            try: self.updateMainLoadingBar(round(next(applicationIterator)))
            except StopIteration: mainLoop = False

        if self.mainProgressBar.value() == self.mainProgressBar.maximum():
            self.mainProgressBar.setFormat('Asignaturas Añadidas')

    def clickVerificationButton(self):
        self.progressBar.setValue(0)
        for i in range(checkEspaiAulaFileIntegrity(self.filePathText.text())):
            self.progressBar.setValue(i+1)

        if self.progressBar.value() == self.progressBar.maximum():
            self.progressBar.setFormat('Verificación Correcta')
            self.clickUseFileButton()

    def clickClearSubjectsButton(self): clearSubjectsPreferences(CONFIG_FILE)
    def updateMainLoadingBar(self, toValue): self.mainProgressBar.setValue(toValue)

    def runInformationWindow(self): print("Not implemented.")

    def openManual(self): webbrowser.open(README_URL)
    def openRepository(self): webbrowser.open(REPOSITORY_URL)
    def exitApplication(self): self.QtApplication.quit()

if __name__ == "__main__":
    QtApplication = QtWidgets.QApplication(sys.argv)
    # Dark Mode is still under development, but if you want to use it, uncomment the following line.
    # QtApplication.setPalette(darkPalette)

    MainWindowDesign = QtWidgets.QMainWindow()

    ApplicationUI = Ui_MainWindowDesign()
    ApplicationUI.setupUi(MainWindowDesign, QtApplication)

    MainWindowDesign.show()
    ApplicationUI.runOnInit()

    sys.exit(QtApplication.exec_())
