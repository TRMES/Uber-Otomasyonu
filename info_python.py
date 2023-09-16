from PyQt5.QtWidgets import *
from info import Ui_Dialog
from signup_python import Signup



class Info(QDialog):
    
    def __init__(self):
        super().__init__()
        self.infoForm = Ui_Dialog()
        self.infoForm.setupUi(self)
        
        self.signInfo = Signup()
        self.signInfo.signupSignal.connect(self.getInfo)

    
    def getInfo(self,identity,fname,lname,age,birthPlace,phoneNumber):
        self.infoForm.label_identity.setText(identity)
        self.infoForm.label_fname.setText(fname)
        self.infoForm.label_lname.setText(lname)
        self.infoForm.label_age.setText(age)
        self.infoForm.label_birthPlace.setText(birthPlace)
        self.infoForm.label_phoneNumber.setText(phoneNumber)
        print("Veriler Yerleştirildi.")