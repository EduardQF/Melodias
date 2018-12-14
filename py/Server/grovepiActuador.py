#import grovepi
#import Time

def __init__(self):
    self.grovepi.pinMode(3,"OUTPUT")
    self.grovepi.pinMode(4,"OUTPUT")
    self.grovepi.pinMode(5,"OUTPUT")
    self.grovepi.pinMode(6,"OUTPUT")
    self.grovepi.pinMode(7,"OUTPUT")

def printLed(self,a,b,c,d,e,f):
    self.grovepi.analogWrite(a,255)
    time.sleep(1)
    self.grovepi.analogWrite(a,1)
    self.grovepi.analogWrite(b,255)
    time.sleep(1)
    self.grovepi.analogWrite(b,1)
    self.grovepi.analogWrite(c,255)
    time.sleep(1)
    self.grovepi.analogWrite(c,1)
    self.grovepi.analogWrite(d,255)
    time.sleep(1)
    self.grovepi.analogWrite(d,1)
    self.grovepi.analogWrite(e,255)
    time.sleep(1)
    self.grovepi.analogWrite(e,1)
    self.grovepi.analogWrite(f,255)
    time.sleep(1)
    self.grovepi.analogWrite(f,1)

def PrintCancion(melodia):
    if(melodia == 1):
        print ("song of time")
        #printLed(4,7,5,4,7,5)
    elif(melodia == 2):
        print ("bolero of fire")
        #printLed(5,7,5,7,5,4)
    elif(melodia == 3):
        print ("song of strom")
        #printLed(7,3,5,7,3,5)
    elif(melodia == 4):
        print ("sun")
        #printLed(4,5,3,4,5,3)
    elif(melodia == 5):
        print ("the forest")
        #printLed(7,3,6,4,6,4)
