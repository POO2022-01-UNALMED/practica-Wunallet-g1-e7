package basedatos;

import java.io.EOFException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.List;

import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.PerfilCreditico;
import gestorAplicacion.infoClientes.Transaccion;
import gestorAplicacion.infoClientes.Usuario;

import gestorAplicacion.productosFinancieros.Ahorro;
import gestorAplicacion.productosFinancieros.BajoMonto;
import gestorAplicacion.productosFinancieros.Corriente;
import gestorAplicacion.productosFinancieros.Credito;



/**
 * Clase para deserializar los objetos que se crearon en ejecucion
 * @author Erik Gonzalez
 * @author Felipe Miranda
 */
public class Deserializador {
	/**
	 * Utilizamos clases genericas para permitir reutilizar la funcion para todas
	 * las clases del proyecto
	 * 
	 * @param <E>       el generico se usa para poder agredar las clases que se
	 *                  crearon
	 * @param lista     Una lista de objetos
	 * @param className El nombre de la clase que queremos usar como nombre del
	 *                  archivo
	 */
	public static <E> void deserializador(List<E> list, String className) {
		FileInputStream fileIn;
		try {
			// Creamos una cadena con la ruta del archivo que vamos a cargar
			String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
//			System.out.println(path);
			// utilizamos un file para crear este archivo si no existe aun
			File archivo = new File(path);
			archivo.createNewFile(); // Crea un nuevo archivo si no existe

			// usamos un FileInputStream para poder saber de donde cargar el archivo
			fileIn = new FileInputStream(path);

			// Si el archivo esta vacio se lanza un throw EOFException y se muestra como un
			// mensaje de vacio, pero si no se usa el objeto in para leer el archivo
			ObjectInputStream in = new ObjectInputStream(fileIn);

			// Lee el listado de elementos
			ArrayList<E> listado = (ArrayList<E>) in.readObject();

			// Recorro el ArrayList
			for (E el : listado) {
				list.add(el);
			}

			in.close();
			fileIn.close();

		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("Esta vacio");
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	/**
	 * Funcion para deserializar toda la aplicacion Generic IT
	 */
	public static void deserializarTodo() {
		Deserializador.deserializador(Banco.listaBancos, "Banco");
		Deserializador.deserializador(PerfilCreditico.getPerfilCreditico(), "PerfilCreditico");
		Deserializador.deserializador(Transaccion.getTransaccion(), "Transaccion");
		Deserializador.deserializador(Usuario.getUsuario(), "Usuario");
		Deserializador.deserializador(Ahorro.getAhorro(), "Ahorro");
		Deserializador.deserializador(BajoMonto.getBajoMonto(), "BajoMonto");
		Deserializador.deserializador(Corriente.getCorriente(), "Corriente");
		Deserializador.deserializador(Credito.getCredito(), "Credito");
	}
}