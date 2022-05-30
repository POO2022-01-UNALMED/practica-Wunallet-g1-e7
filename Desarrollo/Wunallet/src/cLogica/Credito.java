package cLogica;
import java.util.ArrayList;

public class Credito {
	private Usuario titular;
	private Banco banco;
	private float deuda;
	private float cuotaMensual;
	
	public Credito (Usuario titular, Banco banco,float deuda,float cuotaMensual) {
		this.titular = titular;
		this.banco = banco;
		this.deuda = deuda;
		this.cuotaMensual = cuotaMensual;
	}
	
//	-------------------------------------- Métodos get-set --------------------------------------
	
	//	Get-Set usuario
	public void setTitular(Usuario titular) {
		this.titular = titular;
	}
	public Usuario getTituar() {
		return this.titular;
	}
	
	//	Get-Set banco
	public void setBanco(Banco banco) {
		this.banco = banco;
	}
	public Banco getBanco() {
		return this.banco;
	}
	
	//	Get-Set deuda
	public void setDeuda(float deuda) {
		this.deuda = deuda;
	}
	public float getDeuda() {
		return this.deuda;
	}
	
	//	Get-Set cuotaMensual
	public void setCuotaMensual(float cuotaMensual) {
		this.cuotaMensual = cuotaMensual;
	}
	public float getCuotaMensual() {
		return this.cuotaMensual;
	}
	
	
//--------------------------------------------------------------------------------------------------------
	
	public static void simularCredito(Banco banco,float monto, int plazo) {
		
	}
	
}
