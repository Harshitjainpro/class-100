class CarExpert(object):
    def __init__(self,carname,color,modal,company,speed,fueltype):
        self.carname = carname
        self.color = color
        self.modal = modal
        self.company = company
        self.speed = speed
        self.fueltype = fueltype
    
    def start(self):
        print("car is started")
    def stop(self):
        print("car has been stoped")
    def boost(self):
        print("car has been boosted")
    def changeGear(self):
        print("Gear has been changed")

car1=CarExpert("bmw","black","200202020","bmw","500","cng")
car1.start()
car1.stop()
car1.boost()
car1.changeGear()
print("car name: ",car1.carname)
print("car color: ",car1.color)
print("car modal: ",car1.modal)
print("car company: ",car1.company)
print("car speed: ",car1.speed)
print("car fueltype: ",car1.fueltype)