class SmartDevice:
    def turn_on(self): pass
    def turn_off(self): pass
class Light(SmartDevice):
    def turn_on(self): print("Light ON")
class Fan(SmartDevice):
    def turn_on(self): print("Fan ON")
class AC(SmartDevice):
    def turn_on(self): print("AC ON")
class TV(SmartDevice):
    def turn_on(self): print("TV ON")
d = AC()
d.turn_on()
