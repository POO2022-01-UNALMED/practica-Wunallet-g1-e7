package gestorAplicacion.infoClientes;
import java.util.ArrayList;

import gestorAplicacion.productosFinancieros.Corriente;

import java.io.Serializable;

public class PerfilCreditico implements Serializable{
	private Usuario user;
	private float capacidadEndeudamiento;
	private comportamientoDePago comportamientoDePago;
	
    // El Array de clase de clientes de encarga de guardar todas las instancias de
    // Cliente para poder guardar y cargarlas en la serializacion
	private static ArrayList<PerfilCreditico> perfilCreditico = new ArrayList<>();
	
	public PerfilCreditico(Usuario user, float ingresosMensuales, comportamientoDePago nivel) {
		this.user = user;
		this.capacidadEndeudamiento = (float)0.2*ingresosMensuales;
		this.comportamientoDePago = nivel;
		
		perfilCreditico.add(this);
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------

    public static ArrayList<PerfilCreditico> getPerfilCreditico() {
        return perfilCreditico;
    }

    public static void setCorriente(ArrayList<PerfilCreditico> perfilCreditico) {
    	PerfilCreditico.perfilCreditico = perfilCreditico;
    }
	
	//	get-set user
	public void setNombreBanco(Usuario user) {
		this.user = user;
	}
	public Usuario getBanco() {
		return this.user;
	}

//	get-set nivelDeEndeudamiento
	public void setCapacidadEndeudamiento(float nivelDeEndeudamiento) {
		this.capacidadEndeudamiento = nivelDeEndeudamiento;
	}
	public float getCapacidadEndeudamiento() {
		return this.capacidadEndeudamiento;
	}
//	get-set nivel
	public comportamientoDePago getComportamientoDePago() {
		return this.comportamientoDePago;
	}
	
	
}
