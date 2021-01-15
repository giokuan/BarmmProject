from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog, QPrinter
from PyQt5.Qt import QFileInfo
from PyQt5.QtGui import QPainter
import mysql.connector as mc
import pymysql
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit, QDialog ,QFileDialog, QInputDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from barmm import Ui_AddWindow


class Ui_MainWindow(object):

    def open_window(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setStyleSheet('QMessageBox {background-color: rgb(0, 170, 127); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75);\
            border-radius: 10px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        mess.setWindowIcon(QtGui.QIcon('photo/barmm.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_() 

    def exit_app(self):
        msg=QMessageBox()
        msg.setStyleSheet('QMessageBox {background-color: rgb(0, 170, 127); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75); \
            border-radius: 10px; padding: 10px; text-align: center;}QPushButton:hover{color: rgb(0, 170, 127);}') 
        msg.setWindowIcon(QtGui.QIcon('photo/barmm.ico'))
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

    def delete_messagebox(self):
        msg=QMessageBox() 
        msg.setWindowIcon(QtGui.QIcon('photo/barmm.ico'))
        msg.setStyleSheet('QMessageBox {background-color: rgb(0, 170, 127); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75); \
            border-radius: 10px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        msg.setWindowTitle("Delete")
        msg.setText("Are you sure you want to enter on Delete Mode")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec_()
        if res == QMessageBox.Ok:  
            MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.delete_btn.hide()
            self.delete_record_btn.show()
            self.refresh_btn.setEnabled(False)
            self.edit_btn.setEnabled(False)
            self.add_btn.setEnabled(False)
            self.cancel_btn.hide()
            self.cancel_delete_btn.show()
            
        if res == QMessageBox.Cancel:
            pass 

    def cancel_delete(self):
        MainWindow.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.delete_btn.show()
        self.delete_record_btn.hide()
        self.refresh_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)
        self.add_btn.setEnabled(True)
        self.cancel_btn.show()
        self.cancel_delete_btn.hide()

    def default(self):
        self.addPic_edit.setText("photo/Men.png")
        self.photo_label.setPixmap(QtGui.QPixmap("photo/Men.png"))
        

    def search_allRadio(self):
        self.search_all_btn.show()
        self.search_comboBox.show()
        self.search_btn.hide()
        self.search_edit.hide()
        self.advance_search_btn.hide()
        self.advanceLname_search_edit.hide()
        self.advanceFname_search_edit.hide()

    def search_radio(self):
        self.search_all_btn.hide()
        self.search_comboBox.hide()
        self.search_btn.show()
        self.search_edit.show()
        self.advance_search_btn.hide()
        self.advanceLname_search_edit.hide()
        self.advanceFname_search_edit.hide()

    def addsearch_radio(self):
        self.search_all_btn.hide()
        self.search_comboBox.hide()
        self.search_btn.hide()
        self.search_edit.hide()
        self.advance_search_btn.show()
        self.advanceLname_search_edit.show()
        self.advanceFname_search_edit.show()

    def edit(self):
        mem_id=self.id_edit.text()
        if len(mem_id) == 0:
            self.messageBox("No Record", "No Record found")
            return
        else:
            self.lname_edit.setEnabled(True)
            self.middle_edit.setEnabled(True)
            self.fname_edit.setEnabled(True)
            self.sex_combo.setEnabled(True)
            self.civilStatus_combo.setEnabled(True)
            self.family_position_combo.setEnabled(True)
            self.supplemental_combo.setEnabled(True)
            self.dob_edit.setEnabled(True)
            self.pob_edit.setEnabled(True)
            self.sitio_edit.setEnabled(True)
            self.street_address_edit.setEnabled(True)
            self.update_btn.setEnabled(True)
            self.cancel_btn.setEnabled(True)
            self.edit_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
            self.refresh_btn.setEnabled(False)
            self.addPhoto_btn.setEnabled(True)
            
            self.lname_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.fname_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.middle_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.sex_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.civilStatus_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.family_position_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.supplemental_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.dob_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.pob_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.sitio_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.street_address_edit.setStyleSheet("background-color: rgb(255, 255, 255);")

    def cancel(self):
        self.lname_edit.setEnabled(False)
        self.middle_edit.setEnabled(False)
        self.fname_edit.setEnabled(False)
        self.sex_combo.setEnabled(False)
        self.civilStatus_combo.setEnabled(False)
        self.family_position_combo.setEnabled(False)
        self.supplemental_combo.setEnabled(False)
        self.dob_edit.setEnabled(False)
        self.pob_edit.setEnabled(False)
        self.sitio_edit.setEnabled(False)
        self.street_address_edit.setEnabled(False)
        self.update_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.edit_btn.setEnabled(True)
        self.delete_btn.setEnabled(True)
        self.refresh_btn.setEnabled(True)
        self.addPhoto_btn.setEnabled(False)

        self.lname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.fname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.middle_edit.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.sex_combo.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.civilStatus_combo.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.family_position_combo.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.supplemental_combo.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.dob_edit.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.pob_edit.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.sitio_edit.setStyleSheet("background-color: rgb(185, 185, 185);color:black")
        self.street_address_edit.setStyleSheet("background-color: rgb(185, 185, 185);color:black")

    def clear(self):
        self.id_edit.clear()
        self.lname_edit.clear()
        self.middle_edit.clear()
        self.fname_edit.clear()
        self.sex_combo.setCurrentIndex(0)
        self.civilStatus_combo.setCurrentIndex(0)
        self.family_position_combo.setCurrentIndex(0)
        self.supplemental_combo.setCurrentIndex(0)
        self.dob_edit.clear()
        self.pob_edit.clear()
        self.sitio_edit.clear()
        self.street_address_edit.clear()
        self.photo_label.setPixmap(QtGui.QPixmap("photo/Men.png"))

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
            adv_lname = self.advanceLname_search_edit.text()
            adv_fname = self.advanceFname_search_edit.text()
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

        
    def update(self):

        p = self.addPic_edit.text()
        if len(p) == 0:
            self.messageBox("Add Photo","You have no photo selected, \nDefault Photo will be use")
            self.default()
        else:    
            with open(p, 'rb') as f:
                m=f.read()
        
            mem_id=self.id_edit.text()
            lname=self.lname_edit.text()
            mname=self.middle_edit.text()
            fname=self.fname_edit.text()
            sex=self.sex_combo.currentText()
            civil=self.civilStatus_combo.currentText()
            position=self.family_position_combo.currentText()
            sup=self.supplemental_combo.currentText()
            dob=self.dob_edit.text()
            pob=self.pob_edit.text()
            sitio=self.sitio_edit.text()
            street=self.street_address_edit.text()

        
            self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
            cur=self.conn.cursor()

            sql = "UPDATE resident SET Last_name = '"+ lname.upper() +"', First_name= '" + fname.upper() + "',\
                    Middle_name = '" + mname.upper() + "', Sex= '" + sex.upper()\
                    + "', Civil_status = '" + civil.upper() + "', Family_position = '" + position.upper()+ "', Supp_data = '" + sup.upper() + "',\
                    Birth_date = '" + dob.upper() + "', Birth_place = '"\
                    + pob.upper() + "', Sitio = '" + sitio.upper() + "', Street = '" + street.upper() + "', photo= %s WHERE Resident_ID = '"+mem_id+"' "
        
            if (sql):
                msg=QMessageBox()
                if      len(lname) == 0:
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
                    cur.execute(sql,m)
                    self.messageBox("Update", " Member Data Updated")
                    self.conn.commit()
                    #self.cancel()
                    self.loadData()
                    self.cancel()

    def cell_click(self,columnCount,rowCount):
       
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
            pic=col[12]

        self.id_edit.setText(i)
        self.lname_edit.setText(lname)
        self.middle_edit.setText(mname)
        self.fname_edit.setText(fname)
        self.sex_combo.setCurrentText(sex)
        self.civilStatus_combo.setCurrentText(civil)
        self.family_position_combo.setCurrentText(position)
        self.supplemental_combo.setCurrentText(sup)
        self.dob_edit.setText(dob)
        self.pob_edit.setText(pob)
        self.sitio_edit.setText(sitio)
        self.street_address_edit.setText(street)


        with open('photo/pic.png', 'wb') as f:
                f.write(pic)
                self.addPic_edit.setText('photo/pic.png')
                self.photo_label.setPixmap(QtGui.QPixmap("photo/pic.png"))
    

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
        fileName, okPressed = QFileDialog.getSaveFileName( caption = "Export PDF", directory=None, filter="PDF Files(*.pdf);;All Files(*.*)")  
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
            #self.open_dialog() 
            self.messageBox("Delete", " Resident Data Record Deleted")
            cur.execute(sql)
            self.conn.commit() 
            self.loadData()
            self.clear()
            
        if res == QMessageBox.Cancel:
            pass 


    def browse_image(self):
        filename = QFileDialog.getOpenFileName( caption = "Open file", directory=None, filter="Image (*.png * .jpg);;All Files(*.*)")   
        self.addPic_edit.setText(filename[0])
        self.load_image()
        

    def load_image(self):
        p = self.addPic_edit.text()
        self.photo_label.setPixmap(QtGui.QPixmap(p))
 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 845)
        MainWindow.setMaximumSize(QtCore.QSize(1292, 845))
        MainWindow.setMinimumSize(QtCore.QSize(1292, 845))
        MainWindow.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        MainWindow.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/barmm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        #######--------------------FRAMES--------------------###########
        
        #HEADER FRAME
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 1301, 111))
        self.header_frame.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")

        #SEARCH FRAME
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 420, 251, 271))
        self.frame.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        
        #RESIDENT DATA FRAME
        self.residentData_frame = QtWidgets.QFrame(self.centralwidget)
        self.residentData_frame.setGeometry(QtCore.QRect(290, 420, 981, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.residentData_frame.setFont(font)
        self.residentData_frame.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.residentData_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.residentData_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.residentData_frame.setObjectName("residentData_frame")
        
        #######################-------------------LABELS-----------------###############

        #TTILE LABEL (NAME OF BARANGAY)
        self.title_label = QtWidgets.QLabel(self.header_frame)
        self.title_label.setGeometry(QtCore.QRect(130, 20, 791, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")

        #HEADER LOGO LABEL
        self.headerLogo_label = QtWidgets.QLabel(self.header_frame)
        self.headerLogo_label.setGeometry(QtCore.QRect(10, 10, 101, 91))
        self.headerLogo_label.setText("")
        self.headerLogo_label.setPixmap(QtGui.QPixmap("photo/barmm.png"))
        self.headerLogo_label.setScaledContents(True)
        self.headerLogo_label.setObjectName("headerLogo_label")

        #RESIDENT ID LABEL
        self.id_label = QtWidgets.QLabel(self.residentData_frame)
        self.id_label.setGeometry(QtCore.QRect(10, 250, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")

        #PHOTO LABEL
        self.photo_label = QtWidgets.QLabel(self.residentData_frame)
        self.photo_label.setGeometry(QtCore.QRect(20, 60, 181, 181))
        self.photo_label.setFrameShape(QtWidgets.QFrame.Box)
        self.photo_label.setObjectName("photo_label")
        self.photo_label.setScaledContents(True)
        self.photo_label.setPixmap(QtGui.QPixmap("photo/Men.png"))
        self.photo_label.setScaledContents(True)

        #ADD PICTURE EDIT TEXTBOX
        self.addPic_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.addPic_edit.setGeometry(QtCore.QRect(320, 10, 191,41))
        self.addPic_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.addPic_edit.setCursorPosition(0)
        self.addPic_edit.setObjectName("addPic_edit")
        self.addPic_edit.setText("photo/Men.png")
        self.addPic_edit.hide()
 
        #LAST NAME LABEL
        self.lname_label = QtWidgets.QLabel(self.residentData_frame)
        self.lname_label.setGeometry(QtCore.QRect(230, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lname_label.setFont(font)
        self.lname_label.setObjectName("lname_label")
        
        #MIDDLE NAME LABEL
        self.middle_label = QtWidgets.QLabel(self.residentData_frame)
        self.middle_label.setGeometry(QtCore.QRect(230, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.middle_label.setFont(font)
        self.middle_label.setObjectName("middle_label")
        
        #FIRST NAME LABEL
        self.fname_label = QtWidgets.QLabel(self.residentData_frame)
        self.fname_label.setGeometry(QtCore.QRect(230, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")

        #PLACE OF BIRTH LABEL
        self.pob_label = QtWidgets.QLabel(self.residentData_frame)
        self.pob_label.setGeometry(QtCore.QRect(750, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pob_label.setFont(font)
        self.pob_label.setObjectName("pob_label")
        
        #HOUSE NUMBER LABEL
        self.houseStreet_label = QtWidgets.QLabel(self.residentData_frame)
        self.houseStreet_label.setGeometry(QtCore.QRect(460, 250, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.houseStreet_label.setFont(font)
        self.houseStreet_label.setObjectName("houseStreet_label")


        #CIVIL STATUS LABEL
        self.civilStatus_label = QtWidgets.QLabel(self.residentData_frame)
        self.civilStatus_label.setGeometry(QtCore.QRect(620, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.civilStatus_label.setFont(font)
        self.civilStatus_label.setObjectName("civilStatus_label")

        #SUPPLEMENTAL DATA LABEL
        self.supplemental_label = QtWidgets.QLabel(self.residentData_frame)
        self.supplemental_label.setGeometry(QtCore.QRect(750, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.supplemental_label.setFont(font)
        self.supplemental_label.setObjectName("supplemental_label")

        #FAMILY POSITION LABEL
        self.familyPosition_label = QtWidgets.QLabel(self.residentData_frame)
        self.familyPosition_label.setGeometry(QtCore.QRect(750, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.familyPosition_label.setFont(font)
        self.familyPosition_label.setObjectName("familyPosition_label")

        #SEX LABEL
        self.sex_label = QtWidgets.QLabel(self.residentData_frame)
        self.sex_label.setGeometry(QtCore.QRect(620, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        
        #SITIO LABEL
        self.sitio_label = QtWidgets.QLabel(self.residentData_frame)
        self.sitio_label.setGeometry(QtCore.QRect(110, 250, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sitio_label.setFont(font)
        self.sitio_label.setObjectName("sitio_label")

        #DATE OF BIRTH LABEL
        self.dob_label = QtWidgets.QLabel(self.residentData_frame)
        self.dob_label.setGeometry(QtCore.QRect(620, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dob_label.setFont(font)
        self.dob_label.setObjectName("dob_label")


        ###############--------------COMBO BOX--------------------##########################
        
        
        #CIVIL STATUS COMBO BOX
        self.civilStatus_combo = QtWidgets.QComboBox(self.residentData_frame)
        self.civilStatus_combo.setGeometry(QtCore.QRect(620, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.civilStatus_combo.setFont(font)
        self.civilStatus_combo.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.civilStatus_combo.setObjectName("civilStatus_combo")
        status = ["SINGLE", "MARRIED","WIDDOW"]
        self.civilStatus_combo.addItems(status)
        self.civilStatus_combo.setEnabled(False)
        
        #FAMILY POSITION COMBO BOX
        self.family_position_combo = QtWidgets.QComboBox(self.residentData_frame)
        self.family_position_combo.setGeometry(QtCore.QRect(750, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.family_position_combo.setFont(font)
        self.family_position_combo.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.family_position_combo.setObjectName("family_position_combo")
        position = ["HEAD", "MEMBER"]
        self.family_position_combo.addItems(position)
        self.family_position_combo.setEnabled(False)
        
        #SUPPLEMENTAL DATA COMBO BOX
        self.supplemental_combo = QtWidgets.QComboBox(self.residentData_frame)
        self.supplemental_combo.setGeometry(QtCore.QRect(750, 130, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.supplemental_combo.setFont(font)
        self.supplemental_combo.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.supplemental_combo.setObjectName("supplemental_combo")
        supp = ["NOT APPLICABLE", "SENIOR CITIZEN","PWD","INDIGENOUS"]
        self.supplemental_combo.addItems(supp)
        self.supplemental_combo.setEnabled(False)

        #SEX COMBO BOX
        self.sex_combo = QtWidgets.QComboBox(self.residentData_frame)
        self.sex_combo.setGeometry(QtCore.QRect(620, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sex_combo.setFont(font)
        self.sex_combo.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.sex_combo.setObjectName("sex_combo")
        sex = ["MALE", "FEMALE"]
        self.sex_combo.addItems(sex)
        self.sex_combo.setEnabled(False)
        

        ######## ------------------TEXTBOX -----------------------###########

        #SEARCH EDIT TEXTBOX
        self.search_edit = QtWidgets.QLineEdit(self.frame)
        self.search_edit.setGeometry(QtCore.QRect(10, 190, 201, 41))
        self.search_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.search_edit.setObjectName("search_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_edit.setFont(font)

        #ADVANCE LAST NAME SEARCH EDIT 
        self.advanceLname_search_edit = QtWidgets.QLineEdit(self.frame)
        self.advanceLname_search_edit.setGeometry(QtCore.QRect(10, 160, 201, 41))
        self.advanceLname_search_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.advanceLname_search_edit.setObjectName("advanceLname_search_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.advanceLname_search_edit.setFont(font)
        self.advanceLname_search_edit.hide()


        #ADVANCE FIRST NAME SEARCH EDIT
        self.advanceFname_search_edit = QtWidgets.QLineEdit(self.frame)
        self.advanceFname_search_edit.setGeometry(QtCore.QRect(10, 210, 201, 41))
        self.advanceFname_search_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.advanceFname_search_edit.setObjectName("advanceFname_search_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.advanceFname_search_edit.setFont(font)
        self.advanceFname_search_edit.hide()

        #SEARCH COMBO BOX
        self.search_comboBox = QtWidgets.QComboBox(self.frame)
        self.search_comboBox.setGeometry(QtCore.QRect(10, 190, 201, 41))
        self.search_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.search_comboBox.setFont(font)
        self.search_comboBox.setObjectName("search_comboBox")
        search = ["NOT APPLICABLE","SENIOR CITIZEN", "HEAD","PWD", "INDIGENOUS"]
        self.search_comboBox.addItems(search)
        self.search_comboBox.hide()

      
        #LAST NAME EDIT TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.lname_edit.setGeometry(QtCore.QRect(230, 60, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lname_edit.setFont(font)
        self.lname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.setEnabled(False)
        
        #MIDDLE NAME EDIT TEXTBOX
        self.middle_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.middle_edit.setGeometry(QtCore.QRect(230, 130, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.middle_edit.setFont(font)
        self.middle_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.middle_edit.setText("")
        self.middle_edit.setObjectName("middle_edit")
        self.middle_edit.setEnabled(False)

        #FIRST NAME EDIT TEXTBOX
        self.fname_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.fname_edit.setGeometry(QtCore.QRect(230, 200, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fname_edit.setFont(font)
        self.fname_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.fname_edit.setObjectName("fname_edit")
        self.fname_edit.setEnabled(False)
        
        #PLACE OF BIRTH EDIT TEXTBOX
        self.pob_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.pob_edit.setGeometry(QtCore.QRect(750, 200, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pob_edit.setFont(font)
        self.pob_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.pob_edit.setObjectName("pob_edit")
        self.pob_edit.setEnabled(False)
        
        
        #RESIDENT EDIT TEXTBOX
        self.id_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.id_edit.setGeometry(QtCore.QRect(10, 270, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_edit.setFont(font)
        self.id_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.id_edit.setObjectName("id_edit")
        self.id_edit.setEnabled(False)
        
        
        #DATE OF BIRTH EDIT TEXTBOX
        #self.dob_edit = QtWidgets.QDateEdit(self.residentData_frame)
        #self.dob_edit.setGeometry(QtCore.QRect(620, 200, 110, 41))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #self.dob_edit.setFont(font)
        #self.dob_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.dob_edit.setCalendarPopup(False)
        #self.dob_edit.setDate(QtCore.QDate(2021, 1, 1))
        #self.dob_edit.setObjectName("dob_edit")

        self.dob_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.dob_edit.setGeometry(QtCore.QRect(620, 200, 110, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dob_edit.setFont(font)
        self.dob_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.dob_edit.setObjectName("dob_edit")
        self.dob_edit.setEnabled(False)

        
        #SITIO EDIT TEXTBOX
        self.sitio_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.sitio_edit.setGeometry(QtCore.QRect(110, 270, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sitio_edit.setFont(font)
        self.sitio_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.sitio_edit.setObjectName("sitio_edit")
        self.sitio_edit.setEnabled(False)
        
        #HOUSE NUMBER / STREET ADDRESS EDIT TEXTBOX
        self.street_address_edit = QtWidgets.QLineEdit(self.residentData_frame)
        self.street_address_edit.setGeometry(QtCore.QRect(460, 270, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.street_address_edit.setFont(font)
        self.street_address_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.street_address_edit.setObjectName("street_address_edit")
        self.street_address_edit.setEnabled(False)
        
        ############--------------TABLE--------------------#########################################
        
        #TABLE FRAME
        self.table_frame = QtWidgets.QFrame(self.centralwidget)
        self.table_frame.setGeometry(QtCore.QRect(20, 130, 1251, 271))
        self.table_frame.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.table_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        
        self.tableWidget = QtWidgets.QTableWidget(self.table_frame)
        self.tableWidget.setGeometry(QtCore.QRect(24, 20, 1204, 231))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        font = self.tableWidget.font()
        font.setPointSize(10)
        self.tableWidget.setFont(font)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        
        self.loadData()
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.cellClicked.connect(self.cell_click)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setFixedHeight(50)
        self.tableWidget.setAlternatingRowColors(True)
        
        

        ############------BUTTONS--------###################################################


        #SEARCH RADIO BUTTON
        self.search_radioButton = QtWidgets.QRadioButton(self.frame)
        self.search_radioButton.setGeometry(QtCore.QRect(10, 20, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.search_radioButton.setFont(font)
        self.search_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.search_radioButton.setObjectName("searchAll_radioButton")
        self.search_radioButton.toggled.connect(self.search_radio)
        self.search_radioButton.toggled.connect(lambda:self.advanceLname_search_edit.clear())
        self.search_radioButton.toggled.connect(lambda:self.advanceFname_search_edit.clear())
        self.search_radioButton.toggled.connect(lambda:self.loadData())

        
        #SEARCH ALL RADIO BUTTON
        self.searchAll_radioButton = QtWidgets.QRadioButton(self.frame)
        self.searchAll_radioButton.setGeometry(QtCore.QRect(10, 50, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.searchAll_radioButton.setFont(font)
        self.searchAll_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.searchAll_radioButton.setObjectName("searchAll_radioButton")
        self.searchAll_radioButton.toggled.connect(self.search_allRadio)
        self.searchAll_radioButton.toggled.connect(lambda:self.advanceLname_search_edit.clear())
        self.searchAll_radioButton.toggled.connect(lambda:self.advanceFname_search_edit.clear())
        self.searchAll_radioButton.toggled.connect(lambda:self.search_edit.clear())
        self.searchAll_radioButton.toggled.connect(lambda:self.loadData())
        
        #ADVANCE SEARCH RADIO BUTTON
        self.advance_radioButton = QtWidgets.QRadioButton(self.frame)
        self.advance_radioButton.setGeometry(QtCore.QRect(10, 80, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.advance_radioButton.setFont(font)
        self.advance_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.advance_radioButton.setObjectName("advance_radioButton")
        self.advance_radioButton.toggled.connect(self.addsearch_radio)
        self.advance_radioButton.toggled.connect(lambda:self.search_edit.clear())
        self.advance_radioButton.toggled.connect(lambda:self.loadData())
        

        #ADD PHOTO BUTTON
        self.addPhoto_btn = QtWidgets.QPushButton(self.residentData_frame)
        self.addPhoto_btn.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addPhoto_btn.setFont(font)
        self.addPhoto_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.addPhoto_btn.setObjectName("addPhoto_btn")
        self.addPhoto_btn.clicked.connect(self.browse_image)
        self.addPhoto_btn.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPhoto_btn.setIcon(icon)


        #SEARCH BUTTON
        self.search_btn = QtWidgets.QPushButton(self.frame)
        self.search_btn.setGeometry(QtCore.QRect(10, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.search)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon)

        #SEARCH ALL BUTTON
        self.search_all_btn = QtWidgets.QPushButton(self.frame)
        self.search_all_btn.setGeometry(QtCore.QRect(10, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_all_btn.setFont(font)
        self.search_all_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.search_all_btn.setObjectName("search_all_btn")
        self.search_all_btn.hide()
        self.search_all_btn.clicked.connect(self.search_all)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_all_btn.setIcon(icon)

        #ADVANCE SEARCH BUTTON
        self.advance_search_btn = QtWidgets.QPushButton(self.frame)
        self.advance_search_btn.setGeometry(QtCore.QRect(10, 110, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.advance_search_btn.setFont(font)
        self.advance_search_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.advance_search_btn.setObjectName("advance_search_btn")
        self.advance_search_btn.hide()
        self.advance_search_btn.clicked.connect(self.adv_search)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.advance_search_btn.setIcon(icon)

        
        #EXIT BUTTON
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(1130, 770, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.exit_app)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)

        
        #CANCEL BUTTON
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(710, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setEnabled(False)
        self.cancel_btn.clicked.connect(self.cancel)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon)

        #CANCEL DELETE BUTTON
        self.cancel_delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_delete_btn.setGeometry(QtCore.QRect(710, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_delete_btn.setFont(font)
        self.cancel_delete_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.cancel_delete_btn.setObjectName("cancel_btn")
        self.cancel_delete_btn.hide()
        self.cancel_delete_btn.clicked.connect(self.cancel_delete)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_delete_btn.setIcon(icon)
        
        #REFRESH BUTTON
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(990, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.loadData)
        self.refresh_btn.clicked.connect(self.clear)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon)

        
        #EDIT BUTTON
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(430, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.edit_btn.setObjectName("edit_btn")
        self.edit_btn.clicked.connect(self.edit)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon)
        
        #UPDATE BUTTON
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(570, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.update_btn.setFont(font)
        self.update_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.update)
        self.update_btn.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_btn.setIcon(icon)

        
        #DELETE BUTTON
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(850, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.delete_btn.setObjectName("delete_btn")
        self.delete_btn.clicked.connect(self.delete_messagebox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon)

        #DELETE BUTTON 2
        self.delete_record_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_record_btn.setGeometry(QtCore.QRect(850, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delete_record_btn.setFont(font)
        self.delete_record_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.delete_record_btn.setObjectName("delete_btn")
        self.delete_record_btn.clicked.connect(self.delete_record)
        self.delete_record_btn.hide()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_record_btn.setIcon(icon)
        
        
        #ADD NEW BUTTON
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(290, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.open_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/reg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)
        
        #PRINT BUTTON
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(20, 710, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.print_btn.setFont(font)
        self.print_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.print_btn.setObjectName("print_btn")
        self.print_btn.clicked.connect(self.printPreviewListMethod)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_btn.setIcon(icon)

        
        #PRINT PDF BUTTON
        self.printPdf_btn = QtWidgets.QPushButton(self.centralwidget)
        self.printPdf_btn.setGeometry(QtCore.QRect(20, 770, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.printPdf_btn.setFont(font)
        self.printPdf_btn.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.printPdf_btn.setObjectName("printPdf_btn")
        self.printPdf_btn.clicked.connect(self.pdf)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printPdf_btn.setIcon(icon)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #TAB ORDER
        MainWindow.setTabOrder(self.lname_edit, self.middle_edit)
        MainWindow.setTabOrder(self.middle_edit, self.fname_edit)
        MainWindow.setTabOrder(self.fname_edit, self.sex_combo)
        MainWindow.setTabOrder(self.sex_combo, self.civilStatus_combo)
        MainWindow.setTabOrder(self.civilStatus_combo, self.dob_edit)
        MainWindow.setTabOrder(self.dob_edit, self.family_position_combo)
        MainWindow.setTabOrder(self.family_position_combo, self.supplemental_combo)
        MainWindow.setTabOrder(self.supplemental_combo, self.pob_edit)
        MainWindow.setTabOrder(self.pob_edit, self.sitio_edit)
        MainWindow.setTabOrder(self.sitio_edit, self.street_address_edit)
        MainWindow.setTabOrder(self.street_address_edit, self.search_btn)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BANGSAMORO AUTONOMOUS REGION IN MUSLIM MINDANAO"))
        self.title_label.setText(_translate("MainWindow", "NAME OF BARANGAY"))
        self.lname_label.setText(_translate("MainWindow", "Last Name"))
        self.middle_label.setText(_translate("MainWindow", "Middle Name"))
        self.fname_label.setText(_translate("MainWindow", "First Name"))
        self.sex_label.setText(_translate("MainWindow", "Sex"))
        self.civilStatus_label.setText(_translate("MainWindow", "Civil Status"))
        self.familyPosition_label.setText(_translate("MainWindow", "Family Position"))
        self.supplemental_label.setText(_translate("MainWindow", "Supplemental Data"))
        self.sitio_label.setText(_translate("MainWindow", "Sitio"))
        self.id_label.setText(_translate("MainWindow", "Resident ID"))
        self.dob_label.setText(_translate("MainWindow", "Date of Birth"))
        self.pob_label.setText(_translate("MainWindow", "Place of Birth"))
        self.houseStreet_label.setText(_translate("MainWindow", "House no./ Street"))
        self.addPhoto_btn.setText(_translate("MainWindow", "Change Photo"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "RESIDENT\n ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LAST\n NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MIDDLE\n NAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "FIRST\n NAME"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DATE OF \nBIRTH"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PLACE OF\n BIRTH"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SEX"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CIVIL \n STATUS"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "FAMILY \n POSITION"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "SUPPLEMENTAL \n DATA"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "SITIO"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "STREET"))
        
        self.search_radioButton.setText(_translate("MainWindow", "Search"))
        self.searchAll_radioButton.setText(_translate("MainWindow", "Search All"))
        self.advance_radioButton.setText(_translate("MainWindow", "Advance Search"))

        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.search_all_btn.setText(_translate("MainWindow", "Search All"))
        self.advance_search_btn.setText(_translate("MainWindow", "Advance Search"))

        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.cancel_delete_btn.setText(_translate("MainWindow", "Cancel"))

        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.edit_btn.setText(_translate("MainWindow", "Edit"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.delete_record_btn.setText(_translate("MainWindow", "Delete Record"))

        self.add_btn.setText(_translate("MainWindow", "Add New"))
        self.print_btn.setText(_translate("MainWindow", "Print"))
        self.printPdf_btn.setText(_translate("MainWindow", "Print PDF"))
        self.advanceLname_search_edit.setPlaceholderText(_translate("MainWindow", "Enter Last Name"))
        self.advanceFname_search_edit.setPlaceholderText(_translate("MainWindow", "Enter First Name"))
        self.search_edit.setPlaceholderText(_translate("MainWindow", "Enter Last Name"))
        self.dob_edit.setPlaceholderText(_translate("MainWindow", "MM/DD/YYYY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
