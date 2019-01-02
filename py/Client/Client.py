import sys, Ice
import Conector
import reconocedorFrecuencia as rec
import CaptadorFrecuencia as cf
import stack as sc
import reproductor as rep

with Ice.initialize(sys.argv) as communicator:
    baseC = communicator.stringToProxy("ConfirmadorPRX:tcp -h 192.168.43.82 -p 10003")
    baseE = communicator.stringToProxy("ActuadorPRX:tcp -h 192.168.43.82  -p 10002")

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
            de = confirmador.confirmarcion(mel)
            if(de != 0):
                rep.reproducir()
            actuador.actuart(confirmador.confirmarcion(mel))
            print("----------------------------------------------------------------")
            melodi=sc.Stack()
    print("* done recording")
