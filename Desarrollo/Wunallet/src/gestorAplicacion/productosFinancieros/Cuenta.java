/* Clase Abstracta Cuenta
 *
 * Funcionalidad: Son los objetos creados cuando a un usuario se le aprueba su solicitud de crédito. Su función va desde almacenar
 * los detalles del préstamo y a qué banco pertenece, hasta ofrecer simulaciones de crédito.
 *
 */

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
	
//  Constructor
	public Cuenta(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta) {
		this.nroCuenta = nroCuenta;
		this.titular = titular;
		this.saldo = saldo;
		this.banco = banco;
		this.tipoDeCuenta = tipoDeCuenta;
	}
	
//  Al ser ejecutado desde la cuenta origen, iterará sobre la lista historialTransferencia e imprimirá cada uno de los
//  objetos ya formateados por el método toString()
	public void verHistorial() {
		for(int i=0;i<historialTransferencia.size();i++) {
			System.out.println(historialTransferencia.get(i));
		}
	}
	
//  Ejecutará las comprobaciones y actualizaciones de saldo correspondientes al realizar una transferencia. Este proceso depende del
//  tipo de cuenta que lo ejecute, y por eso debe ser un método abstracto.
	public abstract boolean transferir(Cuenta cuentaDestino, float valorTranseferencia);

//  Ejecutará las comprobaciones y actualizaciones de saldo correspondientes al realizar el pago de un crédito. Este proceso
//  depende del tipo de cuenta que lo ejecute, y por eso debe ser un método abstracto.
	public abstract boolean transferir(Credito credito);

//  Es un método implementado por requerimiento de la interfaz gestor. Sumará el saldo del parámetro a la cuenta desde la que se 
//  invoca el método.
	public void sumarSaldo(float valor) {
		this.setSaldo(this.getSaldo() + valor);
	}

//  Restará el saldo del parámetro a la cuenta desde la que se invoca el método.
	public void  restarSaldo(float valor) {
		this.setSaldo(this.getSaldo() - valor);
	}

//	-------------------------------------- Metodos get-set --------------------------------------

	public void setNroCuenta(int nroCuenta) { this.nroCuenta = nroCuenta;}

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
}

