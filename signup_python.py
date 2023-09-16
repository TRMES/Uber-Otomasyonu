from PyQt5.QtWidgets import *
from signup import Ui_Dialog
from PyQt5.QtCore import pyqtSignal


class Signup(QDialog):
    signupSignal = pyqtSignal(str,str,str,str,str,str)
    def __init__(self):
        super().__init__()
        self.signupform = Ui_Dialog()
        self.signupform.setupUi(self)

      
        
        self.signupform.pushButton_signupOk.clicked.connect(self.save)


    def save(self):
        identity = self.signupform.lineEdit_identity.text()
        fname = self.signupform.lineEdit_fname.text()
        lname = self.signupform.lineEdit_lname.text()
        age = self.signupform.lineEdit_age.text()
        birthPlace = self.signupform.lineEdit_birthPlace.text()
        phoneNumber = self.signupform.lineEdit_phoneNumber.text()

        self.signupSignal.emit(identity,fname,lname,age,birthPlace,phoneNumber)
        
        print("Kayıt Başarılı.")

    
    
