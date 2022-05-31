package basedatos;

import gestorAplicacion.productosFinancieros.*;
import gestorAplicacion.infoClientes.*;

import java.io.*;

public class Serializador {

    /*
        Este método es el encargado de serializar las listar que están en cada clase
    */

    public static void serializar() {

        FileOutputStream fileOut;
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\ahorro.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);

            out.writeObject(Ahorro.getAhorro());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\bajoMonto.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);

            out.writeObject(BajoMonto.getBajoMonto());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\corriente.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);

            out.writeObject(Corriente.getCorriente());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\credito.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);

            out.writeObject(Credito.getCredito());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\banco.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);

            out.writeObject(Banco.getBanco());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\perfilCreditico.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(PerfilCreditico.getPerfilCreditico());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\transaccion.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(Transaccion.getTransaccion());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try{
            fileOut = new FileOutputStream("src\\baseDatos\\temp\\usuario.txt");

            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(Usuario.getUsuario());
            out.close();
            fileOut.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
      


    }
}