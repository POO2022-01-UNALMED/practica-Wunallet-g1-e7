package cLogica;

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
	
	
	
	public String toString() {
		
		if (this.cuentaDestino == NULL) {
			
			return "Tranferencia "+ cuentaOrigen.getTitular() + " desde la cuenta " + cuentaOrigen.getNroCuenta() + " a " + getNombreBanco() + " por valor de " + getValorTransaccion() + "." 
		}
		
	}
	
	
}
