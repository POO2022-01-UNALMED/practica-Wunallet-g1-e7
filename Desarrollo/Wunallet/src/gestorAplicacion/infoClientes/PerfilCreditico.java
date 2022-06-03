/* Clase PerfilCreditico
 * 
 * Cada instancia está asociada a un usuario, y describe precisamente el perfil crediticio de éste. Es usada por los bancos para 
 * determinar si una solicitud de crédito se aprueba o rechaza.
 *
 */

package gestorAplicacion.infoClientes;

import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.productosFinancieros.Corriente;

public class PerfilCreditico implements Serializable {
	private Usuario user;
	private float capacidadEndeudamiento;
	private comportamientoDePago comportamientoDePago;

	// El Array de clase de clientes de encarga de guardar todas las instancias de
	// Cliente para poder guardar y cargarlas en la serializacion
	private static ArrayList<PerfilCreditico> perfilCreditico = new ArrayList<>();

    // Constructor
	public PerfilCreditico(Usuario user, float ingresosMensuales, comportamientoDePago nivel) {
		this.user = user;
		this.capacidadEndeudamiento = (float) 0.2 * ingresosMensuales;
		this.comportamientoDePago = nivel;
		perfilCreditico.add(this);
	}

//	-------------------------------------- Metodos get-set --------------------------------------

	public static ArrayList<PerfilCreditico> getPerfilCreditico() { return perfilCreditico;	}

	public static void setPerfilCreditico(ArrayList<PerfilCreditico> perfilCreditico) {
		PerfilCreditico.perfilCreditico = perfilCreditico;
	}

	public void setNombreBanco(Usuario user) { this.user = user; }

	public Usuario getBanco() {	return this.user; }

	public void setCapacidadEndeudamiento(float nivelDeEndeudamiento) {	this.capacidadEndeudamiento = nivelDeEndeudamiento;	}

	public float getCapacidadEndeudamiento() { return this.capacidadEndeudamiento;	}

	public comportamientoDePago getComportamientoDePago() {	return this.comportamientoDePago; }

}
