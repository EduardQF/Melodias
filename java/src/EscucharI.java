import Conector.*;
import com.zeroc.Ice.Current;

public class EscucharI implements Escuchar {

    /*
    * Actiba los actuadores necesarios para cada una de las melodias
    *0. La secuencia no se encuentra
    *1. Song of Time
    *2. Bolero fire
    *3. song of Stroms
    *4. ligth song
    *5. minutero del bosque.
     */
    @Override
    public boolean escucharNota(int melodia, Current current) {
        return false;
    }
}
