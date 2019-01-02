import time,sys
import smbus
import grovepi
from grove_rgb_lcd import *
import socket
import os

def start():
    grovepi.digitalWrite(4,1)
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    setRGB(255,255,0)
    setText_norefresh("IP:"+ipaddr)
    return ipaddr
