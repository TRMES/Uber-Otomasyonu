# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 573)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, -10, 501, 591))
        self.bgwidget.setStyleSheet("\n"
"QWidget#bgwidget{\n"
"background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))}")
        self.bgwidget.setObjectName("bgwidget")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 121, 51))
        self.label_2.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(160, 220, 71, 21))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit_fname = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit_fname.setGeometry(QtCore.QRect(160, 240, 211, 31))
        self.lineEdit_fname.setStyleSheet("border-radius:10px;\n"
"")
        self.lineEdit_fname.setText("")
        self.lineEdit_fname.setObjectName("lineEdit_fname")
        self.lineEdit_lname = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit_lname.setGeometry(QtCore.QRect(160, 310, 211, 31))
        self.lineEdit_lname.setStyleSheet("border-radius:10px;")
        self.lineEdit_lname.setText("")
        self.lineEdit_lname.setObjectName("lineEdit_lname")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 290, 71, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_age = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit_age.setGeometry(QtCore.QRect(160, 380, 211, 31))
        self.lineEdit_age.setStyleSheet("border-radius:10px;")
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 360, 71, 21))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_birthPlace = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit_birthPlace.setGeometry(QtCore.QRect(160, 450, 211, 31))
        self.lineEdit_birthPlace.setStyleSheet("border-radius:10px;")
        self.lineEdit_birthPlace.setObjectName("lineEdit_birthPlace")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 430, 71, 21))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_phoneNumber = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit_phoneNumber.setGeometry(QtCore.QRect(160, 520, 211, 31))
        self.lineEdit_phoneNumber.setStyleSheet("border-radius:10px;")
        self.lineEdit_phoneNumber.setObjectName("lineEdit_phoneNumber")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 500, 71, 21))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_identity = QtWidgets.QLineEdit(self.bgwidget)
        self.lineEdit_identity.setGeometry(QtCore.QRect(160, 170, 211, 31))
        self.lineEdit_identity.setStyleSheet("border-radius:10px;")
        self.lineEdit_identity.setObjectName("lineEdit_identity")
        self.label_7 = QtWidgets.QLabel(self.bgwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 150, 71, 21))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.bgwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 100, 61, 31))
        self.label_8.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.pushButton_signupOk = QtWidgets.QPushButton(self.bgwidget)
        self.pushButton_signupOk.setGeometry(QtCore.QRect(190, 560, 151, 21))
        self.pushButton_signupOk.setStyleSheet("border-radius: 0.5px;\n"
"background-color: rgb(255, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_signupOk.setObjectName("pushButton_signupOk")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "UBER"))
        self.label.setText(_translate("Dialog", "İsim"))
        self.label_3.setText(_translate("Dialog", "Soyisim"))
        self.label_4.setText(_translate("Dialog", "Yaş"))
        self.label_5.setText(_translate("Dialog", "Doğum Yeri"))
        self.label_6.setText(_translate("Dialog", "Telefon No"))
        self.label_7.setText(_translate("Dialog", "TC Kimlik"))
        self.label_8.setText(_translate("Dialog", "Kayıt"))
        self.pushButton_signupOk.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
