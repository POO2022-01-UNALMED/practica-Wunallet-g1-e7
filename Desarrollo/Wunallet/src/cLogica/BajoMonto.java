package cLogica;

public class BajoMonto extends Ahorro{
	private float limiteMensual;
	private float acumuladorTransferencia;
	
	public BajoMonto(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float tasaDeInteres,float limiteMensual,float acumuladorTransferencia) {
		super(nroCuenta,titular,saldo,banco,tipoDeCuenta,tasaDeInteres);
		this.limiteMensual = limiteMensual;
		this.acumuladorTransferencia = acumuladorTransferencia;
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------
//	get-set limiteMensual
	public void setLimiteMensual(float limiteMensual) {
		this.limiteMensual = limiteMensual;
	}
	public float getlimiteMensual() {
		return this.limiteMensual;
	}	
//	get-set acumuladorTransferencia
	public void setAcumuladorTransferencia(float acumuladorTransferencia) {
		this.acumuladorTransferencia = acumuladorTransferencia;
	}
	public float getAcumuladorTransferencia() {
		return this.acumuladorTransferencia;
	}	
	
	
	
	
	
	public void crearCuenta() {
		
	}
	
	public void eliminarCuenta() {
		
	}
	
	public void sumarCuenta(float valorTransferencia) {
		
	}
	
	public void restarCuenta(float valorTransferencia) {
		
	}
}
