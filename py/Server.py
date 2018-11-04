import sys, Ice
import Conector

# Actiba los actuadores necesarios para cada una de las melodias
#0. Secuencia no encontrada
#1. Song of Time
#2. Bolero fire
#3. song of Strom
#4. ligth song
#5. minutero del bosque.

#clase que confirma que la melodia se encuentra dentro de la matrices guardadas
class ConfirmarMelodiaI(Conector.ConfirmarMelodia):

    def confirmarcion(self,secuencia,current=None):
        return 0


#clase que activa los actuadores luego de que se tienen las secuancias confirmadas
class EscucharI(Conector.Escuchar):
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
