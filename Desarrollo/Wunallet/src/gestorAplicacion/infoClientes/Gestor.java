package gestorAplicacion.infoClientes;
import java.util.ArrayList;

public interface Gestor{
	public final float costoRomperTopes = (float)15000.0;	

	public abstract void sumarSaldo(float valorTransferencia);
	public abstract void restarSaldo(float valorTransferencia);
	
}
