#With the same remote controling the different devices.
#Each device fresponds differently on the command.

class controller:
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class TV(controller):
    def turn_on(self):
        msg1 = "TV is connected with power, Welcome."
        return msg1
    
    def turn_off(self):
        msg2 = "Tv is turning off, Bye."
        return msg2
    
class speaker(controller):
    def turn_on(self):
        msg3 = "Speaker is connected with power, Welcome."
        return msg3
    
    def turn_off(self):
        msg4 = "Speaker is turning off, Bye."
        return msg4
    
device_TV = TV()
device_Speaker = speaker()
print("TV")
print(device_TV.turn_on())
print(device_TV.turn_off())

print("Speaker")
print(device_Speaker.turn_on())
print(device_Speaker.turn_off())