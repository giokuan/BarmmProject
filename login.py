from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from main_form import Ui_MainForm

class Ui_MainWindow(object):
    def open_window(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def pop(self):
        sys.exit() 

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        #MainWindow.setWindowFlags( QtCore.Qt.CustomizeWindowHint )
        MainWindow.setMaximumSize(QtCore.QSize(600, 480))
        MainWindow.setMinimumSize(QtCore.QSize(600, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("barmm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reg_btn.setGeometry(QtCore.QRect(90, 320, 91, 41))
        self.reg_btn.setObjectName("reg_btn")
        self.reg_btn.clicked.connect(self.register)

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(90, 320, 91, 41))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.hide()
        self.save_btn.clicked.connect(self.save)

        
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(200, 320, 91, 41))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.log)
        
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(310, 320, 91, 41))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.cancel)

        
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(420, 320, 91, 41))
        self.exit_btn.setObjectName("cancel_btn")
        self.exit_btn.clicked.connect(self.pop)

        self.lname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_edit.setGeometry(QtCore.QRect(130, 70, 181, 31))
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.hide()
        
        self.fname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_edit.setGeometry(QtCore.QRect(130, 110, 181, 31))
        self.fname_edit.setObjectName("fname_edit")
        self.fname_edit.hide()
        
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setGeometry(QtCore.QRect(130, 150, 181, 31))
        self.user_edit.setObjectName("user_edit")
        
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(130, 190, 181, 31))
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_edit.setObjectName("pass_edit")
        
        self.confirm_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_edit.setGeometry(QtCore.QRect(130, 230, 181, 31))
        self.confirm_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_edit.setObjectName("confirm_edit")
        self.confirm_edit.hide()
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 70, 201, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("barmm.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.lname_label.setObjectName("lname_label")
        self.lname_label.hide()
        
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.fname_label.setObjectName("fname_label")
        self.fname_label.hide()
        
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.user_label.setObjectName("user_label")
        
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(30, 190, 61, 16))
        self.pass_label.setObjectName("pass_label")
        
        self.confirm_label = QtWidgets.QLabel(self.centralwidget)
        self.confirm_label.setGeometry(QtCore.QRect(30, 230, 91, 16))
        self.confirm_label.setObjectName("confirm_label")
        self.confirm_label.hide()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bangsamoro Autonomous Region in Muslim Mindanao"))
        self.reg_btn.setText(_translate("MainWindow", "Register"))
        self.login_btn.setText(_translate("MainWindow", "Log In"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.lname_label.setText(_translate("MainWindow", "Last Name:"))
        self.fname_label.setText(_translate("MainWindow", "First Name:"))
        self.user_label.setText(_translate("MainWindow", "Username:"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.confirm_label.setText(_translate("MainWindow", "Confirm Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
