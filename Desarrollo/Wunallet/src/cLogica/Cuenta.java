package cLogica;
import java.util.ArrayList;

public abstract class Cuenta implements Gestor{
	
	protected int nroCuenta;
	protected Usuario titular;
	protected float saldo;
	protected Banco banco;
	protected String tipoDeCuenta;
	protected ArrayList<Transaccion> historialTransferencia = new ArrayList<Transaccion>();
	
	
	public Cuenta(int nroCuenta, Usuario titular,float saldo,Banco banco,String tipoDeCuenta) {
		this.nroCuenta = nroCuenta;
		this.titular = titular;
		this.saldo = saldo;
		this.banco = banco;
		this.tipoDeCuenta = tipoDeCuenta;
	}
	
}
