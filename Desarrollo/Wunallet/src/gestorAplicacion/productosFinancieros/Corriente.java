package gestorAplicacion.productosFinancieros;

import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.Transaccion;
import gestorAplicacion.infoClientes.Usuario;



public class Corriente extends Cuenta{
	private static final float capacidadSobregiro = 600000;
	private float sobregiroActual;
	
	public Corriente(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float sobregiroActual) {
		super(nroCuenta,titular,saldo,banco,tipoDeCuenta);
		this.sobregiroActual = sobregiroActual;
		banco.getListaCuentas().add(this);
		titular.getCuentasAsocidas().add(this);
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
			
			if(valorTransferencia>this.saldo) {
				setSaldo(0);
				setSobregiroActual(this.sobregiroActual+(valorTransferencia-this.saldo));
			}
			
			else{
				this.restarCuenta(valorTransferencia);

			}
			
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
		
		if(this.saldo+(this.capacidadSobregiro-this.sobregiroActual)>= credito.getCuotaMensual()) {
			
			if(credito.getCuotaMensual()>this.saldo) {
				setSaldo(0);
				setSobregiroActual(this.sobregiroActual+(credito.getCuotaMensual()-this.saldo));
			}
			
			else{
				this.restarCuenta(credito.getCuotaMensual());

			}
			
			credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual());
			
			Transaccion trans = new Transaccion(this,credito.getBanco().getNombreBanco(),credito.getCuotaMensual());
			
			historialTransferencia.add(trans);
			
			
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
