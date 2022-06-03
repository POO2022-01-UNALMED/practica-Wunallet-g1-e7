/* Enum comportamientoDePago
 *
 * Este enum es usado como atributo en la clase PerfilCrediticio y según su nivel aprueba o rechaza uno de los filtros
 * para aprobar una solicitud de crédito
 *
 */

package gestorAplicacion.infoClientes;

import java.util.*;

public enum comportamientoDePago {
	BUENO(1),REGULAR(2),MALO(3);
	
	private int nivel;

	private comportamientoDePago(int nivel) { this.nivel=nivel;	}
	
	private static final List<comportamientoDePago> VALUES = Collections.unmodifiableList(Arrays.asList(values()));
	private static final int SIZE = VALUES.size();
	private static final Random RANDOM = new Random();

    // Método para seleccionar aleatoriamente un nivel del enum.
	public static comportamientoDePago randomNivel()  {
		return VALUES.get(RANDOM.nextInt(SIZE));
	}

	public void setNivel(int level) { this.nivel = level; }
	
	public int getNivel() { return this.nivel; }

}
