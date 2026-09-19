class Media:
    def play(self): pass
class Audio(Media):
    def play(self): print("Playing Audio")
class Video(Media):
    def play(self): print("Playing Video")
class Podcast(Media):
    def play(self): print("Playing Podcast")
for m in [Audio(), Video(), Podcast()]: m.play()
