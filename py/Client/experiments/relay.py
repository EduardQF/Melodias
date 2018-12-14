import time
import grovepi

relay = 2

grovepi.pinMode(relay,"OUTPUT")

grovepi.digitalWrite(relay,0)
time.sleep(3)
grovepi.digitalWrite(relay,1)
time.sleep(3)
grovepi.digitalWrite(relay,0)
time.sleep(3)
grovepi.digitalWrite(relay,1)
