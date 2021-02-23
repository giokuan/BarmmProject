
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog, QPrinter
from PyQt5.Qt import QFileInfo
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLineEdit, QDialog ,QFileDialog, QInputDialog
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Ui_BusinessClearance(object):
    def handlePaintRequest(self, printer):
        printer.setResolution(1000)
        printer.setPageMargins(6, 5, 6, 5, QPrinter.Millimeter)
        painter = QPainter()
        painter.begin(printer)
        screenPixmap = self.centralwidget.grab()
        screenPixmap = screenPixmap.scaledToWidth(int(screenPixmap.width() *8000/screenPixmap.width()))
        painter.drawPixmap(10,10, screenPixmap)
        painter.end()
  


    def printPreviewListMethod(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()




    def setupUi(self, BusinessClearance):
        BusinessClearance.setObjectName("BusinessClearance")
        BusinessClearance.resize(682, 1000)
        self.centralwidget = QtWidgets.QWidget(BusinessClearance)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/tipaz_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BusinessClearance.setWindowIcon(icon)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 682, 892))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo/business_clearance.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.business_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.business_name_edit.setGeometry(QtCore.QRect(130, 298, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.business_name_edit.setFont(font)
        self.business_name_edit.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.business_name_edit.setFrame(False)
        self.business_name_edit.setObjectName("business_name_edit")
        
        self.address_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.address_edit.setGeometry(QtCore.QRect(80, 332, 541, 21))
        self.address_edit.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.address_edit.setFrame(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.address_edit.setFont(font)
        self.address_edit.setObjectName("address_edit")
        
        self.issued_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.issued_edit.setGeometry(QtCore.QRect(150, 500, 411, 21))
        self.issued_edit.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.issued_edit.setFrame(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.issued_edit.setFont(font)
        self.issued_edit.setObjectName("issued_edit")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 940, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.printPreviewListMethod)
        
        BusinessClearance.setCentralWidget(self.centralwidget)

        self.retranslateUi(BusinessClearance)
        QtCore.QMetaObject.connectSlotsByName(BusinessClearance)
        BusinessClearance.setTabOrder(self.business_name_edit, self.address_edit)

    def retranslateUi(self, BusinessClearance):
        _translate = QtCore.QCoreApplication.translate
        BusinessClearance.setWindowTitle(_translate("BusinessClearance", "Business Clearance"))
        self.pushButton.setText(_translate("BusinessClearance", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BusinessClearance = QtWidgets.QMainWindow()
    ui = Ui_BusinessClearance()
    ui.setupUi(BusinessClearance)
    BusinessClearance.show()
    sys.exit(app.exec_())
