from PyQt5 import QtCore, QtGui, QtWidgets,QtSql

from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog, QPrinter
from PyQt5.Qt import QFileInfo
from PyQt5.QtGui import QPainter

import mysql.connector as mc
import pymysql
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit, QDialog ,QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from barmm import Ui_AddWindow
#from delete_dialog import Ui_Dialog as Form


class Ui_MainForm(object):
   
    def open_window(self):#
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('barmm.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_() 

    def popup(self):
        msg=QMessageBox() 
        msg.setWindowIcon(QtGui.QIcon('barmm.ico'))
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you wan't to Exit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec_()
        if res == QMessageBox.Ok:  
            sys.exit()
        if res == QMessageBox.Cancel:
            pass 

    def search_allRadio(self):
        self.searchAll_btn.show()
        self.search_comboBox.show()
        self.search_btn.hide()
        self.search_edit.hide()
        self.advance_search.hide()
        self.adsearch_edit_lname.hide()
        self.adsearch_edit_fname.hide()

    def search_radio(self):
        self.searchAll_btn.hide()
        self.search_comboBox.hide()
        self.search_btn.show()
        self.search_edit.show()
        self.advance_search.hide()
        self.adsearch_edit_lname.hide()
        self.adsearch_edit_fname.hide()
       

    def addsearch_radio(self):
        self.searchAll_btn.hide()
        self.search_comboBox.hide()
        self.search_btn.hide()
        self.search_edit.hide()
        self.advance_search.show()
        self.adsearch_edit_lname.show()
        self.adsearch_edit_fname.show()
        
    def loadData(self):

        
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "barmm"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM resident ORDER BY last_name ASC" )
            result = mycursor.fetchall()
            
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    def cell_click(self,columnCount,rowCount):
        #self.cancel()
        #self.editbutton.setEnabled(True)
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
        cur=self.conn.cursor()
        item = self.tableWidget.selectedItems()
        i = (item[0].text())
        if rowCount != (0):
            return

        else:
            cur.execute ("SELECT * from resident WHERE Resident_ID=" +str(i))
            col = cur.fetchone()
            #print (col)           
            lname = col[1]
            mname = col[2]
            fname = col[3]
            civil = col[7]
            position = col[8]
            sex = col [6]
            sup = col[9]
            dob = col[4]
            pob = col[5]
            sitio = col[10]
            street = col[11]

        self.id_edit.setText(i)
        self.lname_edit.setText(lname)
        self.middle_edit.setText(mname)
        self.fname_edit.setText(fname)
        self.sex_comboBox.setCurrentText(sex)
        self.civil_comboBox.setCurrentText(civil)
        self.position_comboBox.setCurrentText(position)
        self.supp_comboBox.setCurrentText(sup)
        self.bday_edit.setText(dob)
        self.place_edit.setText(pob)
        self.sitio_edit.setText(sitio)
        self.street_edit.setText(street)
    
    def update(self):
        
        mem_id=self.id_edit.text()
        lname=self.lname_edit.text()
        mname=self.middle_edit.text()
        fname=self.fname_edit.text()
        sex=self.sex_comboBox.currentText()
        civil=self.civil_comboBox.currentText()
        position=self.position_comboBox.currentText()
        sup=self.supp_comboBox.currentText()
        dob=self.bday_edit.text()
        pob=self.place_edit.text()
        sitio=self.sitio_edit.text()
        street=self.street_edit.text()

        
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
        cur=self.conn.cursor()

        sql = "UPDATE resident SET Last_name = '"+ lname.upper() +"', First_name= '" + fname.upper() + "',\
                Middle_name = '" + mname.upper() + "', Sex= '" + sex.upper()\
                + "', Civil_status = '" + civil.upper() + "', Family_position = '" + position.upper()+ "', Supp_data = '" + sup.upper() + "',\
                Birth_date = '" + dob.upper() + "', Birth_place = '"\
                + pob.upper() + "', Sitio = '" + sitio.upper() + "', Street = '" + street.upper() + "'  WHERE Resident_ID = '"+mem_id+"' "
        
        if (sql):
            msg=QMessageBox()
            if    len(lname) == 0:
                self.messageBox("Information", " Please Enter your Last Name!")
                return
            elif  len(fname) == 0:
                self.messageBox("Information", " Please Enter your First Name!")
                return
            elif  len(mname)  == 0:
                self.messageBox("Information", " Please Enter your Middle Name!")
                return
            elif  len(dob) == 0:
                self.messageBox("Information", " Please Enter your Birth Date!")
                return
            elif  len(pob)== 0:
                self.messageBox("Information", " Please Enter your Place of Birth!")
                return
            elif  len(sitio)== 0:
                self.messageBox("Information", " Please Enter your Sitio!")
                return
            elif  len(street)== 0:
                self.messageBox("Information", " Please Enter House number or Street!")
                return
           
            else:
                cur.execute(sql)
                self.messageBox("Update", " Member Data Updated")
                self.conn.commit()
                self.cancel()
                self.loadData()

    def search(self):    
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "barmm"
            )
            mycursor = mydb.cursor()
            se = self.search_edit.text()
            mycursor.execute("SELECT * FROM resident WHERE last_name = '"+se+"'" );
            result = mycursor.fetchall()
          
            self.tableWidget.setRowCount(0)
           
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    def search_all(self):    
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "barmm"
            )
            mycursor = mydb.cursor()
            se = self.search_comboBox.currentText()
            mycursor.execute("SELECT * FROM resident WHERE Supp_data = '"+se+"' OR Family_position= '"+se+"' " );
            result = mycursor.fetchall()
          
            self.tableWidget.setRowCount(0)
           
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    def adv_search(self):    
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "barmm"
            )
            mycursor = mydb.cursor()
            adv_lname = self.adsearch_edit_lname.text()
            adv_fname = self.adsearch_edit_fname.text()
            mycursor.execute("SELECT * FROM resident WHERE Last_name = '"+adv_lname+"' AND First_name = '"+adv_fname+"' ");
            result = mycursor.fetchall()
            if len(adv_lname) == 0 or len(adv_fname) == 0:
                self.messageBox("Information", " Please Enter Last Name and First Name!")

            else:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)

                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    def delete_record(self):
        mem_id=self.id_edit.text()

        if len(mem_id) == 0:
            self.messageBox("Information", "No Record Found")
            return 

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
        cur=self.conn.cursor()
        sql = "DELETE FROM resident WHERE Resident_ID = '"+mem_id+"' "
        
        msg=QMessageBox() 
        msg.setWindowTitle("Delete")
        msg.setText("Are you sure you wan't to Delete this Record?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec_()
        if res == QMessageBox.Ok:
            self.open_dialog() 
            self.messageBox("Delete", " Resident Data Record Deleted")
            cur.execute(sql)
            self.conn.commit() 
            self.loadData()
            self.clear()
            
        if res == QMessageBox.Cancel:
            pass 

    def log(self):
        

        user=self.user_edit.text()
        password=self.pass_edit.text()

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
        cur=self.conn.cursor()
        data = cur.execute ("SELECT * from login WHERE user_name = '"+user+"' AND password = '"+password+"'")
        
        if (data):
            self.messageBox("Information", "You can now begin to Delete record")
            self.delete2_btn.show()
            self.delete_btn.hide()
            self.user_edit.clear()
            self.pass_edit.clear()
            self.deleteMode_label.show()
            self.pressCancel_label.show()
            self.ok_btn.setEnabled(False)
            self.residentData_frame.setStyleSheet("background-color: rgb(0, 170, 127);")
            self.table_frame.setStyleSheet("background-color: rgb(0, 170, 127);")

        else:
            self.messageBox("Information", "Invalid Username or Password")
            self.delete2_btn.hide()
            self.delete_btn.show()
            return

    def edit(self):
        mem_id=self.id_edit.text()
        if len(mem_id) == 0:
            self.messageBox("No Record", "No Record found")
            return
        else:
            self.lname_edit.setEnabled(True)
            self.middle_edit.setEnabled(True)
            self.fname_edit.setEnabled(True)
            self.sex_comboBox.setEnabled(True)
            self.civil_comboBox.setEnabled(True)
            self.position_comboBox.setEnabled(True)
            self.supp_comboBox.setEnabled(True)
            self.bday_edit.setEnabled(True)
            self.place_edit.setEnabled(True)
            self.sitio_edit.setEnabled(True)
            self.street_edit.setEnabled(True)
            self.update_btn.setEnabled(True)
            self.cancel_btn.setEnabled(True)
            self.edit_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
            self.refresh_btn.setEnabled(False)


    def cancel(self):
        self.lname_edit.setEnabled(False)
        self.middle_edit.setEnabled(False)
        self.fname_edit.setEnabled(False)
        self.sex_comboBox.setEnabled(False)
        self.civil_comboBox.setEnabled(False)
        self.position_comboBox.setEnabled(False)
        self.supp_comboBox.setEnabled(False)
        self.bday_edit.setEnabled(False)
        self.place_edit.setEnabled(False)
        self.sitio_edit.setEnabled(False)
        self.street_edit.setEnabled(False)
        self.update_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.edit_btn.setEnabled(True)
        self.delete_btn.setEnabled(True)
        self.refresh_btn.setEnabled(True)

    def cancel2(self):
        self.user_edit.hide()
        self.pass_edit.hide()
        self.user_label.hide()
        self.pass_label.hide()
        self.ok_btn.hide()
        self.canceled_btn.hide()
        self.deleteMode_label.hide()
        self.pressCancel_label.hide()
        self.delete_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)
        self.addnew_btn.setEnabled(True)
        self.print_btn.setEnabled(True)
        self.pdf_btn.setEnabled(True)
        self.residentData_frame.setStyleSheet("background-color: rgb();")
        self.table_frame.setStyleSheet("background-color: rgb();")

    def delete_show(self):
        self.user_edit.show()
        self.pass_edit.show()
        self.user_label.show()
        self.pass_label.show()
        self.ok_btn.show()
        self.canceled_btn.show()
        self.delete_btn.setEnabled(False)
        self.edit_btn.setEnabled(False)
        self.addnew_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
        self.pdf_btn.setEnabled(False)

    def clear(self):
        self.id_edit.clear()
        self.lname_edit.clear()
        self.middle_edit.clear()
        self.fname_edit.clear()
        self.sex_comboBox.setCurrentIndex(0)
        self.civil_comboBox.setCurrentIndex(0)
        self.position_comboBox.setCurrentIndex(0)
        self.supp_comboBox.setCurrentIndex(0)
        self.bday_edit.clear()
        self.place_edit.clear()
        self.sitio_edit.clear()
        self.street_edit.clear()

    def handlePaintRequest(self, printer):
        printer.setResolution(1000)
        printer.setPageMargins(6, 10, 1, 20, QPrinter.Millimeter)
        painter = QPainter()
        painter.begin(printer)
        screenPixmap = self.tableWidget.grab()
        screenPixmap = screenPixmap.scaledToWidth(int(screenPixmap.width() *8000/screenPixmap.width()))
        painter.drawPixmap(10,10, screenPixmap)
        painter.end()

    def printPreviewListMethod(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def pdf(self): 
        fileName, okPressed = QFileDialog.getSaveFileName( caption = "Export PDF", directory=None, \
                                                            filter="PDF Files(*.pdf);;All Files(*.*)")  
        if fileName != "":
            if QFileInfo(fileName).suffix() =="":
                fileName +=".pdf"  
            printer = QPrinter(QPrinter.HighResolution)
            printer.setPageMargins(6, 10, 1, 20, QPrinter.Millimeter)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fileName)
            painter = QPainter()
            painter.begin(printer)
            screenPixmap = self.tableWidget.grab()
            screenPixmap = screenPixmap.scaledToWidth(int(screenPixmap.width() *8000/screenPixmap.width()))
            painter.drawPixmap(10,10, screenPixmap)
            painter.end()

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1300, 906)
        MainForm.setMaximumSize(QtCore.QSize(1300, 906))
        MainForm.setMinimumSize(QtCore.QSize(1300, 906))
        #MainForm.setStyleSheet("background-color: rgb(0, 170, 127);")

        MainForm.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("barmm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")

        #TABLE WIDGET
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 220, 1202, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.loadData()
        self.tableWidget.cellClicked.connect(self.cell_click)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)


        #NAME OF BARANGAY LABEL
        self.nameOfBarangay_label = QtWidgets.QLabel(self.centralwidget)
        self.nameOfBarangay_label.setGeometry(QtCore.QRect(530, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nameOfBarangay_label.setFont(font)
        self.nameOfBarangay_label.setObjectName("nameOfBarangay_label") 

        #RESIDENT ID EDIT TEXTBOX
        self.id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_edit.setGeometry(QtCore.QRect(50, 510, 201, 31))
        self.id_edit.setObjectName("id_edit")
        self.id_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_edit.setFont(font)

        #LAST NAME EDIT TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_edit.setGeometry(QtCore.QRect(270, 510, 331, 31))
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lname_edit.setFont(font)

        #MIDDLE NAME EDIT TEXTBOX
        self.middle_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.middle_edit.setGeometry(QtCore.QRect(620, 510, 311, 31))
        self.middle_edit.setObjectName("middle_edit")
        self.middle_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.middle_edit.setFont(font)

        #FIRST NAME EDIT TEXTBOX
        self.fname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_edit.setGeometry(QtCore.QRect(950, 510, 311, 31))
        self.fname_edit.setObjectName("fname_edit")
        self.fname_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fname_edit.setFont(font)

        #BIRTHDAY EDIT TEXTBOX
        self.bday_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.bday_edit.setGeometry(QtCore.QRect(620, 580, 311, 31))
        self.bday_edit.setText("")
        self.bday_edit.setObjectName("bday_edit")
        self.bday_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bday_edit.setFont(font)

        #PLACE OF BIRTH EDIT TEXTBOX
        self.place_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.place_edit.setGeometry(QtCore.QRect(950, 580, 311, 31))
        self.place_edit.setObjectName("place_edit")
        self.place_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.place_edit.setFont(font)

        #SEX EDIT TEXTBOX
        self.sex_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.sex_comboBox.setGeometry(QtCore.QRect(50, 580, 86, 31))
        self.sex_comboBox.setObjectName("sex_comboBox")
        sex = ["MALE","FEMALE"]
        self.sex_comboBox.addItems(sex)
        self.sex_comboBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sex_comboBox.setFont(font)

        #CIVIL STATUS EDIT TEXTBOX
        self.civil_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.civil_comboBox.setGeometry(QtCore.QRect(155, 580, 96, 31))
        self.civil_comboBox.setObjectName("civil_comboBox")
        civil = ["SINGLE","MARRIED","WIDDOW"]
        self.civil_comboBox.addItems(civil)
        self.civil_comboBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.civil_comboBox.setFont(font)

        #FAMILY POSITION EDIT TEXTBOX
        self.position_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.position_comboBox.setGeometry(QtCore.QRect(270, 580, 121, 31))
        self.position_comboBox.setObjectName("position_comboBox")
        pos = ["HEAD","MEMBER"]
        self.position_comboBox.addItems(pos)
        self.position_comboBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.position_comboBox.setFont(font)

        #SUPPLEMENTARY COMBO BOX
        self.supp_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.supp_comboBox.setGeometry(QtCore.QRect(410, 580, 191, 31))
        self.supp_comboBox.setObjectName("supp_comboBox")
        sup = ["NOT APPLICABLE","SENIOR CITIZEN", "PWD", "INDIGENOUS"]
        self.supp_comboBox.addItems(sup)
        self.supp_comboBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.supp_comboBox.setFont(font)

        #SITIO EDIT TEXTBOX
        self.sitio_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sitio_edit.setGeometry(QtCore.QRect(140, 640, 301, 31))
        self.sitio_edit.setObjectName("sitio_edit") 
        self.sitio_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sitio_edit.setFont(font)

        #STREET EDIT TEXTBOX
        self.street_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.street_edit.setGeometry(QtCore.QRect(460, 640, 801, 31))
        self.street_edit.setObjectName("street_edit")
        self.street_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.street_edit.setFont(font)

        #USERNAME EDIT TEXTBOX
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setGeometry(QtCore.QRect(1090, 720, 181, 31))
        self.user_edit.setObjectName("user_edit")
        #self.user_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_edit.setFont(font)
        self.user_edit.hide()

        #PASSWORD EDIT TEXTBOX
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(1090, 770, 181, 31))
        self.pass_edit.setObjectName("pass_edit")
        #self.user_edit.setEnabled(False)
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_edit.setFont(font)
        self.pass_edit.hide()



        #SEARCH RADIO BUTTON
        self.search_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.search_radioButton.setGeometry(QtCore.QRect(40, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_radioButton.setFont(font)
        self.search_radioButton.setObjectName("search_radioButton")
        self.search_radioButton.toggled.connect(self.search_radio)
        self.search_radioButton.toggled.connect(lambda:self.adsearch_edit_lname.clear())
        self.search_radioButton.toggled.connect(lambda:self.adsearch_edit_fname.clear())
        self.search_radioButton.toggled.connect(lambda:self.loadData())

        #SEARCH ALL RADIO BUTTON
        self.searchAll_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.searchAll_radioButton.setGeometry(QtCore.QRect(110, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchAll_radioButton.setFont(font)
        self.searchAll_radioButton.setObjectName("searchAll_radioButton")
        self.searchAll_radioButton.toggled.connect(self.search_allRadio)
        self.searchAll_radioButton.toggled.connect(lambda:self.adsearch_edit_lname.clear())
        self.searchAll_radioButton.toggled.connect(lambda:self.adsearch_edit_fname.clear())
        self.searchAll_radioButton.toggled.connect(lambda:self.search_edit.clear())
        self.searchAll_radioButton.toggled.connect(lambda:self.loadData())
        
        #ADVANCE RADIO BUTTON
        self.advance_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.advance_radioButton.setGeometry(QtCore.QRect(200, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.advance_radioButton.setFont(font)
        self.advance_radioButton.setObjectName("advance_radioButton")
        self.advance_radioButton.toggled.connect(self.addsearch_radio)
        self.advance_radioButton.toggled.connect(lambda:self.search_edit.clear())
        self.advance_radioButton.toggled.connect(lambda:self.loadData())
        
        
        #USERNAME LABEL
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(1030, 730, 81, 16))
        self.user_label.setObjectName("user_label")
        self.user_label.hide()

        #PASSWORD LABEL
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(1030, 780, 81, 16))
        self.pass_label.setObjectName("pass_label")
        self.pass_label.hide()

        #NUMERONG ID NG RESIDENTE LABEL
        self.numeroID_label = QtWidgets.QLabel(self.centralwidget)
        self.numeroID_label.setGeometry(QtCore.QRect(50, 490, 141, 16))
        self.numeroID_label.setObjectName("numeroID_label")

        #RESIDENT ID LABEL
        self.res_id_label = QtWidgets.QLabel(self.centralwidget)
        self.res_id_label.setGeometry(QtCore.QRect(50, 480, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.res_id_label.setFont(font)
        self.res_id_label.setObjectName("res_id_label")

        #APELYIDO LABEL
        self.apelyido_label = QtWidgets.QLabel(self.centralwidget)
        self.apelyido_label.setGeometry(QtCore.QRect(270, 490, 91, 16))
        self.apelyido_label.setObjectName("apelyido_label")

        #LAST NAME LABEL
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(270, 480, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lname_label.setFont(font)
        self.lname_label.setObjectName("lname_label")

        #MIDDLE NAME LABEL
        self.middle_label = QtWidgets.QLabel(self.centralwidget)
        self.middle_label.setGeometry(QtCore.QRect(620, 480, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.middle_label.setFont(font)
        self.middle_label.setObjectName("middle_label")

        #GITNANG PANGALAN LABEL
        self.gitnangpangalan_label = QtWidgets.QLabel(self.centralwidget)
        self.gitnangpangalan_label.setGeometry(QtCore.QRect(620, 490, 91, 16))
        self.gitnangpangalan_label.setObjectName("gitnangpangalan_label")

        #FIRST NAME LABEL
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(950, 480, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")

        #UNANG PANGALAN LABEL
        self.unangpangalan_label = QtWidgets.QLabel(self.centralwidget)
        self.unangpangalan_label.setGeometry(QtCore.QRect(950, 490, 91, 16))
        self.unangpangalan_label.setObjectName("unangpangalan_label")

        #DATE OF BIRTH LABEL
        self.Dateofbirth_label = QtWidgets.QLabel(self.centralwidget)
        self.Dateofbirth_label.setGeometry(QtCore.QRect(620, 550, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Dateofbirth_label.setFont(font)
        self.Dateofbirth_label.setObjectName("Dateofbirth_label")

        #PETSA NG KAPANGANAKAN LABEL
        self.petsangkapanganaka_label = QtWidgets.QLabel(self.centralwidget)
        self.petsangkapanganaka_label.setGeometry(QtCore.QRect(620, 560, 131, 16))
        self.petsangkapanganaka_label.setObjectName("petsangkapanganaka_label")

        #PLACE OF BIRTH LABEL
        self.placeofbirth_label = QtWidgets.QLabel(self.centralwidget)
        self.placeofbirth_label.setGeometry(QtCore.QRect(950, 550, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.placeofbirth_label.setFont(font)
        self.placeofbirth_label.setObjectName("placeofbirth_label")

        #LUGAR NG KAPANGANAKAN LABEL
        self.lugarngkapanganakan_label = QtWidgets.QLabel(self.centralwidget)
        self.lugarngkapanganakan_label.setGeometry(QtCore.QRect(950, 560, 131, 16))
        self.lugarngkapanganakan_label.setObjectName("lugarngkapanganakan_label")

        #SEX LABEL
        self.sex_label = QtWidgets.QLabel(self.centralwidget)
        self.sex_label.setGeometry(QtCore.QRect(50, 550, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")

        #KASARIAN LABEL
        self.kasarian_label = QtWidgets.QLabel(self.centralwidget)
        self.kasarian_label.setGeometry(QtCore.QRect(50, 560, 141, 16))
        self.kasarian_label.setObjectName("kasarian_label")

        #CIVIL STATUS LABEL
        self.civil_label = QtWidgets.QLabel(self.centralwidget)
        self.civil_label.setGeometry(QtCore.QRect(155, 550, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.civil_label.setFont(font)
        self.civil_label.setObjectName("civil_label")

        #KALAGAYANG SIBIL LABEL
        self.kalagayansibil_label = QtWidgets.QLabel(self.centralwidget)
        self.kalagayansibil_label.setGeometry(QtCore.QRect(155, 560, 141, 16))
        self.kalagayansibil_label.setObjectName("kalagayansibil_label")

        #FAMILY POSITION LABEL
        self.familyPosition_label = QtWidgets.QLabel(self.centralwidget)
        self.familyPosition_label.setGeometry(QtCore.QRect(270, 550, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.familyPosition_label.setFont(font)
        self.familyPosition_label.setObjectName("familyPosition_label")

        #POSISYON LABEL
        self.posisyon_label = QtWidgets.QLabel(self.centralwidget)
        self.posisyon_label.setGeometry(QtCore.QRect(270, 560, 141, 16))
        self.posisyon_label.setObjectName("posisyon_label")

        #KARAGDAGANG DATOS LABEL
        self.karagdagangDatos_label = QtWidgets.QLabel(self.centralwidget)
        self.karagdagangDatos_label.setGeometry(QtCore.QRect(410, 560, 141, 16))
        self.karagdagangDatos_label.setObjectName("karagdagangDatos_label")

        #SUPPLEMENTAL DATA LABEL
        self.supp_label = QtWidgets.QLabel(self.centralwidget)
        self.supp_label.setGeometry(QtCore.QRect(410, 550, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.supp_label.setFont(font)
        self.supp_label.setObjectName("supp_label")

        #self.label_12 = QtWidgets.QLabel(self.centralwidget)
        #self.label_12.setGeometry(QtCore.QRect(50, 630, 47, 13))
        #self.label_12.setText("")
        #self.label_12.setObjectName("label_12")

        #ADDRESS LABEL
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(50, 640, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")

        #TIRAHAN LABEL
        self.tirahan_label = QtWidgets.QLabel(self.centralwidget)
        self.tirahan_label.setGeometry(QtCore.QRect(50, 650, 51, 16))
        self.tirahan_label.setObjectName("tirahan_label")

        
        #FRAME OF RESIDENT DATA
        self.residentData_frame = QtWidgets.QLabel(self.centralwidget)
        self.residentData_frame.setGeometry(QtCore.QRect(30, 470, 1242, 221))
        self.residentData_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.residentData_frame.setText("")
        self.residentData_frame.setObjectName("residentData_frame")
        #self.label_13.setStyleSheet("background-color: rgb(207, 207, 71);")

        #FRAME OF TABLE
        self.table_frame = QtWidgets.QLabel(self.centralwidget)
        self.table_frame.setGeometry(QtCore.QRect(30, 200, 1242, 261))
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setText("")
        self.table_frame.setObjectName("table_frame")
        #self.label_14.setStyleSheet("background-color: rgb(207, 207, 71);")

        #SITIO LABEL
        self.sitio_label = QtWidgets.QLabel(self.centralwidget)
        self.sitio_label.setGeometry(QtCore.QRect(140, 620, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sitio_label.setFont(font)
        self.sitio_label.setObjectName("sitio_label")

        #STREET LABEL
        self.stree_label = QtWidgets.QLabel(self.centralwidget)
        self.stree_label.setGeometry(QtCore.QRect(460, 620, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stree_label.setFont(font)
        self.stree_label.setObjectName("stree_label")

        #DELETE MODE LABEL
        self.deleteMode_label = QtWidgets.QLabel(self.centralwidget)
        self.deleteMode_label.setGeometry(QtCore.QRect(320, 780, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.deleteMode_label.setFont(font)
        self.deleteMode_label.setStyleSheet("border-color: rgb(255, 0, 0);")
        self.deleteMode_label.setObjectName("deleteMode_label")
        self.deleteMode_label.hide()

        #PRESS CANCEL LABEL
        self.pressCancel_label = QtWidgets.QLabel(self.centralwidget)
        self.pressCancel_label.setGeometry(QtCore.QRect(420, 820, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pressCancel_label.setFont(font)
        self.pressCancel_label.setStyleSheet("border-color: rgb(255, 0, 0);")
        self.pressCancel_label.setObjectName("deleteMode_label")
        self.pressCancel_label.hide()


        #ADD NEW BUTTON
        self.addnew_btn = QtWidgets.QPushButton(self.centralwidget)
        self.addnew_btn.setGeometry(QtCore.QRect(30, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addnew_btn.setFont(font)
        self.addnew_btn.setObjectName("addnew_btn")
        self.addnew_btn.clicked.connect(self.open_window)
        self.addnew_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #PRINT BUTTON
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(30, 780, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.print_btn.setFont(font)
        self.print_btn.setObjectName("print_btn")
        self.print_btn.clicked.connect(self.printPreviewListMethod)
        self.print_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #PDF BUTTON
        self.pdf_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pdf_btn.setGeometry(QtCore.QRect(170, 780, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pdf_btn.setFont(font)
        self.pdf_btn.setObjectName("pdf_btn")
        self.pdf_btn.clicked.connect(self.pdf)
        self.pdf_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #EDIT BUTTON
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(170, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edit_btn.setFont(font)
        self.edit_btn.setObjectName("edit_btn")
        self.edit_btn.clicked.connect(self.edit)
        self.edit_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #UPDATE BUTTON
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(310, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.update)
        self.update_btn.setEnabled(False)
        self.update_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #CANCEL BUTTON
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(450, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.cancel)
        self.cancel_btn.setEnabled(False)
        self.cancel_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #DELETE BUTTON
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(590, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.delete_btn.clicked.connect(self.delete_record)
        self.delete_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        ##DELETE 2 BUTTON
        #self.delete2_btn = QtWidgets.QPushButton(self.centralwidget)
        #self.delete2_btn.setGeometry(QtCore.QRect(590, 720, 121, 41))
        #font = QtGui.QFont()
        #font.setBold(True)
        #font.setWeight(75)
        #self.delete2_btn.setFont(font)
        #self.delete2_btn.setObjectName("delete2_btn")
        #self.delete2_btn.clicked.connect(self.delete_record)
        #self.delete2_btn.hide()
        #self.delete2_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #REFRESH BUTTON
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(730, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.loadData)
        self.refresh_btn.clicked.connect(self.search_radio)
        self.refresh_btn.clicked.connect(self.clear)
        self.refresh_btn.clicked.connect(lambda:self.search_radioButton.setChecked(True))
        self.refresh_btn.setStyleSheet("background-color: rgb(200, 200, 200);")
         
        #EXIT BUTTON
        self.Exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_btn.setGeometry(QtCore.QRect(870, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Exit_btn.setFont(font)
        self.Exit_btn.setObjectName("Exit_btn")
        self.Exit_btn.clicked.connect(self.popup)
        self.Exit_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #OK BUTTON DELETE
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(1090, 820, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.ok_btn.hide()
        self.ok_btn.clicked.connect(self.log)
        self.ok_btn.setStyleSheet("background-color: rgb(200, 200, 200);")
        
        #CANCELED BUTTON DELETE
        self.canceled_btn = QtWidgets.QPushButton(self.centralwidget)
        self.canceled_btn.setGeometry(QtCore.QRect(1190, 820, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.canceled_btn.setFont(font)
        self.canceled_btn.setObjectName("canceled_btn")
        self.canceled_btn.clicked.connect(self.clear)
        self.canceled_btn.clicked.connect(self.cancel2)
        self.canceled_btn.clicked.connect(lambda:self.delete2_btn.hide())
        self.canceled_btn.clicked.connect(lambda:self.delete_btn.show())
        self.canceled_btn.hide()
        self.canceled_btn.setStyleSheet("background-color: rgb(200, 200, 200);")
        
        #SEARCH BUTTON
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(30, 150, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.search)
        self.search_btn.setStyleSheet("background-color: rgb(200, 200, 200);")

        #SEARCH ALL BUTTON
        self.searchAll_btn = QtWidgets.QPushButton(self.centralwidget)
        self.searchAll_btn.setGeometry(QtCore.QRect(30, 150, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchAll_btn.setFont(font)
        self.searchAll_btn.setObjectName("searchAll_btn")
        self.searchAll_btn.hide()
        self.searchAll_btn.clicked.connect(self.search_all)
        self.searchAll_btn.setStyleSheet("background-color: rgb(200, 200, 200);")       

        #ADVANCE SEARCH BUTTON
        self.advance_search = QtWidgets.QPushButton(self.centralwidget)
        self.advance_search.setGeometry(QtCore.QRect(30, 150, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.advance_search.setFont(font)
        self.advance_search.setObjectName("advance_search")
        self.advance_search.hide()
        self.advance_search.clicked.connect(self.adv_search)
        self.advance_search.setStyleSheet("background-color: rgb(200, 200, 200);")

        #SEARCH EDIT TEXTBOX
        self.search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_edit.setGeometry(QtCore.QRect(170, 150, 201, 41))
        self.search_edit.setObjectName("search_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_edit.setFont(font)
        
        #ADVANCE SEARCH EDIT TEXTBOX LAST NAME
        self.adsearch_edit_lname = QtWidgets.QLineEdit(self.centralwidget)
        self.adsearch_edit_lname.setGeometry(QtCore.QRect(170, 150, 201, 41))
        self.adsearch_edit_lname.setObjectName("adsearch_edit_lname")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adsearch_edit_lname.setFont(font)
        self.adsearch_edit_lname.hide()

        #ADVANCE SEARCH EDIT TEXTBOX FIRST NAME
        self.adsearch_edit_fname = QtWidgets.QLineEdit(self.centralwidget)
        self.adsearch_edit_fname.setGeometry(QtCore.QRect(380, 150, 201, 41))
        self.adsearch_edit_fname.setObjectName("adsearch_edit_fname")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adsearch_edit_fname.setFont(font)
        self.adsearch_edit_fname.hide()

        #SEARCH COMBO BOX
        self.search_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.search_comboBox.setGeometry(QtCore.QRect(170, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.search_comboBox.setFont(font)
        self.search_comboBox.setObjectName("search_comboBox")
        search = ["SENIOR CITIZEN", "HEAD","PWD", "INDIGENOUS","NOT APPLICABLE"]
        self.search_comboBox.addItems(search)
        self.search_comboBox.hide()

        
        #FRAME OF RADIO BUTTONS
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 90, 341, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        #LABEL THAT CARRY A LOGO
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(1100, 30, 161, 151))
        self.logo_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("barmm.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        
        self.frame.raise_()
        self.residentData_frame.raise_()
        self.table_frame.raise_()
        self.tableWidget.raise_()
        #self.label.raise_()
        
        self.res_id_label.raise_()
        self.id_edit.raise_()
        self.numeroID_label.raise_()
        
        self.lname_edit.raise_()
        self.apelyido_label.raise_()
        self.lname_label.raise_()
        
        self.middle_edit.raise_()
        self.middle_label.raise_()
        self.gitnangpangalan_label.raise_()
        
        self.fname_edit.raise_()
        self.fname_label.raise_()
        self.unangpangalan_label.raise_()
        
        self.Dateofbirth_label.raise_()
        self.bday_edit.raise_()
        self.petsangkapanganaka_label.raise_()
        
        self.place_edit.raise_()
        self.placeofbirth_label.raise_()
        self.lugarngkapanganakan_label.raise_()
        
        self.sex_label.raise_()
        self.sex_comboBox.raise_()
        self.kasarian_label.raise_()
        
        self.civil_comboBox.raise_()
        self.civil_label.raise_()
        self.kalagayansibil_label.raise_()
        
        self.position_comboBox.raise_()
        self.familyPosition_label.raise_()
        self.posisyon_label.raise_()
        
        self.karagdagangDatos_label.raise_()
        self.supp_label.raise_()
        self.supp_comboBox.raise_()
        
        self.address_label.raise_()
        self.tirahan_label.raise_()
        
        self.sitio_edit.raise_()
        self.sitio_label.raise_()
        
        self.stree_label.raise_()
        self.street_edit.raise_()
        
        self.user_edit.raise_()
        self.user_label.raise_()
        self.pass_edit.raise_()
        
        self.addnew_btn.raise_()
        self.edit_btn.raise_()
        self.update_btn.raise_()
        self.delete_btn.raise_()
        self.cancel_btn.raise_()
        self.searchAll_btn.raise_()
        self.search_btn.raise_()
        self.Exit_btn.raise_()
        self.refresh_btn.raise_()

        self.search_comboBox.raise_()
        self.search_edit.raise_()
        self.search_radioButton.raise_()
        self.searchAll_radioButton.raise_()
        self.advance_radioButton.raise_()
        
        self.logo_label.raise_()

        MainForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "BANGSAMORO AUTONOMOUS REGION IN MUSLIM MINDANAO"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Resident ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainForm", "Middle Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainForm", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainForm", "Date of Birth"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainForm", "Place of Birth"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainForm", "Sex"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainForm", "Civil Status"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainForm", "Family Position"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainForm", "Sup. Data"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainForm", "Sitio"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainForm", "Street"))

        self.nameOfBarangay_label.setText(_translate("MainForm", "NAME OF BARANGAY"))
        self.res_id_label.setText(_translate("MainForm", "Resident ID:"))
        self.numeroID_label.setText(_translate("MainForm", "(Numerong ID ng Residente)"))
        self.apelyido_label.setText(_translate("MainForm", "(Apelyido)"))
        self.lname_label.setText(_translate("MainForm", "Last Name:"))
        self.middle_label.setText(_translate("MainForm", "Middle Name:"))
        self.gitnangpangalan_label.setText(_translate("MainForm", "(Gitnang Pangalan)"))
        self.fname_label.setText(_translate("MainForm", "First Name:"))
        self.unangpangalan_label.setText(_translate("MainForm", "(Unang Pangalan)"))
        self.Dateofbirth_label.setText(_translate("MainForm", "Date of Birth:"))
        self.petsangkapanganaka_label.setText(_translate("MainForm", "(Petsa ng Kapanganakan)"))
        self.placeofbirth_label.setText(_translate("MainForm", "Place of Birth:"))
        self.lugarngkapanganakan_label.setText(_translate("MainForm", "(Lugar ng Kapanganakan)"))
        self.sex_label.setText(_translate("MainForm", "Sex:"))
        self.kasarian_label.setText(_translate("MainForm", "(Kasarian)"))
        self.civil_label.setText(_translate("MainForm", "Civil Status:"))
        self.kalagayansibil_label.setText(_translate("MainForm", "(Kalagayang Sibil)"))
        self.familyPosition_label.setText(_translate("MainForm", "Family Position"))
        self.posisyon_label.setText(_translate("MainForm", "(Posisyon sa Pamilya)"))
        self.karagdagangDatos_label.setText(_translate("MainForm", "(Karagdagang Datos)"))
        self.supp_label.setText(_translate("MainForm", "Supplementary Data:"))
        self.address_label.setText(_translate("MainForm", "Address:"))
        self.tirahan_label.setText(_translate("MainForm", "(Tirahan)"))
        self.sitio_label.setText(_translate("MainForm", "Sitio:"))
        self.stree_label.setText(_translate("MainForm", "Street:"))
        self.user_label.setText(_translate("MainForm", "Username:"))
        self.pass_label.setText(_translate("MainForm", "Password:"))
        self.deleteMode_label.setText(_translate("MainForm", "YOU ARE ON DELETE MODE"))
        self.pressCancel_label.setText(_translate("MainForm", "PRESS CANCEL TO EXIT"))
        
        self.addnew_btn.setText(_translate("MainForm", "ADD NEW"))
        self.edit_btn.setText(_translate("MainForm", "EDIT"))
        self.update_btn.setText(_translate("MainForm", "UPDATE"))
        self.delete_btn.setText(_translate("MainForm", "DELETE"))
        self.delete2_btn.setText(_translate("MainForm", "DELETE"))
        self.cancel_btn.setText(_translate("MainForm", "CANCEL"))
        self.refresh_btn.setText(_translate("MainForm", "REFRESH"))
        self.searchAll_btn.setText(_translate("MainForm", "Search All"))
        self.advance_search.setText(_translate("MainForm", "Advance Search"))
        self.search_btn.setText(_translate("MainForm", "Search"))
        self.Exit_btn.setText(_translate("MainForm", "Exit"))
        self.ok_btn.setText(_translate("MainForm", "OK"))
        self.canceled_btn.setText(_translate("MainForm", "Cancel"))
        self.print_btn.setText(_translate("MainForm", "Print"))
        self.pdf_btn.setText(_translate("MainForm", "Print PDF"))
        
        self.search_radioButton.setText(_translate("MainForm", "Search"))
        self.searchAll_radioButton.setText(_translate("MainForm", "Search All"))
        self.advance_radioButton.setText(_translate("MainForm", "Advance Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
