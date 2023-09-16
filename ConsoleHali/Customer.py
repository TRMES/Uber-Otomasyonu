from Person import Person

class Customer(Person):
    def __init__(self,identity,fname,lname,age,birthPlace,phoneNumber):
        super().__init__(identity,fname,lname,age,birthPlace,phoneNumber)
        