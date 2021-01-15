from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql.connector as mc
import pymysql, sys
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog



class Ui_AddWindow(object): 
   

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setStyleSheet('QMessageBox {background-color: rgb(0, 170, 127); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75);\
            border-radius: 10px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        mess.setWindowIcon(QtGui.QIcon("photo/barmm.ico"))
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def default(self):
        self.addPic_edit.setText("photo/Men.png")
        self.logo_label.setPixmap(QtGui.QPixmap("photo/Men.png"))
                  

    def insert_data(self):
        p = self.addPic_edit.text()
        if len(p) == 0:
            self.messageBox("Add Photo","You have no photo selected, \n Default Photo will be use!")
            self.default()
        else:
            
        
            with open(p, 'rb') as f:
                m=f.read()
          
            lname = self.lname_edit.text()
            fname = self.fname_edit.text()
            middle = self.middle_edit.text()
            bday = self.bday_edit.text()
            place = self.place_edit.text()
            sitio = self.sitio_edit.text()
            street = self.street_edit.text()
            position = self.position_combo.currentText()
            sex = self.sex_combo.currentText()
            status = self.civil_combo.currentText()
            supplementary = self.supp_combo.currentText()
       
            self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="barmm")
       
            query=("INSERT INTO resident (Last_name, Middle_name, First_name, Birth_date, Birth_place, Sex, Civil_status, Family_position, Sitio, Street, Supp_data,photo) VALUES  (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")
            cur=self.conn.cursor()
            data= cur.execute(query, (lname.upper(),middle.upper(),fname.upper(),bday.upper(),place.upper(), sex, status, position, sitio.upper(),street.upper(), supplementary,m))
        
            if (data):
                msg=QMessageBox()
                if    len(lname) == 0:
                    self.messageBox("Information", " Please Enter your Last Name!")
                    return
                elif  len(fname) == 0:
                    self.messageBox("Information", " Please Enter your First Name!")
                    return
                elif  len(middle)  == 0:
                    self.messageBox("Information", " Please Enter your Middle Name!")
                    return
                elif  len(bday) == 0:
                    self.messageBox("Information", " Please Enter your Birth Date!")
                    return
                elif  len(place)== 0:
                    self.messageBox("Information", " Please Enter your Place of Birth!")
                    return
                elif  len(sitio)== 0:
                    self.messageBox("Information", " Please Enter your Sitio!")
                    return
                elif  len(street)== 0:
                    self.messageBox("Information", " Please Enter House number or Street!")
                    return
            
                else:
                    self.messageBox("Saved", " Member Data Saved")
                    self.conn.commit()
                    self.clear_field()
               
    def clear_field(self):
        self.lname_edit.clear()
        self.fname_edit.clear()
        self.middle_edit.clear()
        self.bday_edit.clear()
        self.place_edit.clear()
        self.sitio_edit.clear()
        self.street_edit.clear()
        self.sex_combo.setCurrentIndex(0)
        self.civil_combo.setCurrentIndex(0)
        self.position_combo.setCurrentIndex(0)
        self.supp_combo.setCurrentIndex(0)
        self.addPic_edit.setText("photo/Men.png")
        self.logo_label.setPixmap(QtGui.QPixmap("photo/Men.png"))

    def browse_image(self):
        filename = QFileDialog.getOpenFileName( caption = "Open file", directory=None, filter="Image (*.png * .jpg);;All Files(*.*)")   
        self.addPic_edit.setText(filename[0])
        self.load_image()

    def load_image(self):
        p = self.addPic_edit.text()
        self.logo_label.setPixmap(QtGui.QPixmap(p))
      

    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(742, 710)
        AddWindow.setMaximumSize(QtCore.QSize(742, 710))
        AddWindow.setMinimumSize(QtCore.QSize(742, 710))
        AddWindow.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        AddWindow.setStyleSheet("background-color: rgb(75, 75, 75);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/barmm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")


        #HEADER FRAME
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.header_frame.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")

        #LAST NAME EDIT TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_edit.setGeometry(QtCore.QRect(30, 170, 311, 31))
        self.lname_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.lname_edit.setObjectName("lname_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lname_edit.setFont(font)

        #FIRST NAME EDIT TEXTBOX
        self.fname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_edit.setGeometry(QtCore.QRect(30, 310, 311, 31))
        self.fname_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.fname_edit.setObjectName("fname_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fname_edit.setFont(font)

        #MIDDLE NAME EDIT TEXTBOX
        self.middle_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.middle_edit.setGeometry(QtCore.QRect(30, 240, 311, 31))
        self.middle_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.middle_edit.setObjectName("middle_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.middle_edit.setFont(font)

        #DATE OF BIRTH EDIT TEXTBOX
        self.bday_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.bday_edit.setGeometry(QtCore.QRect(30, 380, 311, 31))
        self.bday_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.bday_edit.setText("")
        self.bday_edit.setObjectName("bday_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bday_edit.setFont(font)

        #PLACE OF BIRTH EDIT TEXTBOX
        self.place_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.place_edit.setGeometry(QtCore.QRect(30, 450, 311, 31))
        self.place_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.place_edit.setObjectName("place_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.place_edit.setFont(font)

        #SITIO EDIT TEXTBOX
        self.sitio_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sitio_edit.setGeometry(QtCore.QRect(410, 190, 301, 31))
        self.sitio_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.sitio_edit.setObjectName("sitio_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sitio_edit.setFont(font)

        #STREET ADDRESS EDIT TEXTBOX
        self.street_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.street_edit.setGeometry(QtCore.QRect(410, 230, 301, 31))
        self.street_edit.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.street_edit.setObjectName("street_edit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.street_edit.setFont(font)

        #ADD PICTURE EDIT TEXTBOX
        self.addPic_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.addPic_edit.setGeometry(QtCore.QRect(410, 120, 301, 31))
        self.addPic_edit.setStyleSheet("background-color: rgb(185, 185, 185);color: black")
        self.addPic_edit.setCursorPosition(0)
        self.addPic_edit.setObjectName("addPic_edit")
        self.addPic_edit.setText("photo/Men.png")
        self.addPic_edit.hide()

        #SAVE BUTTON
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(410, 600, 141, 41))
        self.save_btn.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.save_btn.setDefault(False)
        self.save_btn.setFlat(False)
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.insert_data)

        #add photo BUTTON
        self.add_photo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_photo_btn.setGeometry(QtCore.QRect(410, 555, 301, 21))
        self.add_photo_btn.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.add_photo_btn.setDefault(False)
        self.add_photo_btn.setFlat(False)
        self.add_photo_btn.setObjectName("add_photo_btn")
        self.add_photo_btn.clicked.connect(self.browse_image)

        #CANCEL BUTTON
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(570, 600, 141, 41))
        self.clear_btn.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.clear_btn.setDefault(False)
        self.clear_btn.setFlat(False)
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.clicked.connect(self.clear_field)

        #SEX COMBO BOX
        self.sex_combo = QtWidgets.QComboBox(self.centralwidget)
        self.sex_combo.setGeometry(QtCore.QRect(30, 520, 69, 32))
        self.sex_combo.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.sex_combo.setObjectName("sex_combo")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sex_combo.setFont(font)
        sex =["MALE", "FEMALE"]
        self.sex_combo.addItems(sex)
        
        #CIVIL STATUS COMBO BOX
        self.civil_combo = QtWidgets.QComboBox(self.centralwidget)
        self.civil_combo.setGeometry(QtCore.QRect(120, 520, 91, 32))
        self.civil_combo.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.civil_combo.setObjectName("civil_combo")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.civil_combo.setFont(font)
        civil = ["SINGLE", "MARRIED", "WIDDOW"]
        self.civil_combo.addItems(civil)
       
        #FAMILY POSITION COMBO BOX
        self.position_combo = QtWidgets.QComboBox(self.centralwidget)
        self.position_combo.setGeometry(QtCore.QRect(230, 520, 111, 32))
        self.position_combo.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.position_combo.setObjectName("position_combo")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.position_combo.setFont(font)
        fam_position = ["HEAD", "MEMBER"]
        self.position_combo.addItems(fam_position)

        #SUPPLEMENTARY DATA COMBO BOX
        self.supp_combo = QtWidgets.QComboBox(self.centralwidget)
        self.supp_combo.setGeometry(QtCore.QRect(30, 610, 201, 32))
        self.supp_combo.setStyleSheet("background-color: rgb(255, 255, 255);color: black")
        self.supp_combo.setObjectName("supp_combo")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.supp_combo.setFont(font)
        supp = ["NOT APPLICABLE","SENIOR CITIZEN", "PWD", "INDIGENOUS"]
        self.supp_combo.addItems(supp)

        #LASTNAME LABEL
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(30, 135, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lname_label.setFont(font)
        self.lname_label.setObjectName("lname_label")

        #APELYIDO LABEL
        self.apelyido_label = QtWidgets.QLabel(self.centralwidget)
        self.apelyido_label.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.apelyido_label.setObjectName("apelyido_label")

        #MIDDLE NAME LABEL
        self.middle_label = QtWidgets.QLabel(self.centralwidget)
        self.middle_label.setGeometry(QtCore.QRect(30, 205, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.middle_label.setFont(font)
        self.middle_label.setObjectName("middle_label")

        #GITNANG PANGALAN LABEL
        self.gitna_label = QtWidgets.QLabel(self.centralwidget)
        self.gitna_label.setGeometry(QtCore.QRect(30, 220, 91, 16))
        self.gitna_label.setObjectName("gitna_label")

        #FIRSTNAME LABEL
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(30, 275, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")

        #UNANG PANGALAN LABEL
        self.una_label = QtWidgets.QLabel(self.centralwidget)
        self.una_label.setGeometry(QtCore.QRect(30, 290, 91, 16))
        self.una_label.setObjectName("una_label")
        
        #DATE OF BIRTH LABEL
        self.dateofBirth_label = QtWidgets.QLabel(self.centralwidget)
        self.dateofBirth_label.setGeometry(QtCore.QRect(30, 345, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateofBirth_label.setFont(font)
        self.dateofBirth_label.setObjectName("dateofBirth_label")

        #PETSA NG KAPANGANAKAN LABEL
        self.petsa_label = QtWidgets.QLabel(self.centralwidget)
        self.petsa_label.setGeometry(QtCore.QRect(30, 360, 131, 16))
        self.petsa_label.setObjectName("petsa_label")

        #PLACE OF BIRTH LABEL
        self.place_label = QtWidgets.QLabel(self.centralwidget)
        self.place_label.setGeometry(QtCore.QRect(30, 415, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.place_label.setFont(font)
        self.place_label.setObjectName("place_label")

        #LUGAR NG KAPANGANAKAN LABEL
        self.lugar_label = QtWidgets.QLabel(self.centralwidget)
        self.lugar_label.setGeometry(QtCore.QRect(30, 430, 131, 16))
        self.lugar_label.setObjectName("lugar_label")

        #SEX LABEL
        self.sex_label = QtWidgets.QLabel(self.centralwidget)
        self.sex_label.setGeometry(QtCore.QRect(30, 485, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")

        #KASARIAN LABEL
        self.kasarian_label = QtWidgets.QLabel(self.centralwidget)
        self.kasarian_label.setGeometry(QtCore.QRect(30, 500, 51, 16))
        self.kasarian_label.setObjectName("kasarian_label")

        #CIVIL STATUS LABEL
        self.civil_label = QtWidgets.QLabel(self.centralwidget)
        self.civil_label.setGeometry(QtCore.QRect(120, 485, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.civil_label.setFont(font)
        self.civil_label.setObjectName("civil_label")

        #KALAGAYANG ESTADO LABEL
        self.kalagayan_label = QtWidgets.QLabel(self.centralwidget)
        self.kalagayan_label.setGeometry(QtCore.QRect(120, 500, 101, 16))
        self.kalagayan_label.setObjectName("kalagayan_label")

        #FAMILY POSITION LABEL
        self.familyPosition_label = QtWidgets.QLabel(self.centralwidget)
        self.familyPosition_label.setGeometry(QtCore.QRect(230, 485, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.familyPosition_label.setFont(font)
        self.familyPosition_label.setObjectName("familyPosition_label")

        #POSISYON SA PAMILYA LABEL
        self.posisyon_label = QtWidgets.QLabel(self.centralwidget)
        self.posisyon_label.setGeometry(QtCore.QRect(230, 500, 111, 16))
        self.posisyon_label.setObjectName("posisyon_label")

       
        #SUPPLEMENTARY DATA LABEL
        self.supp_label = QtWidgets.QLabel(self.centralwidget)
        self.supp_label.setGeometry(QtCore.QRect(30, 575, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.supp_label.setFont(font)
        self.supp_label.setObjectName("supp_label")

        #KARAGDAGANG DATOS LABEL
        self.karagdagan_label = QtWidgets.QLabel(self.centralwidget)
        self.karagdagan_label.setGeometry(QtCore.QRect(30, 590, 111, 16))
        self.karagdagan_label.setObjectName("karagdagan_label")

        #ADD NEW RESIDENT TITLE LABEL
        self.addNew_label = QtWidgets.QLabel(self.centralwidget)
        self.addNew_label.setGeometry(QtCore.QRect(250, 20, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.addNew_label.setFont(font)
        self.addNew_label.setObjectName("addNew_label")
        self.addNew_label.setStyleSheet("background-color: rgb(0, 170, 127);")

        #ADDRESS LABEL
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(410, 155, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")

        #TIRAHAN LABEL
        self.tirahan_label = QtWidgets.QLabel(self.centralwidget)
        self.tirahan_label.setGeometry(QtCore.QRect(410, 170, 91, 16))
        self.tirahan_label.setObjectName("tirahan_label")

        #LOGO
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(440, 301, 241, 231))
        self.logo_label.setObjectName("logo_label")
        self.logo_label.setPixmap(QtGui.QPixmap("photo/Men.png"))
        self.logo_label.setScaledContents(True)

        #BACKGROUND OF PICK
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        self.pic_label.setGeometry(QtCore.QRect(410, 280, 301, 271))
        self.pic_label.setAutoFillBackground(False)
        self.pic_label.setFrameShape(QtWidgets.QFrame.Box)
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")
        self.pic_label.setStyleSheet("background-color: rgb(0, 170, 127);")

       
        #RAISE FROM THE FRAME
        self.pic_label.raise_()
        self.fname_edit.raise_()
        self.fname_label.raise_()
        self.una_label.raise_()
        self.middle_edit.raise_()
        self.middle_label.raise_()
        self.gitna_label.raise_()
        self.lname_edit.raise_()
        self.lname_label.raise_()
        self.apelyido_label.raise_()
        self.bday_edit.raise_()
        self.dateofBirth_label.raise_()
        self.petsa_label.raise_()
        self.place_edit.raise_()
        self.place_label.raise_()
        self.lugar_label.raise_()
        self.sex_combo.raise_()
        self.sex_label.raise_()
        self.kasarian_label.raise_()
        self.civil_label.raise_()
        self.kalagayan_label.raise_()
        self.civil_combo.raise_()
        self.supp_label.raise_()
        self.supp_combo.raise_()
        self.karagdagan_label.raise_()
        self.addNew_label.raise_()
        self.save_btn.raise_()
        self.clear_btn.raise_()
        self.sitio_edit.raise_()
        self.address_label.raise_()
        self.tirahan_label.raise_()
        self.street_edit.raise_()
        self.logo_label.raise_()
        self.posisyon_label.raise_()
        self.familyPosition_label.raise_()
        self.position_combo.raise_()


        AddWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "Bangsamorro Autonomous Region in Muslim Mindanao"))
        self.fname_label.setText(_translate("AddWindow", "First Name:"))
        self.una_label.setText(_translate("AddWindow", "(Unang Pangalan)"))
        self.middle_label.setText(_translate("AddWindow", "Middle Name:"))
        self.gitna_label.setText(_translate("AddWindow", "(Gitnang Pangalan)"))
        self.lname_label.setText(_translate("AddWindow", "Last Name:"))
        self.apelyido_label.setText(_translate("AddWindow", "(Apelyido)"))
        self.dateofBirth_label.setText(_translate("AddWindow", "Date of Birth:"))
        self.petsa_label.setText(_translate("AddWindow", "(Petsa ng Kapanganakan)"))
        self.place_label.setText(_translate("AddWindow", "Place of Birth:"))
        self.lugar_label.setText(_translate("AddWindow", "(Lugar ng Kapanganakan)"))
        self.sex_label.setText(_translate("AddWindow", "Sex:"))
        self.kasarian_label.setText(_translate("AddWindow", "(Kasarian)"))
        self.civil_label.setText(_translate("AddWindow", "Civil Status:"))
        self.kalagayan_label.setText(_translate("AddWindow", "(Kalagayang Sibil)"))
        self.supp_label.setText(_translate("AddWindow", "Supplementary Data:"))
        self.karagdagan_label.setText(_translate("AddWindow", "(Karagdagang Datos)"))
        self.addNew_label.setText(_translate("AddWindow", "ADD NEW RESIDENT"))
        self.save_btn.setText(_translate("AddWindow", "Save"))
        self.add_photo_btn.setText(_translate("AddWindow", "Add Photo"))
        self.clear_btn.setText(_translate("AddWindow", "Clear"))
        self.address_label.setText(_translate("AddWindow", "Address:"))
        self.tirahan_label.setText(_translate("AddWindow", "(Tirahan)"))
        self.posisyon_label.setText(_translate("AddWindow", "(Posisyon sa Pamilyal)"))
        self.familyPosition_label.setText(_translate("AddWindow", "Family position:"))
        self.bday_edit.setPlaceholderText(_translate("AddWindow", "MM/DD/YYYY"))
        self.sitio_edit.setPlaceholderText(_translate("AddWindow", "SITIO"))
        self.street_edit.setPlaceholderText(_translate("AddWindow", "HOUSE NO./STREET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddWindow = QtWidgets.QMainWindow()
    ui = Ui_AddWindow()
    ui.setupUi(AddWindow)
    AddWindow.show()
    sys.exit(app.exec_())
