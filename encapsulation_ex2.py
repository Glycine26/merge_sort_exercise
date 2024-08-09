# Example of a TV remote.

class TV_remote:
    def __init__(self):
        self.__initial_vol = 10 
    
    def increse_volume(self,add_volume_by):
        add_volume_by +=self.__initial_vol
        msg1 = f"You're present volume: {add_volume_by}"
        return msg1
    
    def reduce_volume(self,minus_volume_by):
        current_vol = 15
        if minus_volume_by <= self.__initial_vol:
            current_vol-=minus_volume_by
            msg2 = f"You're present reduced volume: {current_vol}"
            return msg2

remote_control = TV_remote()
give_volume = remote_control.increse_volume(6)
take_volume = remote_control.reduce_volume(3)
print(give_volume)
print(take_volume)