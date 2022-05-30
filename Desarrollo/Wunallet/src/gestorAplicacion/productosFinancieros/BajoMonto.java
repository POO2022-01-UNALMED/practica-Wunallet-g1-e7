package gestorAplicacion.productosFinancieros;

import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.Transaccion;
import gestorAplicacion.infoClientes.Usuario;



public class BajoMonto extends Ahorro{
	private float limiteMensual;
	private float acumuladorTransferencia;
	
	public BajoMonto(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float tasaDeInteres,float limiteMensual,float acumuladorTransferencia) {
		super(nroCuenta,titular,saldo,banco,tipoDeCuenta,tasaDeInteres);
		this.limiteMensual = limiteMensual;
		this.acumuladorTransferencia = acumuladorTransferencia;
		banco.getListaCuentas().add(this);
		titular.getCuentasAsocidas().add(this);
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
	
	
	public boolean transferir(Cuenta cuentaDestino, float valorTransferencia) {
		
		if(this.saldo >= valorTransferencia && valorTransferencia + acumuladorTransferencia <= limiteMensual ) {
			

			
			
			this.restarCuenta(valorTransferencia);

			
			
			cuentaDestino.sumarCuenta(valorTransferencia);
			
			Transaccion trans = new Transaccion(this,cuentaDestino,cuentaDestino.banco.getNombreBanco(),valorTransferencia);
			
			historialTransferencia.add(trans);
			
			return true;
		}
		
		else {
			return false;
		}
	}
	
	public boolean transferir(Credito credito) {
		
		if(this.saldo >= credito.getCuotaMensual()&& credito.getCuotaMensual() + acumuladorTransferencia <= limiteMensual ) {
			

			
			
			this.restarCuenta(credito.getCuotaMensual());

			
			
			credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual());
			
			Transaccion trans = new Transaccion(this,credito.getBanco().getNombreBanco(),credito.getCuotaMensual());
			
			historialTransferencia.add(trans);
			
			
			return true;
			
		}
		
		else {
			return false;
		}

	}	
	

}
