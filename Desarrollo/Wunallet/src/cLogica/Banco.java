package cLogica;
import java.util.ArrayList;

public class Banco {
	private String nombreBanco;
	private final float tasaInteresAnual = (float) 1.82;
	public static ArrayList<String> listaBancos = new ArrayList<String>();
	private ArrayList<Cuenta> listaCuentas = new ArrayList<Cuenta>();
	private ArrayList<Credito> listaCreditos = new ArrayList<Credito>();
	
	
	public Banco(String nombreBanco) {
		this.nombreBanco = nombreBanco;
		Banco.listaBancos.add(nombreBanco);
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------
	
//	get-set nombreBanco
	public void setNombreBanco(String nombreBanco) {
		this.nombreBanco = nombreBanco;
	}
	public String getBanco() {
		return this.nombreBanco;
	}

	
	
	
	
//	-------------------------------------- Metodos propuestos --------------------------------------	
	
	public static String extraerBanco(String nombreBanco) {
		String nameBanco = null;
		for(String i:Banco.listaBancos) {
			if (nombreBanco == i) {
				nameBanco = i;
			}
		}
		return nameBanco;
	}
	
	
	
	
}
