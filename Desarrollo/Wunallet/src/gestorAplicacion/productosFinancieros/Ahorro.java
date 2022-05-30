package gestorAplicacion.productosFinancieros;
import java.util.ArrayList;

import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.Transaccion;
import gestorAplicacion.infoClientes.Usuario;
import gestorAplicacion.productosFinancieros.Cuenta;

public class Ahorro extends Cuenta{
	protected float tasaDeInteres;
	
	public Ahorro(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,ArrayList<Transaccion> historial,float tasaDeInteres) {
		super(nroCuenta,titular,saldo,banco,tipoDeCuenta,historial);
		this.tasaDeInteres = tasaDeInteres;
		banco.getListaCuentas().add(this);
		titular.getCuentasAsocidas().add(this);
	}


//	-------------------------------------- Metodos get-set --------------------------------------
//	get-set user
	public void setTasaDeInteres(float tasaDeInteres) {
		this.tasaDeInteres = tasaDeInteres;
	}
	public float getTasaDeInteres() {
		return this.tasaDeInteres;
	}

	
	public boolean transferir(Cuenta cuentaDestino, float valorTransferencia) {
		
		if(this.saldo >= valorTransferencia) {
			

			
			
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
		
		if(this.saldo >= credito.getCuotaMensual()) {
			

			
			
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
