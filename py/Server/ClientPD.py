import sys, Ice
import PetFoodSensors

def iniciar():        
    with Ice.initialize(sys.argv) as communicator:
        baseC = communicator.stringToProxy("SensorControl:tcp -h 192.168.43.152 -p 10000")

        confirmador = PetFoodSensors.SensorControlPrx.checkedCast(baseC)

        if not confirmador:
            raise RuntimeError("Invalid proxy in Confirmador")

        print("****************LISTENING*********************")
        confirmador.motorTime("5")
