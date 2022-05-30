package gestorAplicacion.infoClientes;
import gestorAplicacion.productosFinancieros.Cuenta;

public class Transaccion {
	private Cuenta cuentaOrigen;
	private Cuenta cuentaDestino;
	private String nombreBanco;
	private float valorTransaccion;
	
	public Transaccion(Cuenta cuentaOrigen,Cuenta cuentaDestino,String nombreBanco,float valorTransaccion) {
		this.cuentaOrigen = cuentaOrigen;
		this.cuentaDestino = cuentaDestino;
		this.nombreBanco = nombreBanco;
		this.valorTransaccion = valorTransaccion;	
		
	}
	
	public Transaccion(Cuenta cuentaOrigen,String nombreBanco,float valorTransaccion) {
		this.cuentaOrigen = cuentaOrigen;
		this.nombreBanco = nombreBanco;
		this.valorTransaccion = valorTransaccion;	
		
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------

	public void setCuentaOrigen(Cuenta cuentaOrigen) {
		this.cuentaOrigen = cuentaOrigen;
	}
	public Cuenta getCuentaOrigen() {
		return this.cuentaOrigen;
	}
	
	public void setCuentaDestino(Cuenta cuentaDestino) {
		this.cuentaDestino = cuentaDestino;
	}
	public Cuenta getCuentaDestino() {
		return this.cuentaDestino;
	}
	
	public void setNombreBanco(String nombreBanco) {
		this.nombreBanco = nombreBanco;
	}
	public String getNombreBanco() {
		return this.nombreBanco;
	}
	
	public void setValorTransaccion(float valorTransaccion) {
		this.valorTransaccion = valorTransaccion;
	}
	public float getValorTransaccion() {
		return this.valorTransaccion;
	}
	
	
	//--------------------------------------------------------------------------------------

	public String toString() {
		
		if (this.cuentaDestino == null) {
			
			return "Tranferencia "+ cuentaOrigen.getTitular() + " desde la cuenta " + cuentaOrigen.getNroCuenta() + " a " + getNombreBanco() + " por valor de " + getValorTransaccion() + "." ;
		}
		
		else {
			return "Transferencia de " + cuentaOrigen.getTitular() + " desde la cuenta " + cuentaOrigen.getNroCuenta() + " a " + 
					 cuentaDestino.getTitular() + " a la cuenta " + cuentaDestino. getNroCuenta() + " por valor de " + getValorTransaccion() + ".";
		}
		
		
		
	}
	
	
}