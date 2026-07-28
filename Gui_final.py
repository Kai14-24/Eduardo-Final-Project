from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow:QtWidgets.QMainWindow) -> None:
         """here we are setting up the main window and all the widgets needed for the application"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #her we have the dog bread and the buttom for it to do the search
        self.breads = QtWidgets.QPushButton(self.centralwidget)
        self.breads.setGeometry(QtCore.QRect(20, 20, 110, 25))
        self.breads.setObjectName("breads")
        self.button_bread = QtWidgets.QPushButton(self.centralwidget)
        self.button_bread.setGeometry(QtCore.QRect(140, 20, 250, 25))
        self.button_bread.setObjectName("button_bread")

        #here we have the dog weight the actual weight
        self.label_input_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_input_weight.setGeometry(QtCore.QRect(20, 60, 100, 25))
        self.label_input_weight.setObjectName("label_input_weight")
        self.input_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.input_weight.setGeometry(QtCore.QRect(140, 60, 250, 25))
        self.input_weight.setPlaceholderText("Ej. 24.5")
        self.input_weight.setObjectName("input_weight")

        #here we have the  button for dog recommended weight calculation
        self.button_recommend_weight = QtWidgets.QPushButton(self.centralwidget)
        self.button_recommend_weight.setGeometry(QtCore.QRect(140, 100, 25 0, 30))
        self.button_recommend_weight.setObjectName("button_recommend_weight")

        #here we have the dog weight the actual weight result
        self.label_ideal_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_ideal_weight.setGeometry(QtCore.QRect(20, 140, 110, 25))
        self.label_ideal_weight.setObjectName("label_ideal_weight")
        self.ideal_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.ideal_weight.setGeometry(QtCore.QRect(140, 140, 210, 25))
        self.ideal_weight.setObjectName("ideal_weight")

        #here we have the weight evaluation button
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
        
        #here we have the dog breed information
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(20, 275, 110, 20))
        self.labelinfo.setObjectName("label_info")
        self.txt_info = QtWidgets.QLabel(self.centralwidget)
        self.txt_info.setGeometry(Qtcore.QRect(140, 275, 500, 100))
        self.txt_info.setReadOnly(True)
        self.txt_info.setObjectName("txt_info")
       
        #The error label
        self.label_error = QtWidgets.QTextxEdit(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(140, 365, 450, 20))
        self.label_error.setStyleSheet("color: Red;")
        self.label_error.setObjectName("label_error")

        MainWindow.setCentrelWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotaByName(MainWindow)

    def retranslateUi(self, MainWindow:QtWidgets.QMainWindow) -> None:
        """here we have the trasalete the aplicaton to the main window"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculate ideal Weight"))
        self.breads.setText(_translate("MainWindow", "Breads"))
        self.label_input_weight.setText(_translate("MainWindow", "Actual Weight (kg)"))
        self.label_ideal_weight.setText(_translate("MainWindow", "Ideal range"))
        self.label_status_titel.setText(_translate("MainWindow", "Result:"))
        self.label_lifespan.setText(_translate("MainWindow", "Lifespan"))
        self.label_pros.setText(_translate("MainWindow", "Information"))
        
