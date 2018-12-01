import Conector.*;
import com.zeroc.Ice.Current;

import java.util.ArrayList;

public class ConfirmarMelodiaI implements ConfirmarMelodia {

    ArrayList<String> melodias = new ArrayList();

    /*
    *Confirma la existencia de la melodia en la matriz incertada.
    *0. La secuencia no se encuentra
    *1. Song of Time
    *2. Bolero fire
    *3. song of Stroms
    *4. ligth song
    *5. minutero del bosque.
     */
    @Override
    public int confirmarcion(String secuencia, Current current) {
        System.out.println("Secuancia: "+secuencia);
        return 0;
    }

    private boolean validacion(String secuenia){
        return false;
    }

    private int comparacion(String secuencia){
        return 0;
    }
}
