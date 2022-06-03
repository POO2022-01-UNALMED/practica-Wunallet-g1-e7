/* Clase Banco
 *
 * Cada instancia de esta clase representa uno de los bancos integrados al software, y en sus atributos almacenan toda la
 * información sobre sus productos e identidad.
 *
 */

package gestorAplicacion.infoClientes;

import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.productosFinancieros.Corriente;
import gestorAplicacion.productosFinancieros.Credito;
import gestorAplicacion.productosFinancieros.Cuenta;

public class Banco implements Serializable {
	private String nombreBanco;
	private final float tasaInteresAnual;
	public static ArrayList<Banco> listaBancos = new ArrayList<Banco>();
	private ArrayList<Cuenta> listaCuentas = new ArrayList<Cuenta>();
	private ArrayList<Credito> listaCreditos = new ArrayList<Credito>();
	
    // El Array de clase de clientes de encarga de guardar todas las instancias de
    // Cliente para poder guardar y cargarlas en la serializacion
	private static ArrayList<Banco> banco = new ArrayList<>();
	
    // Constructor
	public Banco(String nombreBanco,float tasaInteresAnual) {
		this.nombreBanco = nombreBanco;
		Banco.listaBancos.add(this);
		this.tasaInteresAnual = tasaInteresAnual;
		
		banco.add(this);
	}
	
    
    //Recorre iterativamente la listaBancos de la clase Banco, buscando un banco cuyo nombre coincida con el parámetro ingresado. De
    //existir retornará el objeto.
	public static Banco extraerBanco(String nombreBanco) {
		Banco banco = null;
		for(Banco i:Banco.listaBancos) {
			if (nombreBanco.equals(i.getNombreBanco())) {
				banco = i;
			}
		}
		return banco;
	}
	
    //Recorre iterativamente la listaDeCuentas del banco desde donde se invoca el método, buscando una cuenta que tenga el numero
    //de cuenta ingresado. 
	public Cuenta extraerCuenta(int nroCuenta) {
		Cuenta cuenta = null;
		for(Cuenta i: this.getListaCuentas()) {
			if (nroCuenta == i.getNroCuenta()) {
				cuenta = i;
			}
		}
		return cuenta;		
	}	
	
    // Añade un crédito a la listaCreditos del banco.
	public void añadirCredito(Credito credito) {
		listaCreditos.add(credito);
	}

    // Remueve la cuenta del parámetro de la listaCuentas del banco.
	public void removerCuenta(Cuenta cuenta) {
		this.getListaCuentas().remove(cuenta);
	}

//	-------------------------------------- Metodos get-set --------------------------------------
    public static ArrayList<Banco> getBanco() { return banco; }

    public static void setBanco(ArrayList<Banco> banco) { Banco.banco = banco; }
	
	public void setNombreBanco(String nombreBanco) { this.nombreBanco = nombreBanco; }
	
	public String getNombreBanco() { return this.nombreBanco; }
	
	public ArrayList<Cuenta> getListaCuentas(){	return this.listaCuentas; }
	
	public ArrayList<Credito> getListaCreditos(){ return this.listaCreditos; }
	
	public float getTasaInteresAnual() { return this.tasaInteresAnual; }
}

