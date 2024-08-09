#We set the time and power level for the aplliance like Microwaveoven and Washing machine.

from abc import ABC, abstractmethod

class appliance(ABC):
    def __init__(self, time:int, power:int):
        self.time = time
        self.power = power

    def start_machine(self):
        msg1 = "Set the timer and power"
        return msg1
    
    def stop_machine(self):
        msg2 = "Work done, Please remove the item"
        return msg2
    
    @abstractmethod
    def usage_rule(self):
        pass
    
    @abstractmethod
    def power_saving_rule(self):
        pass

#sub class under appliance
class microwave(appliance):
    def __init__(self, time:int, power:int):
        super().__init__(time, power)
        
    def usage_rule(self):
        msg1 = "Usage rule :\n1)Always use recommended container.\n2)Wear gloves."
        return msg1
    
    def power_saving_rule(self):
        msg2 = "Power saving rule:\n1)Turn off as soon as task completed"
        return msg2
    
    def set_inputs(self):
        timer = self.time
        inp_power = self.power
        msg3 = f"You set time {timer}sec and input power is {inp_power} watt"
        return msg3

class washingmachine(appliance):
    def __init__(self, time:int, power:int):
        super().__init__(time, power)
        
    def usage_rule(self):
        msg1 = "Usage rule :\n1)Always use recommended container.\n2)Wear gloves."
        return msg1
    
    def power_saving_rule(self):
        msg2 = "Power saving rule:\n1)Turn off as soon as task completed"
        return msg2
    
    def set_inputs(self):
        timer = self.time
        inp_power = self.power
        msg3 = f"You set time {timer}sec and input power is {inp_power} watt"
        return msg3
    

#o/p
print("Microwave")
app_microwave = microwave(20,5)
app_usage_mic = app_microwave.usage_rule()
app_rule = app_microwave.power_saving_rule()
app_op = app_microwave.set_inputs()
print(f"{app_usage_mic}\n{app_rule}\n{app_op}")
print("\n")
print("Washingmachine")
app_wash = washingmachine(65,10)
app_usage_wash = app_wash.usage_rule()
app_rule = app_wash.power_saving_rule()
app_op = app_wash.set_inputs()
print(f"{app_usage_wash}\n{app_rule}\n{app_op}")