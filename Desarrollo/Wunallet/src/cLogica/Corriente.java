package cLogica;

public class Corriente extends Cuenta{
	private static final float capacidadSobregiro = 600000;
	private float sobregiroActual;
	
	public Corriente(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float sobregiroActual) {
		super(nroCuenta,titular,saldo,banco,tipoDeCuenta);
		this.sobregiroActual = sobregiroActual;
		banco.getListaCuentas().add(this);
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------
//	get-set sobregiroActual
	public void setSobregiroActual(float sobregiroActual) {
		this.sobregiroActual = sobregiroActual;
	}
	public float getSobregiroActual() {
		return this.sobregiroActual;
	}		
	
	
	
	public boolean transferir(Cuenta cuentaDestino, float valorTransferencia) {
		
		if(this.saldo+(this.capacidadSobregiro-this.sobregiroActual)>= valorTransferencia) {
			
			
			return true;
		}
		
		else {
			return false;
		}
	}
	
	

	
	public void sumarCuenta(float valorTransferencia) {
		
	}
	
	public void restarCuenta(float valorTransferencia) {
		
	}	

}
