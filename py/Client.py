import sys, Ice
import Conector

with Ice.initialize(sys.argv) as communicator:
    baseC = communicator.stringToProxy("ConfirmadorPRX:default -p 10003")
    baseE = communicator.stringToProxy("EscuchadorPRX:default -p 10002")

    escuchador = Conector.EscuchadorPRX.checkedCast(baseE)
    confirmador = Conector.ConfirmadorPRX.checkedCast(baseC)

    if not escuchador:
        raise RuntimeError("Invalid proxy in Escuchador")

    if not confirmador:
        raise RuntimeError("Invalid proxy in Confirmador")
