class Camera:
    def take_photo(self): print("Taking photo...")
class Phone:
    def make_call(self): print("Making call...")
class Smartphone(Camera, Phone): pass
sp = Smartphone()
sp.take_photo()
sp.make_call()
