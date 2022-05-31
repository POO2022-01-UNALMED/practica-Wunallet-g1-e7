package gestorAplicacion.productosFinancieros;
import java.util.ArrayList;

import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.Gestor; 
import gestorAplicacion.infoClientes.Transaccion;
import gestorAplicacion.infoClientes.Usuario;
import java.io.Serializable;

public abstract class Cuenta implements Gestor,Serializable{
	
	protected int nroCuenta;
	protected Usuario titular;
	protected float saldo;
	protected Banco banco;
	protected String tipoDeCuenta;
	protected ArrayList<Transaccion> historialTransferencia = new ArrayList<Transaccion>();
//	protected ArrayList<Transaccion> historialTransferencia;
	
 
	
	
	public Cuenta(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta) {
		this.nroCuenta = nroCuenta;
		this.titular = titular;
		this.saldo = saldo;
		this.banco = banco;
		this.tipoDeCuenta = tipoDeCuenta;
		
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------

	public void setNroCuenta(int nroCuenta) {
		this.nroCuenta = nroCuenta;
	}
	public int getNroCuenta() {
		return this.nroCuenta;
	}
	
	public void setTitular(Usuario titular) {
		this.titular = titular;
	}
	public Usuario getTitular() {
		return this.titular;
	}
	
	public void setSaldo(float saldo) {
		this.saldo = saldo;
	}
	public float getSaldo() {
		return this.saldo;
	}
	
	public void setBanco(Banco banco) {
		this.banco = banco;
	}
	public Banco getBanco() {
		return this.banco;
	}
	
	public void setTipoCuenta(String tipoDeCuenta) {
		this.tipoDeCuenta = tipoDeCuenta;
	}
	public String getTipoCuenta() {
		return this.tipoDeCuenta;
	}
	
	public ArrayList<Transaccion> getHistorialTransferencia(){
		return this.historialTransferencia;
	}
		
	public void setHistorialTransferencia(ArrayList<Transaccion> historial){
		this.historialTransferencia = historial;
	}
	
	//--------------------------------------------------------------------------------------

	public void verHistorial() {
		for(int i=0;i<historialTransferencia.size();i++) {
			System.out.print(historialTransferencia.get(i));
		}
	}
	
	public abstract boolean transferir(Cuenta cuentaDestino, float valorTranseferencia);
	
	public abstract boolean transferir(Credito credito);
	
	public void sumarSaldo(float valor) {
		this.setSaldo(this.getSaldo() + valor);
	}
	
//	
	
	public void  restarSaldo(float valor) {
		this.setSaldo(this.getSaldo() - valor);
	}

}
