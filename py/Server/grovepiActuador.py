import grovepi
import time
import ClientPD as cpd
from grove_rgb_lcd import *

class GroveActuador:
    def __init__(self):
        self.grovepi= grovepi
        self.grovepi.pinMode(2,"OUTPUT")#relay
        self.grovepi.pinMode(3,"OUTPUT")
        self.grovepi.pinMode(4,"OUTPUT")
        self.grovepi.pinMode(5,"OUTPUT")
        self.grovepi.pinMode(6,"OUTPUT")
        self.grovepi.pinMode(7,"OUTPUT")
        setRGB(0,255,0)

    def PrintCancion(self,melodia):
        if(melodia == 0):
            setRGB(255,0,0)
            setText_norefresh("Wrong\n Bad melody!!")
              
        elif(melodia == 1):
            print ("Song of time")
                #grovepi.pinMode(3,"OUTPUT")
            t= str(time.strftime("%H:%M:%S"))
            print(t)
            setRGB(178,255,255)
            setText_norefresh("Song of Time\n"+t)
            
        elif(melodia == 2):
            print ("Bolero of fire")
            self.grovepi.analogWrite(4,255)
            
        elif(melodia == 3):
            print ("Song of storms")
            cpd.iniciar()
            
        elif(melodia == 4):                                                                                                            
            print ("Sun's song")
            setRGB(255,255,0)
            setText_norefresh("Sun's Song")
            self.grovepi.digitalWrite(2,1)
            
        elif(melodia == 5):
            print ("Saria's Song")
            self.grovepi.digitalWrite(2,0)
            self.grovepi.analogWrite(4,0)
            setRGB(255,0,0)
            setText_norefresh("Saria's Song")
            