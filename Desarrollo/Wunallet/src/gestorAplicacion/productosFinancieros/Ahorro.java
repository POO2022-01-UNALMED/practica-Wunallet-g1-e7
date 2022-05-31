package gestorAplicacion.productosFinancieros;
import java.util.ArrayList;

import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.Transaccion;
import gestorAplicacion.infoClientes.Usuario;

import gestorAplicacion.productosFinancieros.Cuenta;
import java.io.Serializable;




public class Ahorro extends Cuenta implements Serializable{
	protected float tasaDeInteres;
	
    // El Array de clase de clientes de encarga de guardar todas las instancias de
    // Cliente para poder guardar y cargarlas en la serializacion
	private static ArrayList<Ahorro> ahorro = new ArrayList<>();
	
	
	public Ahorro(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float tasaDeInteres) {
		super(nroCuenta,titular,saldo,banco,tipoDeCuenta);
		this.tasaDeInteres = tasaDeInteres;
		banco.getListaCuentas().add(this);
		titular.getCuentasAsociadas().add(this);
		
		ahorro.add(this);
	}


//	-------------------------------------- Metodos get-set --------------------------------------
//	get-set user
    public static ArrayList<Ahorro> getAhorro() {
        return ahorro;
    }

    public static void setAhorro(ArrayList<Ahorro> ahorro) {
        Ahorro.ahorro = ahorro;
    }
	
	public void setTasaDeInteres(float tasaDeInteres) {
		this.tasaDeInteres = tasaDeInteres;
	}
	public float getTasaDeInteres() {
		return this.tasaDeInteres;
	}
	
	public ArrayList<Transaccion> getHistorialTransferencia(){
		return this.historialTransferencia;
	}
	
	public void setHistorialTransferencia(ArrayList<Transaccion> historial){
		this.historialTransferencia = historial;
	}
	
	public boolean transferir(Cuenta cuentaDestino, float valorTransferencia) {
		
		if(this.saldo >= valorTransferencia) {
			

			
			
			this.restarSaldo(valorTransferencia);

			
			
			cuentaDestino.sumarSaldo(valorTransferencia);
			
			Transaccion trans = new Transaccion(this,cuentaDestino,valorTransferencia);
			
			historialTransferencia.add(trans);
			
			return true;
		}
		
		else {
			return false;
		}
	}
	
	public boolean transferir(Credito credito) {
		
		if(this.saldo >= credito.getCuotaMensual()) {
			

			
			
			this.restarSaldo(credito.getCuotaMensual());

			
			
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
