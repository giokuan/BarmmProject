
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog, QPrinter
from PyQt5.Qt import QFileInfo
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLineEdit, QDialog ,QFileDialog, QInputDialog
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Ui_MainClear(object):

    # def handlePaintRequest(self, printer):
    #     document = QtGui.QTextDocument()
    #     #cursor = QtGui.QTextCursor(document)
    #     document.print_(printer)

    def handlePaintRequest(self, printer):
        printer.setResolution(1000)
        printer.setPageMargins(6, 2, 6, 5, QPrinter.Millimeter)
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
    



    def setupUi(self, MainClear):
        MainClear.setObjectName("MainClear")
        MainClear.resize(681, 980)
        MainClear.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainClear)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 931))
        self.label.setStyleSheet("background-color: rgb(197, 224, 179);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo/tipaz_clearance.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(200, 366, 161, 20))
        self.name_edit.setFrame(False)
        self.name_edit.setObjectName("name_edit")
        
        self.age_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.age_edit.setGeometry(QtCore.QRect(373, 366, 31, 20))
        self.age_edit.setFrame(False)
        self.age_edit.setObjectName("age_edit")
        
        self.sex_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sex_edit.setGeometry(QtCore.QRect(465, 367, 65, 20))
        self.sex_edit.setFrame(False)
        self.sex_edit.setObjectName("sex_edit")
        
        self.month_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.month_edit.setGeometry(QtCore.QRect(268, 535, 151, 20))
        self.month_edit.setFrame(False)
        self.month_edit.setObjectName("month_edit")
        
        self.day_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.day_edit.setGeometry(QtCore.QRect(190, 535, 31, 20))
        self.day_edit.setFrame(False)
        self.day_edit.setObjectName("day_edit")
        
        self.or_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.or_edit.setGeometry(QtCore.QRect(170, 755, 91, 20))
        self.or_edit.setFrame(False)
        self.or_edit.setObjectName("or_edit")
        
        self.issue_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.issue_edit.setGeometry(QtCore.QRect(170, 783, 91, 20))
        self.issue_edit.setFrame(False)
        self.issue_edit.setObjectName("issue_edit")

        #BARANGAY CLEARANCE BUTTON
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(200, 935, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.print_btn.setFont(font)
        self.print_btn.setStyleSheet("background-color: qlineargradient(spread:pad,\
         x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.print_btn.setObjectName("print_btn")
        self.print_btn.clicked.connect(self.printPreviewListMethod)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_btn.setIcon(icon)


       



        MainClear.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainClear)
        QtCore.QMetaObject.connectSlotsByName(MainClear)

    def retranslateUi(self, MainClear):
        _translate = QtCore.QCoreApplication.translate
        MainClear.setWindowTitle(_translate("MainClear", "Barangay Clearance"))

        self.print_btn.setText(_translate("MainClear", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainClear = QtWidgets.QMainWindow()
    ui = Ui_MainClear()
    ui.setupUi(MainClear)
    MainClear.show()
    sys.exit(app.exec_())
