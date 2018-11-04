import com.zeroc.Ice.Application;

public class Client extends Application {

    public static void main(String args[]){
        Client app= new Client();
        app.main("Client",args);
    }

    @Override
    public int run(String[] args) {
        try(com.zeroc.Ice.Communicator communicator = com.zeroc.Ice.Util.initialize(args)) {
            com.zeroc.Ice.ObjectPrx baseA = communicator.stringToProxy("ActuadorPRX -t -e 1.1:tcp -h localhost -p 10003 -t 60000:tcp -h localhost -p 9093 -t 60000");//"Actuador -t -e 1.1:tcp -h 172.23.81.25 -p 9090 -t 60000"
            com.zeroc.Ice.ObjectPrx baseE = communicator.stringToProxy("EscuchadorPRX -t -e 1.1:tcp -h localhost -p 10002 -t 60000:tcp -h localhost -p 9092 -t 60000");//"Escuchador -t -e 1.1:tcp -h 172.23.81.25 -p 9090 -t 60000"
            //ObjectPrx base = communicator.propertyToProxy("PrintAdapter.Proxy");
            Conector.ConfirmarMelodiaPrx confirmar = Conector.ConfirmarMelodiaPrx.checkedCast(baseA);
            Conector.EscucharPrx escuchar = Conector.EscucharPrx.checkedCast(baseE);


            if (confirmar == null) {
                throw new Error("Invalid proxy in Confirmador");
            }

            if (escuchar == null) {
                throw new Error("Invalid proxy in Escuchador");
            }
        }
        return 0;
    }
}
