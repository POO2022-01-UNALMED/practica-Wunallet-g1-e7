package gestorAplicacion.infoClientes;
import java.util.ArrayList;

import gestorAplicacion.infoClientes.PerfilCreditico;
import gestorAplicacion.productosFinancieros.Credito;
import gestorAplicacion.productosFinancieros.Cuenta;


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
	
	
//	Los parametros cc y tipoCuenta no son necesarios porque se utilizan para las verificaciones en Banquero
	public void inscribir(int numeroCuenta, String nombreBanco) {
		Banco banco = Banco.extraerBanco(nombreBanco);
		Cuenta cuenta = banco.extraerCuenta(numeroCuenta);
		this.listaInscritos.add(cuenta);
		

	}
	
//	-------------------------------------- Métodos get-set --------------------------------------
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
	
//	-------------------------------------- Métodos creados --------------------------------------
	public int solicitarCredito(Banco banco, float monto, int plazo,Cuenta cuentaSc) {
		int salida=0;
		if(this.getPerfilCrediticio()==null) {
			PerfilCreditico perfil = new PerfilCreditico(this,this.getIngresosMensuales(),comportamientoDePago.randomNivel());
			this.setPerfilCrediticio(perfil);
		}
		
		if(this.getPerfilCrediticio().getComportamientoDePago().getNivel()==3) {
			salida=1;
		}else {
			float cuotaTentativa = Credito.simularCredito(banco, monto, plazo);
			
			if(cuotaTentativa>this.getPerfilCrediticio().getCapacidadEndeudamiento()) {
				salida=2;
			}else {
				Credito credito = new Credito(this,banco,monto,cuotaTentativa);
				this.setCreditoActivo(credito);
				cuentaSc.setSaldo(cuentaSc.getSaldo() + monto);
				banco.añadirCredito(credito);
				
				salida=3;
				}
		}
		
		return salida;
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
