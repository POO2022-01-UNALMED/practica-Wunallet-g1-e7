package cLogica;
import java.util.ArrayList;

public class Usuario {
	private ArrayList<Cuenta> listaInscritos = new ArrayList<Cuenta>();
	private float ingresosMensuales;
	private PerfilCreditico perfilCrediticio;
	private int cc;
	private Credito creditoActivo;
	private ArrayList<String> bancosAsociados = new ArrayList<String>();
	private ArrayList<Cuenta> cuentasAsociadas = new ArrayList<Cuenta>();
	
	public Usuario(PerfilCreditico perfilCrediticio,float ingresosMensuales,int cc,Credito creditoActivo) {
		this.perfilCrediticio = perfilCrediticio;
		this.ingresosMensuales = ingresosMensuales;
		this.cc = cc;
		this.creditoActivo = creditoActivo;
		
	}
	

	
//	public solicitarCredito() {}
	
//	Los parametros cc y tipoCuenta no son necesarios porque se utilizan para las verificaciones en Banquero
	public void inscribir(int cc,int numeroCuenta,String tipoCuenta, String nombreBanco) {
		Banco banco = Banco.extraerBanco(nombreBanco);
		Cuenta cuenta = banco.extraerCuenta(numeroCuenta);
		this.listaInscritos.add(cuenta);
		

	}
	
//	-------------------------------------- M�todos get-set --------------------------------------
//	Get-Set ingresosMensuales
	public void setIngresosMensuales(float ingresosMensuales) {
		this.ingresosMensuales = ingresosMensuales;
	}
	public float getIngresosMensuales() {
		return this.ingresosMensuales;
	}
	
//	Get-Set perfilCrediticio
	public void setPerfilCrediticio(PerfilCreditico perfilCrediticio) {
		this.perfilCrediticio = perfilCrediticio;
	}
	public PerfilCreditico getPerfilCrediticio() {
		return this.perfilCrediticio;
	}
	
//	Get-Set cc
	public void setCc(int cc) {
		this.cc = cc;
	}
	public int getCc() {
		return this.cc;
	}
	
//	Get-Set creditoActivo
	public void setCreditoActivo(Credito creditoActivo) {
		this.creditoActivo = creditoActivo;
	}
	public Credito getCreditoActivo() {
		return this.creditoActivo;
	}
	
//	Get listaInscritos
	public ArrayList<Cuenta> getListaIncritos(){
		return this.listaInscritos;
	}
	
//	Get cuentasAsociadas
	public ArrayList<Cuenta> getCuentasAsocidas(){
		return this.cuentasAsociadas;
	}
	
	
	public String toString() {
		StringBuffer texto = new StringBuffer(110);
		texto.append("Las cuentas inscritas del usuario "+ this.getCc() +" son: ");
		for(Cuenta i : this.getListaIncritos()) {
			texto.append(i.getNroCuenta() + " ");
		}
		return texto.toString();
	}
	
}
