import sys, Ice
import Conector
import reconocedorFrecuencia as rec
import CaptadorFrecuencia as cf
import stack as sc

with Ice.initialize(sys.argv) as communicator:
    baseC = communicator.stringToProxy("ConfirmadorPRX:default -p 10003")
    baseE = communicator.stringToProxy("ActuadorPRX:default -p 10002")

    confirmador = Conector.ConfirmarMelodiaPrx.checkedCast(baseC)
    actuador = Conector.ActuadorPrx.checkedCast(baseE)

    if not actuador:
        raise RuntimeError("Invalid proxy in Escuchador")

    if not confirmador:
        raise RuntimeError("Invalid proxy in Confirmador")

    print("****************LISTENING*********************")
    melodi=sc.Stack()
    validate=True
    nota=""

    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while(True):
        thefreq=cf.captador()
        nota=rec.pitch(thefreq)

        if (nota == ""):
            validate=True

        if(validate and nota !=""):
            print "notas: ", (melodi.length()+1)
            melodi.add(nota)
            validate=False

        if(melodi.length() == 6):
            print("----------------------------------------------------------------")
            mel=melodi.toString()
            actuador.actuart(confirmador.confirmarcion(mel))
            print("----------------------------------------------------------------")
            melodi=sc.Stack()

    print("* done recording")
