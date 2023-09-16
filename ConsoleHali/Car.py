class Car:
    def __init__(self,id,plate,brand,model,year,km):
        self.id = id
        self.plate = plate
        self.brand = brand
        self.model = model
        self.year = year
        self.km = km


c1 = Car(1,"31 AB 824","Renault","Clio","2021","8763")
c2 = Car(2,"60 TK 60","Honda","CRV","2019","24634")
c3 = Car(3,"06 ATA 1938","Mercedes","E 300","2022","3546")
c4 = Car(4,"01 HA 543","Toyota","Corolla","2012","130682")
c5 = Car(5,"31 BB 473","Volkswagen","Passat","2014","165431")

cars = [c1,c2,c3,c4,c5]