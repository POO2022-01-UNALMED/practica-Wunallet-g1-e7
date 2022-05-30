package cLogica;
import java.util.ArrayList;

public class PerfilCreditico {
	private Usuario user;
	private float nivelDeEndeudamiento;
	private comportamientoDePago nivel;
	
	public PerfilCreditico(Usuario user, float ingresosMensuales, comportamientoDePago nivel) {
		this.user = user;
		this.nivelDeEndeudamiento = (float)0.2*ingresosMensuales;
		this.nivel = nivel;
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
	public void setNivelDeEndeudamiento(float nivelDeEndeudamiento) {
		this.nivelDeEndeudamiento = nivelDeEndeudamiento;
	}
	public float getNivelDeEndeudamiento() {
		return this.nivelDeEndeudamiento;
	}
	
}
