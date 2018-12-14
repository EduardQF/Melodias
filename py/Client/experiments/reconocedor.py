import pyaudio
import wave
import numpy as np
import struct

class Stack:
    def __init__(self):
        self.items =[]

    def isNull(self):
        return self.items ==[]

    def add(self,item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

    def insp(self):
        return self.items[len(self.items)-1]

    def length(self):
        return len(self.items)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 6000#48000
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"
swidth=2
window=np.blackman(CHUNK)

#--------------------------------------------------------
BANDWIDTH = 25
#A
A= 825#830
#B
B=910
#DM
CM=955
#C
C=515
#D
D=555#563
#E
E=622#627
#F
F= 665#665
#G
G=750#750

p= pyaudio.PyAudio()
#------------------------------------------------------

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("****************LISTENING*********************")
melodi=Stack()
validate=True
nota="C"

#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
while(True):
    data = stream.read(CHUNK)
    #frames.append(data)
    #------------------------------------------------
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                         data))*window
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2

    which = fftData[1:].argmax() + 1

    y0,y1,y2 = np.log(fftData[which-1:which+2:])
    x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
    # find the frequency and output it
    thefreq = (which+x1)*RATE/CHUNK
    #print "The freq is %f Hz." % (thefreq)#re,do,mi,fa,sol,la,
    if(thefreq> C - BANDWIDTH and thefreq < C + BANDWIDTH ):
        nota="C"
        print("C")
    elif (thefreq> D - BANDWIDTH and thefreq < D + BANDWIDTH):
        nota="D"
        print("D")
    elif (thefreq> E - BANDWIDTH and thefreq < E + BANDWIDTH):
        nota="E"
        print("E")
    elif (thefreq> F - BANDWIDTH and thefreq < F + BANDWIDTH):
        nota="F"
        print("F")
    elif (thefreq> G - BANDWIDTH and thefreq < G + BANDWIDTH):
        nota="G"
        print("G")
    elif (thefreq> A - BANDWIDTH and thefreq < A + BANDWIDTH):
        nota="A"
        print("A")
    elif (thefreq> B - BANDWIDTH and thefreq < B + BANDWIDTH):
        nota="B"
        print("B")
    elif (thefreq> CM - BANDWIDTH and thefreq < CM + BANDWIDTH):
        nota="CM"
        print("CM")
    else:
        nota = ""
        validate=True
        print("not note")

    if(validate and nota !=""):
        print("*********************--------------------****************", melodi.length())
        melodi.add(nota)
        validate=False

    if(melodi.length() == 6):
        print("----------------------------------------------------------------")
        for i in range(6):
            print(melodi.get())
        print("----------------------------------------------------------------")
        melodi=Stack()

print("* done recording")
