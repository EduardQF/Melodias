import pyaudio
import wave
import numpy as np
import struct

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 6000#48000
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"
swidth=2
window=np.blackman(CHUNK)

p= pyaudio.PyAudio()
#------------------------------------------------------

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def captador():
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
    print "the freq is :", thefreq
    return thefreq
