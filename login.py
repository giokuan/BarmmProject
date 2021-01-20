from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from BarmmNew import Ui_MainWindow

class Ui_MainForm(object):
    def open_window(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainForm.hide()
        self.window.show()

    def pop(self):
        sys.exit() 

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setStyleSheet('QMessageBox {background-color: qlineargradient(spread:pad,\
             x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255)); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75);\
            border-radius: 10px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        mess.setWindowIcon(QtGui.QIcon('photo/barmm.ico'))
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def register(self):
        self.lname_edit.show()
        self.fname_edit.show()
        self.confirm_edit.show()
        self.lname_label.show()
        self.fname_label.show()
        self.confirm_label.show()
        self.save_btn.show()
        self.reg_btn.hide()
        self.login_btn.setEnabled(False)
        self.cancel_btn.setEnabled(True)
        #self.header_frame.setGeometry(QtCore.QRect(0, 0, 600, 81))
        self.logo2_label.show()
        self.logo_label.hide()


    def cancel(self):
        self.lname_edit.hide()
        self.fname_edit.hide()
        self.confirm_edit.hide()
        self.lname_label.hide()
        self.fname_label.hide()
        self.confirm_label.hide()
        self.save_btn.hide()
        self.reg_btn.show()
        self.user_edit.clear()
        self.pass_edit.clear()
        self.login_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)
        #self.header_frame.setGeometry(QtCore.QRect(0, 5, 600, 151))
        self.logo2_label.hide()
        self.logo_label.show()

    def log(self):

        user=self.user_edit.text()
        password=self.pass_edit.text()

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
        cur=self.conn.cursor()
        data = cur.execute ("SELECT * from login WHERE user_name = '"+user+"' AND password = '"+password+"'")
        
        if (data):
            self.messageBox("Information", "Login Successful")
            self.open_window()
        else:
            self.messageBox("Information", "Invalid Username or Password")
            return


    def save(self):
        lname=self.lname_edit.text()
        fname=self.fname_edit.text()
        user=self.user_edit.text()
        password=self.pass_edit.text()
        confirm=self.confirm_edit.text()

        if password != confirm:
            self.messageBox("Information", "Password not match")

        else:

            self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
       
            query=("INSERT INTO login (last_name, first_name, user_name, password) VALUES  (%s, %s, %s,%s)")
            cur=self.conn.cursor()

            data= cur.execute(query, (lname.upper(),fname.upper(),user,password))
        

            if (data):
                msg=QMessageBox()
                if    len(lname) == 0:
                    self.messageBox("Information", " Last Name Cannot be empty!")
                    return
                elif  len(fname) == 0:
                    self.messageBox("Information", " First Name Cannot be empty!")
                    return
                elif  len(user)  == 0:
                    self.messageBox("Information", " username Cannot be empty!")
                    return
                elif  len(password) == 0:
                    self.messageBox("Information", " Password Cannot be empty!")
                    return
        

                else:
                    self.messageBox("Saved", " Member Data Saved")
                    self.conn.commit()
                    self.save_btn.hide()
                    self.lname_edit.hide()
                    self.fname_edit.hide()
                    self.confirm_edit.hide()
                    self.lname_label.hide()
                    self.fname_label.hide()
                    self.confirm_label.hide()
                    self.reg_btn.show()
                    self.user_edit.clear()
                    self.pass_edit.clear()
                    self.login_btn.setEnabled(True)
                    self.cancel_btn.setEnabled(False)

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(600, 400)
        #MainForm.setStyleSheet("background-color: rgb(75, 75, 75);")
        #MainWindow.setWindowFlags( QtCore.Qt.CustomizeWindowHint )
        MainForm.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        MainForm.setMaximumSize(QtCore.QSize(600, 400))
        MainForm.setMinimumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/barmm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")

        #BACKGROUND LABEL
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.background_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("photo/back3.png"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")


        #BIG LOGO HEADER TRANSITION WITH LOGO2_LABEL
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(240, 10, 301, 71))
        self.logo_label.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.logo_label.setFont(font)
        self.logo_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo_label.setObjectName("logo_label")

        #SMALL LOGO HEADER TRANSITION WITH LOGO_LABEL
        self.logo2_label = QtWidgets.QLabel(self.centralwidget)
        self.logo2_label.setGeometry(QtCore.QRect(220, 10, 301, 71))
        self.logo2_label.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.logo2_label.setFont(font)
        self.logo2_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo2_label.setObjectName("logo2_label")
        self.logo2_label.hide()

        
        #REGISTER BUTTON
        self.reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reg_btn.setGeometry(QtCore.QRect(90, 330, 91, 41))
        self.reg_btn.setStyleSheet("background-color: qlineargradient(spread:pad,\
             x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));color: black")
        self.reg_btn.setObjectName("reg_btn")
        self.reg_btn.clicked.connect(self.register)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/reg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reg_btn.setIcon(icon)

        #SAVE BUTTON
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(90, 330, 91, 41))
        self.save_btn.setStyleSheet("background-color: qlineargradient(spread:pad,\
             x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));color: black")
        self.save_btn.setObjectName("save_btn")
        self.save_btn.hide()
        self.save_btn.clicked.connect(self.save)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon)

        #LOG IN BUTTON
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(200, 330, 91, 41))
        self.login_btn.setStyleSheet("background-color: qlineargradient(spread:pad,\
             x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));color: black")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.log)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon)
        
        #CANCEL BUTTON
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(310, 330, 91, 41))
        self.cancel_btn.setStyleSheet("background-color: qlineargradient(spread:pad,\
             x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));color: black")
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.cancel)
        self.cancel_btn.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon)

        #EXIT BUTTON
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(420, 330, 91, 41))
        self.exit_btn.setStyleSheet("background-color: qlineargradient(spread:pad,\
             x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));color: black")
        self.exit_btn.setObjectName("cancel_btn")
        self.exit_btn.clicked.connect(self.pop)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)

        #LASSTNAME EDIT TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_edit.setGeometry(QtCore.QRect(130, 100, 181, 31))
        self.lname_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.hide()
        
        #FIRSTNAME EDIT TEXTBOX
        self.fname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_edit.setGeometry(QtCore.QRect(130, 140, 181, 31))
        self.fname_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.fname_edit.setObjectName("fname_edit")
        self.fname_edit.hide()
        
        #USERNAME EDIT TEXTBOX
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setGeometry(QtCore.QRect(130, 180, 181, 31))
        self.user_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.user_edit.setObjectName("user_edit")
        
        #PASSWORD EDIT TEXTBOX
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(130, 220, 181, 31))
        self.pass_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_edit.setObjectName("pass_edit")
        
        #CONFIRM PASSWORD EDIT TEXTBOX
        self.confirm_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_edit.setGeometry(QtCore.QRect(130, 260, 181, 31))
        self.confirm_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.confirm_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_edit.setObjectName("confirm_edit")
        self.confirm_edit.hide()
        
        #BARMM LOGO LABEL
        self.middle_logo_label = QtWidgets.QLabel(self.centralwidget)
        self.middle_logo_label.setGeometry(QtCore.QRect(350, 95, 201, 191))
        self.middle_logo_label.setPixmap(QtGui.QPixmap("photo/logo_login.png"))
        self.middle_logo_label.setScaledContents(True)
        self.middle_logo_label.setObjectName("middle_logo_label")
        
        #LASTNAME LABEL
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(30, 105, 61, 16))
        self.lname_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.lname_label.setObjectName("lname_label")
        self.lname_label.hide()
        
        #FIRSTNAME LABEL
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(30, 145, 61, 16))
        self.fname_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.fname_label.setObjectName("fname_label")
        self.fname_label.hide()
        
        #USERNAME
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(30, 185, 61, 16))
        self.user_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_label.setObjectName("user_label")
        
        #PASSWORD LABEL
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(30, 225, 61, 16))
        self.pass_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.pass_label.setObjectName("pass_label")
        
        #CONFIRM PASSWORD LABEL
        self.confirm_label = QtWidgets.QLabel(self.centralwidget)
        self.confirm_label.setGeometry(QtCore.QRect(30, 265, 91, 16))
        self.confirm_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.confirm_label.setObjectName("confirm_label")
        self.confirm_label.hide()
        
        MainForm.setCentralWidget(self.centralwidget)
        #self.statusbar = QtWidgets.QStatusBar(MainForm)
        #self.statusbar.setObjectName("statusbar")
        #MainForm.setStatusBar(self.statusbar)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Bangsamoro Autonomous Region in Muslim Mindanao"))
        self.reg_btn.setText(_translate("MainForm", "Register"))
        self.login_btn.setText(_translate("MainForm", "Log In"))
        self.cancel_btn.setText(_translate("MainForm", "Cancel"))
        self.exit_btn.setText(_translate("MainForm", "Exit"))
        self.save_btn.setText(_translate("MainForm", "Save"))
        self.lname_label.setText(_translate("MainForm", "Last Name:"))
        self.fname_label.setText(_translate("MainForm", "First Name:"))
        self.user_label.setText(_translate("MainForm", "Username:"))
        self.pass_label.setText(_translate("MainForm", "Password:"))
        self.confirm_label.setText(_translate("MainForm", "Confirm Password:"))
        self.logo_label.setText(_translate("MainForm", "Login"))
        self.logo2_label.setText(_translate("MainForm", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
