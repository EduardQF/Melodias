import alsaaudio, time, audioop

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
inp.setchannels(1)
inp.setrate(48000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

print ("---------------------start-----------------------")
time.sleep(0.5)
print ("----------------you blow-------------------------")
time.sleep(0.5)
cont=0
while cont<1000:
    # Read data from device
    l,data = inp.read()
    if l:
        # Return the maximum of the absolute value of all samples in a fragment.
        #if (audioop.max(data, 2)<7000 and audioop.max(data, 2)>6000):
        #    print("DO")
        #elif(audioop.max(data, 2)<5600 and audioop.max(data, 2)>4300):
        #    print("re")
        #else:
        print audioop.max(data, 2)
    time.sleep(.001)
    cont=cont

print ("finish")
