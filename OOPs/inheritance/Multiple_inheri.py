# MULTIPLE INHERITANCE:- 
'''
class C1:
    def getA(self):
        self.a = 10
class C2():
    def getB(self):
        self.b = 20
class C3(C1,C2): # Multiple class
    def getC(self):
        self.c = 30
    def operations(self):
        self.getA()
        self.getB()
        self.getC()
        self.d = self.a + self.b + self.c 
        print(self.d)
o1 = C3()
o1.operations()'''

# Design a Smartphone class that uses multiple inheritance from three functionality classes: MusicPlayer, Camera, and Phone.
'''class MusicPlayer:
    def volume(self):
        self.a = 50
    def play_song(Self):
        Self.song_title = input("Which song do you want to play:- ")
        print(f"Playing: {Self.song_title}\nVolume: {Self.a}")

class Camera:
    def resolution(Self):
        Self.a = 1080
    def take_photo(self):
        print(f"Photo Captured at Resolution {self.a}")

class Phone:
    def carrier(self):
        self.a = "GlobalNet"
    def getphone(self):
        self.number = input("Enter the NUmber:- ")
        print(f"Dialing {self.number} Via {self.a}.")

class Smartphone(MusicPlayer,Camera,Phone):
    def __init__(self):
        self.model_name = input("Enter the Model Name:- ")
        self.volume()
        self.play_song()
        self.resolution()
        self.take_photo()
        self.carrier()
        self.getphone()

s = Smartphone()
s
print("Successfully Completed...!!")
print("-"*50)'''