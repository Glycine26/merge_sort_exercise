from abc import ABC,abstractmethod  #for abstract import

class car(ABC):
    
    def __init__(self, model:str, name: str, year: int):
        self.model = model
        self.name = name
        self.year = year 
        
    def start_car(self):
        msg1 = "Happy Motoring"
        return msg1
    def stop_car(self):
        msg2 = "Good bye, Have a great day!"
        return msg2
    
    @abstractmethod
    def avg_driving_speed(self):
        pass
    
    @abstractmethod
    def avg_vehicle_mileage(self):
        pass
    
class car_driver(car):
    #since the subclass uses the parent class as attribute, we cann't add extra attributes than mode, name, year.
    def __init__(self, model: str, name: str, year: int):
        super().__init__(model, name, year)
        
    def welcome_customer(self, custom_name:str):
        msg3 = f"Hello {custom_name}. We are going in {self.name}, which is a {self.model} model, built {self.year} year"
        return msg3
        
    def avg_driving_speed(self):
        msg4 = "Now avg speed is 90km/hr"
        return msg4
    
    def avg_vehicle_mileage(self):
        msg5 = "Now the vehicle mileage is 25km/l"
        return msg5
    
car_info = car_driver("SUV", "RR Discovery", "2022")
turn_on = car_info.start_car()
cust_wel = car_info.welcome_customer("Subi")
drive_info1 = car_info.avg_driving_speed()
drive_info2 = car_info.avg_vehicle_mileage()
turn_off = car_info.stop_car()

print(f"{turn_on}\n{cust_wel}\n{drive_info1}\n{drive_info2}\n{turn_off}")
