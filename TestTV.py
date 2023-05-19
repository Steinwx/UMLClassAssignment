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
class TestTV:
    def __init__(self):
        self.tv1 = TV()
        self.tv2 = TV()
        self.tv1.setChannel(30)
        self.tv1.setVolume(3)
        self.tv2.setChannel(3)
        self.tv2.setVolume(2)
        

    def display_tv_info(self):
        print("tv1's channel is", self.tv1.getChannel(), "and volume level is", self.tv1.getVolume())
        print("tv2's channel is", self.tv2.getChannel(), "and volume level is", self.tv2.getVolume())


#TestTV that will create two objects from Class TV and will produce the following output:
test_tv = TestTV()
test_tv.display_tv_info()