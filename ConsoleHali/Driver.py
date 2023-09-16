from Person import Person
from Car import Car 
import random

class Driver(Person):
    def __init__(self,identity,fname,lname,age,birthPlace,phoneNumber, drivingLicence):
        super().__init__(identity,fname,lname,age,birthPlace,phoneNumber)
        
        self.drivingLicence = drivingLicence
        
    

d1 = Driver("11111111111","Selin","Gül","26","İstanbul","+90 599 999 99 99",True)
d2 = Driver("22222222222","Mahmut","Demir","38","Antalya","+90 588 888 88 88",True)
d3 = Driver("33333333333","Hakan","Sarıoğlu","27","Samsun","+90 577 777 77 77",True)
d4 = Driver("44444444444","Ceren","Koyun","31","Erzumun","+90 566 666 66 66",True)
d5 = Driver("55555555555","Sami","Akıncı","24","Tokat","+90 555 555 55 55",True)

drivers = [d1,d2,d3,d4,d5]

