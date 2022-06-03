/* Clase Ahorro
 *
 * Es el producto financiero más simple, diferenciándose de su clase padre Cuenta al ofrecer una tasa de interés que producirá 
 * ingresos en el tiempo.
 *
 */
package gestorAplicacion.productosFinancieros;

import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.Transaccion;
import gestorAplicacion.infoClientes.Usuario;
import gestorAplicacion.productosFinancieros.Cuenta;

public class Ahorro extends Cuenta implements Serializable{

	protected float tasaDeInteres;
	
    // El Array de clase de clientes de encarga de guardar todas las instancias de
    // Cliente para poder guardar y cargarlas en la serializacion
	private static ArrayList<Ahorro> ahorro = new ArrayList<>();

    //Constructor
	public Ahorro(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta,float tasaDeInteres) {
		super(nroCuenta,titular,saldo,banco,tipoDeCuenta);
		this.tasaDeInteres = tasaDeInteres;
		banco.getListaCuentas().add(this);
		titular.getCuentasAsociadas().add(this);
		
		ahorro.add(this);
	}
	
	// Verifica si el usuario cuenta con saldo para realizar la transacción. De ser así realiza los ajustes de saldo en cada cuenta,
    // crea el objeto transaccion y lo añade al historial de las cuentas involucradas.
	public boolean transferir(Cuenta cuentaDestino, float valorTransferencia) {
		if(this.saldo >= valorTransferencia) {
			this.restarSaldo(valorTransferencia);
			cuentaDestino.sumarSaldo(valorTransferencia);
			Transaccion trans = new Transaccion(this,cuentaDestino,valorTransferencia);
			historialTransferencia.add(trans);
			cuentaDestino.historialTransferencia.add(trans);
			return true;
		}
		else {
			return false;
		}
	}
	
	// Verifica si el usuario cuenta con saldo para realizar el pago de la cuota mensual. De ser así realiza los ajustes de saldo
    // en la cuenta origen y la deuda, crea el objeto transaccion y lo añade al historial de la cuenta de origen.
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

//	-------------------------------------- Metodos get-set --------------------------------------

    public static ArrayList<Ahorro> getAhorro() { return ahorro; }

    public static void setAhorro(ArrayList<Ahorro> ahorro) { Ahorro.ahorro = ahorro; }
	
	public void setTasaDeInteres(float tasaDeInteres) { this.tasaDeInteres = tasaDeInteres; }

	public float getTasaDeInteres() { return this.tasaDeInteres; }
	
	public ArrayList<Transaccion> getHistorialTransferencia(){ return this.historialTransferencia; }
	
	public void setHistorialTransferencia(ArrayList<Transaccion> historial){ this.historialTransferencia = historial; }

}
