/* Interface Gestor
 *
 * Esta interface le exige a las clases que la implementan que declaren métodos de gestión de dichos productos financieros.
 * Adicionalmente almacena constantes relevantes para la gestión de dichos productos.
 *
 */

package gestorAplicacion.infoClientes;

import java.util.ArrayList;

public interface Gestor{

	public final float costoRomperTopes = (float)15000.0;	

    // Metodo para sumar saldo del producto bancario en que se implementa.
	public abstract void sumarSaldo(float valorTransferencia);

    //Metodo para restar saldo del producto bancario en que se implementa.
	public abstract void restarSaldo(float valorTransferencia);
	
}
