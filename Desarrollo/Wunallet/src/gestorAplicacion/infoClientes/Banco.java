package gestorAplicacion.infoClientes;
import java.util.ArrayList;

import gestorAplicacion.productosFinancieros.Credito;
import gestorAplicacion.productosFinancieros.Cuenta;

public class Banco {
	private String nombreBanco;
	private final float tasaInteresAnual;
	public static ArrayList<Banco> listaBancos = new ArrayList<Banco>();
	private ArrayList<Cuenta> listaCuentas = new ArrayList<Cuenta>();
	private ArrayList<Credito> listaCreditos = new ArrayList<Credito>();
	
	
	public Banco(String nombreBanco,float tasaInteresAnual) {
		this.nombreBanco = nombreBanco;
		Banco.listaBancos.add(this);
		this.tasaInteresAnual = tasaInteresAnual;
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------
	
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
	
	public void a�adirCredito(Credito credito) {
		
		listaCreditos.add(credito);
	}
	
	
}