import com.zeroc.Ice.*;

public class Server extends Application {

    public static void main(String args[]){
        Server app = new Server();
        app.main("Server",args);
    }

    @Override
    public int run(String[] args) {
        try(Communicator communicator = com.zeroc.Ice.Util.initialize(args,"Server.config"))
        {
            ObjectAdapter adapterE = communicator.createObjectAdapter("Escuchador");//
            ObjectAdapter adapterA = communicator.createObjectAdapter("Actuador");//

            com.zeroc.Ice.Object Escuchador = new EscucharI();
            com.zeroc.Ice.Object Actuador = new ConfirmarMelodiaI();

            com.zeroc.Ice.ObjectPrx proxyE= adapterE.add(Escuchador, Util.stringToIdentity("EscuchadorPRX"));
            com.zeroc.Ice.ObjectPrx proxyA= adapterA.add(Actuador, Util.stringToIdentity("ActuadorPRX"));

            System.out.println("\n+----------------------------------Server Dates------------------------------------------");
            System.out.println("|"+communicator.proxyToString(proxyE));
            System.out.println("|"+communicator.proxyToString(proxyA));

            System.out.println("+----------------------------------------------------------------------------------------");

            adapterE.activate();
            adapterA.activate();
            communicator.waitForShutdown();
        }
        return 0;
    }

}
