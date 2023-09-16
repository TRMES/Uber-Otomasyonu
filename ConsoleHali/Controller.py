def identityController(identity):

    while True:
        if len(identity) != 11 or identity.isdigit() == False:

            if len(identity) != 11:
                    print("Lütfen 11 Hane Giriniz.")
                
            if identity.isdigit() == False:
                    print("Lütfen Sadece Sayı Giriniz.")
            
            identity = input("TC Kimlik Numaranız: ")
        else:
            return identity
             

def fnameController(fname):

    while True:
         
         if fname.isalpha() == False :
              print("Hatalı Karakter İçermekte")
              fname = input("Adınız: ")
         else:
              return fname
         
         
def lnameController(lname):

    while True:
         
         if lname.isalpha() == False :
              print("Hatalı Karakter İçermekte")
              lname = input("Soyadınız: ")
         else:
              return lname
         

def ageController(age):
     
     while True:
          
          if age.isdigit() == False:
                print("Hatalı Karakter İçermekte")
                age = input("Yaşınız: ")
          else:
               return age
        
        
def birthPlaceController(birthPlace):
     
     while True:
          
          if birthPlace.isalpha() == False:
               print("Hatalı Karakter İçermekte")
               birthPlace = input("Doğduğunuz Yer: ")
          else:
               return birthPlace
          

def phoneNumberController(phoneNumber):
     
     while True:
          
          if phoneNumber.isdigit() == False:
                print("Hatalı Karakter İçermekte")         
          if len(phoneNumber) != 10:
                print("Lütfen 10 Hane Giriniz.")
          else: 
               return phoneNumber
          
          phoneNumber = input("Telefon Numaranız(Başında '0' Olmadan): ")


def drivingLicenceController(drivingLicence):

     while True:

          if drivingLicence == "1":
               drivingLicence = "Var"
               print("Sürücü Başvurunuz Başarılı Şekilde Gönderildi.")
               return drivingLicence 
          elif drivingLicence == "0":
               drivingLincence = "Yok"
               print("Ehliyetiniz Olmadığı İçin Başvuramazsınız.")

               return drivingLicence
          else:
               print("Geçersiz Tuşlama")