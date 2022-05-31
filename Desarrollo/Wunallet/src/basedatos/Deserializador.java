package basedatos;

import gestorAplicacion.productosFinancieros.*;
import gestorAplicacion.infoClientes.*;
import java.util.ArrayList;
import java.io.*;

public class Deserializador {

    /*
        Este método es el encargado de deserializar las listas que están en cada clase
    */

    public static void deserializar() {

        FileInputStream fileIn;
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\ahorro.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<Ahorro> ahorro;

            ahorro = (ArrayList<Ahorro>) in.readObject();

            Ahorro.setAhorro(ahorro);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\bajoMonto.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<BajoMonto> bajoMonto;

            bajoMonto = (ArrayList<BajoMonto>) in.readObject();

            BajoMonto.setBajoMonto(bajoMonto);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\corriente.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<Corriente> corriente;

            corriente = (ArrayList<Corriente>) in.readObject();

            Corriente.setCorriente(corriente);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\credito.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<Credito> credito;

            credito = (ArrayList<Credito>) in.readObject();

            Credito.setCredito(credito);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\banco.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<Banco> banco;

            banco = (ArrayList<Banco>) in.readObject();

            Banco.setBanco(banco);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\perfilCreditico.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<PerfilCreditico> perfilCreditico;

            perfilCreditico = (ArrayList<PerfilCreditico>) in.readObject();

            PerfilCreditico.setPerfilCreditico(perfilCreditico);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\transaccion.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<Transaccion> transaccion;

            transaccion = (ArrayList<Transaccion>) in.readObject();

            Transaccion.setTransaccion(transaccion);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            fileIn = new FileInputStream("src\\baseDatos\\temp\\usuario.txt");

            ObjectInputStream in = new ObjectInputStream(fileIn);

            ArrayList<Usuario> usuario;

            usuario = (ArrayList<Usuario>) in.readObject();

            Usuario.setUsuario(usuario);

            in.close();
            fileIn.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }


    }
}