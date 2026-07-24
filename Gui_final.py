from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    """here we are setting up the main window and all the widgets needed for the application"""
    def setupUi(self, MainWindow:QtWidgets.QMainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #her we have the dog bread and the buttom for it to do the search
        self.breads = QtWidgets.QPushButton(self.centralwidget)
        self.breads.setGeometry(QtCore.QRect(20, 20, 110, 25))
        self.breads.setObjectName("breads")
        self.button_bread = QtWidgets.QPushButton(self.centralwidget)
        self.button_bread.setGeometry(QtCore.QRect(140, 55, 210, 25))
        self.button_bread.setObjectName("button_bread")

        #here we have the dog weight the actual weight
        self.label_input_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_input_weight.setGeometry(QtCore.QRect(20, 60, 100, 25))
        self.label_input_weight.setObjectName("label_input_weight")
        self.input_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.input_weight.setGeometry(QtCore.QRect(140, 60, 100, 25))
        self.input_weight.setPlaceholderText("Ej. 24.5")
        self.input_weight.setObjectName("input_weight")

        #here we have the  button for dog recommended weight calculation
        self.button_recommend_weight = QtWidgets.QPushButton(self.centralwidget)
        self.button_recommend_weight.setGeometry(QtCore.QRect(140, 95, 210, 30))
        self.button_recommend_weight.setObjectName("button_recommend_weight")

        #here we have the dog weight the actual weight result
        self.label_ideal_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_ideal_weight.setGeometry(QtCore.QRect(20, 140, 110, 25))
        self.label_ideal_weight.setObjectName("label_ideal_weight")
        self.ideal_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.ideal_weight.setGeometry(QtCore.QRect(140, 140, 210, 25))
        self.ideal_weight.setObjectName("ideal_weight")
        self.label_status_titel = QtWidgets.QLabel(self.centralwidget)
        self.label_status_titel.setGeometry(QtCore.QRect(20, 175, 110, 25))
        self.label_status_titel.setObjectName("label_status_titel")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(140, 175, 210, 25))
        self.label_status.setObjectName("label_status")

        #here we have the input and label for the lifespan
        self.label_lifespan = QtWidgets.QLabel(self.centralwidget)
        self.label_lifespan.setGeometry(QtCore.QRect(20, 210, 110, 25))
        self.label_lifespan.setObjectName("label_lifespan")
        self.lifespan = QtWidgets.QLineEdit(self.centralwidget)
        self.lifespan.setGeometry(QtCore.QRect(140, 210, 110, 25))
        self.lifespan.setObjectName("lifespan")
        #input age
        self.label_age = QtWidgets.QLabal(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(20, 310, 110, 25))
        self.label_age.setObjectname("label_age")
        self.label_age_status = QtWidgets.QLabal(self.centralwidget)
        self.label_age_status.setGeometry(QtCore.QRect(140, 310, 450, 25))
        self.label_age_status.setObjectname("label_age_status")
        

        #here we have the pro and cons of the dog bread
        #Pros
        self.label_pros = QtWidgets.QLabel(self.centralwidget)
        self.label_pros.setGeometry(QtCore.QRect(20, 245, 80, 20))
        self.label_pros.setObjectName("label_pro")
        self.txt_pros = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pros.setGeometry(QtCore.QRect(20, 270, 330, 55))
        self.txt_pros.setReadOnly(True)
        self.txt_pros.setObjectName("txt_pro")

        #Cons
        self.label_cons = QtWidgets.QLabel(self.centralwidget)
        self.label_cons.setGeometry(QtCore.QRect(20, 335, 80, 20))
        self.label_cons.setObjectName("label_cons")
        self.txt_cons = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cons.setGeometry(QtCore.QRect(20, 360, 330, 55))
        self.txt_cons.setReadOnly(True)
        self.txt_cons.setObjectName("txt_cons")

        #The error label
        self.label_error = QtWidgets.QTextxEdit(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(140, 365, 450, 20))
        self.label_error.setStyleSheet("color: Red;")
        self.label_error.setObjectName("label_error")

        MainWindow.setCentrelWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotaByName(MainWindow)

    def retranslateUi(self, MainWindow:QtWidgets.QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculate ideal Weight"))
        self.breads.setText(_translate("MainWindow", "Breads"))
        self.label_input_weight.setText(_translate("MainWindow", "Actual Weight (kg)"))
        self.label_ideal_weight.setText(_translate("MainWindow", "Ideal range"))
        self.label_status_titel.setText(_translate("MainWindow", "Result:"))
        self.label_lifespan.setText(_translate("MainWindow", "Lifespan"))
        self.label_pros.setText(_translate("MainWindow", "Pro"))
        self.label_cons.setText(_translate("MainWindow", "Con"))
