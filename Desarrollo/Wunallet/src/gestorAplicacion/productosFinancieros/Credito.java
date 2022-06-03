/* Clase Credito
 *
 * Son los objetos creados cuando a un usuario se le aprueba su solicitud de crédito. Su función va desde almacenar los detalles del
 * préstamo y a qué banco pertenece, hasta ofrecer simulaciones de crédito.
 *
 */

package gestorAplicacion.productosFinancieros;

import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.infoClientes.Banco;
import gestorAplicacion.infoClientes.Usuario;

public class Credito implements Serializable {

	private Usuario titular;
	private Banco banco;
	private float deuda;
	private float cuotaMensual;
	
    // El Array de clase de clientes de encarga de guardar todas las instancias de
    // Cliente para poder guardar y cargarlas en la serializacion
	private static ArrayList<Credito> credito = new ArrayList<>();
	
    //Constructor
	public Credito (Usuario titular, Banco banco,float deuda,float cuotaMensual) {
		this.titular = titular;
		this.banco = banco;
		this.deuda = deuda;
		this.cuotaMensual = cuotaMensual;
		
		credito.add(this);
	}

    //Es un método estático que se ejecuta para verificar si, al solicitar un crédito, la cuota mensual esperada no supera la
    //capacidad de endeudamiento del usuario. El método toma la tasa de interes anual del banco, y hará el siguiente cálculo
    //
    //Deuda = (1+((tasaInteresAnual/12)*plazoEnMeses))*monto
    //
    //Es decir, el monto que pide, más el interés aplicado a ese monto multiplicado por el plazo del crédito. Una vez calculada la
    //deuda, se retorna el valor Deuda/Plazo (valor de cada cuota)
	public static float simularCredito(Banco banco,float monto, int plazo) {
		float deuda = (1+((banco.getTasaInteresAnual()/12)*plazo))*monto;
		return deuda/plazo; 	
	}

//	-------------------------------------- Métodos get-set --------------------------------------
   
	public static ArrayList<Credito> getCredito() { return credito; }

    public static void setCredito(ArrayList<Credito> credito) { Credito.credito = credito; }
    
	public void setTitular(Usuario titular) { this.titular = titular; }

	public Usuario getTituar() { return this.titular; }
	
	public void setBanco(Banco banco) {	this.banco = banco;	}

	public Banco getBanco() { return this.banco; }
	
	public void setDeuda(float deuda) {	this.deuda = deuda;	}

	public float getDeuda() { return this.deuda; }
	
	public void setCuotaMensual(float cuotaMensual) { this.cuotaMensual = cuotaMensual;	}

	public float getCuotaMensual() { return this.cuotaMensual; }
	
}
