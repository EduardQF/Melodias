import sys, Ice
import Conector
import grovepiActuador
import display
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
#sun = deque(['A','F','D5','A','F','D5']):wq
#5. minutero del bosque.
#forest = deque(['D4','D5','B','A','B','A'])
#-------------------------------CONFRIMADOR--------------------------------------------------------------
#clase que confirma que la melodia se encuentra dentro de la matrices guardadas
class ConfirmarMelodiaI(Conector.ConfirmarMelodia):

    def __init__(self):
        time="ADFADF"
        fire="FDFDAF"
        strom="DFDDFD"
        sun="AFDAFD"
        saria="FABFAB"
        self.melodias=[time,fire,strom,sun,saria]

    #metodo que confirma la existencia de la secuencia en la matriz.
    def confirmarcion(self,secuencia,current=None):
        print (secuencia)
        for i in range(len(self.melodias)):
            if (secuencia == self.melodias[i]):
                print "valor: " , (i+1)
                return (i + 1)
        return 0
#---------------------------------------ACTUADOR------------------------------------------------------------
#clase que activa los actuadores luego de que se tienen las secuancias confirmadas

class ActuarI(Conector.Actuador):
    def __init__(self):
        self.ga=grovepiActuador.GroveActuador()
        
    def actuart(self, melodia, current=None):
        print ("entro ", melodia)
        self.ga.PrintCancion(melodia)

#--------------------------------------SERVIDOR-------------------------------------------------------------
with Ice.initialize(sys.argv) as communicator:
    ip=display.start()
    ac = "tcp -h "+ip+" -p 10002"
    co = "tcp -h "+ip+" -p 10003"
    adapterE = communicator.createObjectAdapterWithEndpoints("Actuador", ac)
    adapterC = communicator.createObjectAdapterWithEndpoints("Confirmador", co)

    objectC = ConfirmarMelodiaI()
    objectE = ActuarI()

    adapterC.add(objectC, communicator.stringToIdentity("ConfirmadorPRX"))
    adapterE.add(objectE, communicator.stringToIdentity("ActuadorPRX"))

    adapterC.activate()
    adapterE.activate()

    print "--------------------EndPoints-----------------------"
    print "AdapterC:", adapterC.getEndpoints()
    print "AdapterE:", adapterE.getEndpoints()
    print "----------------------------------------------------"
    
    communicator.waitForShutdown()
