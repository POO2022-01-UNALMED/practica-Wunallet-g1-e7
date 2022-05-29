package cLogica;
import java.util.ArrayList;

public abstract interface Gestor {
	public static final float sobregiroMaximo = 600000;
	
//	Modificar
	public abstract void crearCuenta();
	public abstract void eliminarCuenta();
	
	public abstract void sumarCuenta(float valorTransferencia);
	public abstract void restarCuenta(float valorTransferencia);
	
}
