from PyQt5.QtWidgets import *
from welcomeScreen import Ui_Dialog
from signup_python import Signup
from info_python import Info


class Menu(QDialog):
    def __init__(self):
        super().__init__()
        self.welcome = Ui_Dialog()
        self.welcome.setupUi(self)
        self.SignupOpen = Signup()
        self.infoOpen = Info()
        
        
        self.welcome.pushButton_signup.clicked.connect(self.signup)
        self.welcome.pushButton_myInfo.clicked.connect(self.myInfo)
        self.welcome.pushButton_callUber.clicked.connect(self.callUber)
        self.welcome.pushButton_drivingSignup.clicked.connect(self.drivingSignup)
        self.welcome.pushButton_exit.clicked.connect(self.exit)

        self.SignupOpen.signupSignal.connect(self.infoOpen.getInfo) 
    


    def signup(self):     
        self.SignupOpen.show()

    def myInfo(self):      
      
        self.infoOpen.show()

    def callUber(self):
        window = QWidget()
        box = "Uber çağırmak istediğinize emin misiniz?"
        result = QMessageBox.question(window,"Onay",box,QMessageBox.Yes | QMessageBox.No)
        
        if result == QMessageBox.Yes:
            QMessageBox.information(window,"Onay","Uber Çağrıldı.")
        else:
            pass
        window.show()
    
    def drivingSignup(self):
        window = QWidget()
        QMessageBox.information(window,"Bilgilendirme","Sürücü Başvuru Ekranı Bakımda.")
        window.show()
        
        

    def exit(self):
        QApplication.quit()
  
        
        
