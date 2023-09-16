from Customer import Customer
import Driver
import Car
import Controller
import random


def start():
    while True:
        print("__UBER OTOMASYONU__\n1-Kayıt Ol\n2-Kişisel Bilgilerim\n3-Uber Çağır\n4-Sürücü Kayıt(Bizimle Çalışmak İster Misiniz?)\n5-Çıkış")        

        try:
            process = int(input("İşlem Numarası: "))

            if process == 1:
            # identity,fname,lname,age,birthPlace,phoneNumber
                identity = input("TC Kimlik Numaranız: ")
                identity = Controller.identityController(identity)

                fname = input("Adınız: ")
                fname =Controller.fnameController(fname)

                lname = input("Soyadınız: ")
                lname = Controller.lnameController(lname)

                age = input("Yaşınız: ")
                age = Controller.ageController(age)

                birthPlace = input("Doğduğunuz Yer: ")
                birthPlace = Controller.birthPlaceController(birthPlace)

                phoneNumber = input("Telefon Numaranız(Başında '0' Olmadan): ")
                phoneNumber = Controller.phoneNumberController(phoneNumber)
                
                c1 = Customer(identity,fname,lname,age,birthPlace,phoneNumber)
                print("Kayıt Başarılı.")
            elif process == 2:
                print(f"TC Kimlik No: {c1.identity}")
                print(f"Ad: {c1.fname}")
                print(f"Soyad: {c1.lname}")
                print(f"Yaş: {c1.age}")
                print(f"Doğduğu Yer: {c1.birthPlace}")
                print(f"Telefon No: {c1.phoneNumber}")
            elif process == 3:
                # identity,fname,lname,age,birthPlace,phoneNumber, drivingLicence
                d = random.choice(Driver.drivers)
                c = random.choice(Car.cars)
                print(f"__Sürücü Bilgileri__\nAdı: {d.fname}\nSoyadı: {d.lname}\nYaş: {d.age}\nTelefon No: {d.phoneNumber}")
                print(f"__Araba__\nMarka: {c.brand}\nModel: {c.model}\nYaş: {c.year}")
                print("Uber Çağrıldı.(Yukarıdan Uberiniz Hakkında Bilgi Alabilirsiniz.)")
            elif process == 4:
                # identity,fname,lname,age,birthPlace,phoneNumber, drivingLicence
                identity = input("TC Kimlik Numaranız: ")
                identity = Controller.identityController(identity)

                fname = input("Adınız: ")
                fname =Controller.fnameController(fname)

                lname = input("Soyadınız: ")
                lname = Controller.lnameController(lname)

                age = input("Yaşınız: ")
                age = Controller.ageController(age)

                birthPlace = input("Doğduğunuz Yer: ")
                birthPlace = Controller.birthPlaceController(birthPlace)

                phoneNumber = input("Telefon Numaranız: ")
                phoneNumber = Controller.phoneNumberController(phoneNumber)

                drivingLicence = input("Ehliyet(Varsa-1, Yoksa-0):")
                drivingLicence = Controller.drivingLicenceController(drivingLicence)
        
                d1 = Driver(identity,fname,lname,age,birthPlace,phoneNumber,drivingLicence)
                
            elif process == 5:
                print("Çıkış Yapıldı.")
                break
            else:
                print("Geçersiz İşlem.")
        except ValueError:
            print("Geçersiz Değer")
        except Exception as ex:
            print("Bir Sorun Oluştu.", ex)

start()



