#parent  class with "object" in attribute.
class BaseModelcar(object):
    def __init__(self, model:str, name:str, horsepower:int):
        self.model = model
        self.name = name
        self.horsepower = horsepower
    
    def car_info(self):
        msg3 = f"About the car: This is the {self.model} model {self.name}, with {self.horsepower}HP engine power."
        return msg3
    
    def start_car(self):
        msg1 = "Happy Motoring"
        return msg1
    def stop_car(self):
        msg2 = "Good bye, Have a great day!"
        return msg2
    
print(":BaseModelCar:")
base_model_car = BaseModelcar("SUV","Mahinndra Thar",'1200')
print(base_model_car.car_info())
print(base_model_car.start_car())
print(base_model_car.stop_car())
