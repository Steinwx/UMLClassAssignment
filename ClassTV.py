# Paul Adrian S. Montas
# BSCOE 1-4

#Class Objects
class TV:
    
    def __init__(self) -> None:
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    def turnOn(self):
        self.on= True

    def turnOff(self):
        self.on= False

    def getChannel(self):
        return self.channel
    
    def setChannel(self,int):
        if int<= 120 and int>= 1:
            self.channel=int

    def getVolume(self):
        return self.volumeLevel

    def setVolume(self,int2):
        if int2<=7 and int2>=1:
            self.volumeLevel=int2

    def channelUp(self):
        if self.channel < 120:
            self.channel += 1
        else:
            self.channel= 1

    def channelDown(self):
        if self.channel> 1:
            self.channel-= 1
        else:
            self.channel= 120

    def volumelUp(self):
        if self.channel < 7:
            self.channel += 1
        else:
            self.channel = 1

    def volumeDown(self):
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 7
