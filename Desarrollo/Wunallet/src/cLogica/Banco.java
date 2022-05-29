package cLogica;
import java.util.ArrayList;

public class Banco {
	private String nombreBanco;
	private final float tasaInteresAnual = (float) 1.82;
	public static ArrayList<Banco> listaBancos = new ArrayList<Banco>();
	private ArrayList<Cuenta> listaCuentas = new ArrayList<Cuenta>();
	private ArrayList<Credito> listaCreditos = new ArrayList<Credito>();
	
	
	public Banco(String nombreBanco) {
		this.nombreBanco = nombreBanco;
		Banco.listaBancos.add(this);
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------
	
//	get-set nombreBanco
	public void setNombreBanco(String nombreBanco) {
		this.nombreBanco = nombreBanco;
	}
	
	public String getNombreBanco() {
		return this.nombreBanco;
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
	
	
	
	
}
