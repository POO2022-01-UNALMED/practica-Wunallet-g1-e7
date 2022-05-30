package gestorAplicacion.infoClientes;
import java.util.ArrayList;

import gestorAplicacion.productosFinancieros.Corriente;
import gestorAplicacion.productosFinancieros.Credito;
import gestorAplicacion.productosFinancieros.Cuenta;
import java.io.Serializable;

public class Banco implements Serializable {
	private String nombreBanco;
	private final float tasaInteresAnual;
	public static ArrayList<Banco> listaBancos = new ArrayList<Banco>();
	private ArrayList<Cuenta> listaCuentas = new ArrayList<Cuenta>();
	private ArrayList<Credito> listaCreditos = new ArrayList<Credito>();
	
    // El Array de clase de clientes de encarga de guardar todas las instancias de
    // Cliente para poder guardar y cargarlas en la serializacion
	private static ArrayList<Banco> banco = new ArrayList<>();
	
	public Banco(String nombreBanco,float tasaInteresAnual) {
		this.nombreBanco = nombreBanco;
		Banco.listaBancos.add(this);
		this.tasaInteresAnual = tasaInteresAnual;
		
		banco.add(this);
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------
	
    public static ArrayList<Banco> getBanco() {
        return banco;
    }

    public static void setBanco(ArrayList<Banco> banco) {
        Banco.banco = banco;
    }
	
	
//	get-set nombreBanco
	public void setNombreBanco(String nombreBanco) {
		this.nombreBanco = nombreBanco;
	}
	
	public String getNombreBanco() {
		return this.nombreBanco;
	}
	
	public ArrayList<Cuenta> getListaCuentas(){
		return this.listaCuentas;
	}
	
	public ArrayList<Credito> getListaCreditos(){
		return this.listaCreditos;
	}
	
	
	public float getTasaInteresAnual() {
		return this.tasaInteresAnual;
	}
	
//	-------------------------------------- Metodos propuestos --------------------------------------	
	
	public static Banco extraerBanco(String nombreBanco) {
		Banco banco = null;
		for(Banco i:Banco.listaBancos) {
			if (nombreBanco == i.getNombreBanco()) {
				banco = i;
			}
		}
		return banco;
	}
	
	public Cuenta extraerCuenta(int nroCuenta) {
		Cuenta cuenta = null;
		for(Cuenta i: this.getListaCuentas()) {
			if (nroCuenta == i.getNroCuenta()) {
				cuenta = i;
				
			}
		}
		return cuenta;		
	}	
	
	public void añadirCredito(Credito credito) {
		
		listaCreditos.add(credito);
	}
	
	
}
