package cLogica;
import java.util.ArrayList;

public abstract interface Gestor {
	public static final float sobregiroMaximo = 600000;
	
//	Modificar
	public default void eliminarCuenta() {
		
	}
	
	
	public default void sumarCuenta(float valorTransferencia) {
		this.setSaldo(this.getSaldo() + valorTransferencia);
	}
	
	public default void restarCuenta(float valorTransferencia) {
		this.setSaldo(this.getSaldo() - valorTransferencia);
	}
	
}
