package gestorAplicacion.infoClientes;
import java.util.ArrayList;

public class PerfilCreditico {
	private Usuario user;
	private float capacidadEndeudamiento;
	private comportamientoDePago comportamientoDePago;
	
	public PerfilCreditico(Usuario user, float ingresosMensuales, comportamientoDePago nivel) {
		this.user = user;
		this.capacidadEndeudamiento = (float)0.2*ingresosMensuales;
		this.comportamientoDePago = nivel;
	}
	
//	-------------------------------------- Metodos get-set --------------------------------------
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
