package cLogica;
import java.util.ArrayList;

public class PerfilCreditico {
	private Usuario user;
	private float nivelDeEndeudamiento;
//	Enum
	
	public PerfilCreditico(Usuario user) {
		this.user = user;
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
		this.user = user;
	}
	public float getNivelDeEndeudamiento() {
		return this.nivelDeEndeudamiento;
	}
	
}
