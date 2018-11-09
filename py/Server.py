import sys, Ice
import Conector

# Actiba los actuadores necesarios para cada una de las melodias
#0. Secuencia no encontrada
#notes = deque(['G','G','G','G','G','G'], maxlen=6)
#1. Song of Time
#time = deque(['A','D4','F','A','D4','F'])
#2. Bolero fire
#fire = deque(['F','D4','F','D4','A','F'])
#3. song of Strom
#storm = deque(['D4','F','D5','D4','F','D5'])
#4. ligth song
#sun = deque(['A','F','D5','A','F','D5'])
#5. minutero del bosque.
#forest = deque(['D4','D5','B','A','B','A'])

#clase que confirma que la melodia se encuentra dentro de la matrices guardadas
class ConfirmarMelodiaI(Conector.ConfirmarMelodia):
    #matriz de nota
    notes = deque(['G','G','G','G','G','G'], maxlen=6)
    time = deque(['A','D4','F','A','D4','F'])
    fire = deque(['F','D4','F','D4','A','F'])
    storm = deque(['D4','F','D5','D4','F','D5'])
    sun = deque(['A','F','D5','A','F','D5'])
    forest = deque(['D4','D5','B','A','B','A'])
    #Espectro sonoro para cada nota
    BANDWIDTH = 25
    # frecuencias (Hz) a detectar (Use audacity to record a wave and then do Analyze->Plot Spectrum)
    D4 = 630
    E = 685
    F = 755
    G = 806
    A = 890
    B = 1000
    D5 = 1175
    #rango de frecuencia por cada nota
    #rangeD4 = range(D4-BANDWIDTH,D4+BANDWIDTH)
    #rangeE = range(E-BANDWIDTH,E+BANDWIDTH)
    #rangeF = range(F-BANDWIDTH,F+BANDWIDTH)
    #rangeG = range(G-BANDWIDTH,G+BANDWIDTH)
    #rangeA = range(A-BANDWIDTH,A+BANDWIDTH)
    #rangeB = range(B-BANDWIDTH,B+BANDWIDTH)
    #rangeD5 = range(D5-BANDWIDTH,D5+BANDWIDTH)

    #matriz de melodias

    #metodo que confirma la existencia de la secuencia en la matriz.
    def confirmarcion(self,secuencia,current=None):
        return 0


#clase que activa los actuadores luego de que se tienen las secuancias confirmadas
class ActuarI(Conector.Escuchar):
    def escucharNota(self, melodia, current=None):
        return False

with Ice.initialize(sys.argv) as communicator:
    adapterE = communicator.createObjectAdapterWithEndpoints("Escuchador", "default -p 10002")
    adapterC = communicator.createObjectAdapterWithEndpoints("Confirmador", "default -p 10003")

    objectC = ConfirmarMelodiaI()
    objectE = EscucharI()

    adapterC.add(objectC, communicator.stringToIdentity("ActuadorPRX"))
    adapterE.add(objectE, communicator.stringToIdentity("ConfirmadorPRX"))

    adapterC.activate()
    adapterE.activate()

    print "--------------------EndPoints-----------------------"
    print "AdapterC:", adapterC.getEndpoints()
    print "AdapterE:", adapterE.getEndpoints()
    print "----------------------------------------------------"
    communicator.waitForShutdown()
