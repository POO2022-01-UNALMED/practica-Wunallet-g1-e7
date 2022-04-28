# Aerolinea

## A tener en cuenta

- Pertenece al paquete: ????.
- Se relaciona con: ????.
- ???? (algo más).

## Atributos

- \- idAerolinea: int
- REVISAR - idVueloActual: int (**A qué hace referencia?**)
- \- nombreAerolinea: String
- \- vuelosDisponibles: Vuelo[0..\*] (ArrayList de vuelos)

## Métodos

- POR DEFINIR cuáles métodos get y set será necesario implementar. (Si es necesario implementar alguno)

- \+ venderTiquete(Pasajero pasajero):

**Argumentos**: El pasajero a quién se le venderá la aerolinea.

**Funcionamiento**: Crea un tiquete asociado al pasajero y agrega el pasajero a la lista de pasajeros del vuelo.

Este método debe acceder y suministrar toda la información necesaria para crear un Tiquete. 

En caso de que la aerolínea NO tenga vuelos disponibles se debe crear un vuelo. (NOTA: Podríamos evadir este caso haciendo qué, por ejemplo, las aerolíneas siempre tengan por defecto 3 vuelos disponibles pertenecientes a cada categoría de vuelo o si cada aerolinea sólo ofrecerá una categoría, que tenga siempre un vuelo disponible).

Una vez creado usará el método agregarPasajero(*debería cambiarse por agregarTiquete*) de la clase Vuelo para que el pasajero quede en el ArrayList de tiquetes del vuelo.

Al finalizar se debe usar otro método (**Pendiente por definir**) que nos permita preguntarle al vuelo si le cabe un pasajero más (adicional al que ya se asignó). De NO ser así, significa que el vuelo está lleno y por lo tanto será necesario crear un nuevo vuelo el cual se agregará a la lista de vuelos disponibles, reemplazando al vuelo que ya está lleno.

*PROPUESTA* Además, también ejecutará un chequeo del vuelo sobre el que se vendió el tiquete llamando al método de la misma clase aprobarVuelo. **Ojo, hay que considerar que si se implementa esto, un vuelo nunca va a llenar su capacidad porque va a estar listo para salir en cuanto llene su mínima capacidad. Es necesario pensar en como funcionará la aprobación de vuelos y qué escenarios va a permitir/prohibir**

**Retorno**: El tiquete.

- \+ cancelacionTiquete(Tiquete tiquete):

**Argumentos**: Un tiquete.

**Funcionamiento**: Desasigna al pasajero del vuelo asociado en su tiquete. 

Invocará al método quitarPasajero de la clase Vuelo.

**Retorno**: Void


- \- crearVuelo(Aerolinea aerolinea):

**Argumentos**: La aerolinea que va a crear el vuelo (entonces... Ninguno(? )

**Funcionalidad**:  Creará un vuelo asociado a la aerolinea.

El método debe proveer todos los atributos necesarios para crear un vuelo. 

Se crea una vez que se vende un primer tiquete (**Nota: Esto también se podría evitar si mantenemos siempre creado al menos un vuelo disponbile. También puede ayudar a evitar situaciones como ¿qué pasa si un vuelo tiene un solo tiquete, y el pasajero cancela el vuelo? ¿se destruye el vuelo o se deja vacio? lo más natural sería dejarlo vacío y disponible, y por eso mismo es más conveniente simplemente crear el vuelo desde antes**)

También debe asociar el vuelo creado con un avión, y llamar un método de la clase avión (**POR DEFINIR**) que asigne al avión el misom vuelo.

El vuelo es quien determina si el avión es de primera clase, económica o comercial y NO EL AVION (**esto se debería re considerar, ya que podríamos simplificar el asunto creando 3 tipos de aviones con categorías asociadas a esos aviones [primera clase, econ...], y suponer que la aerolinea tiene capacidad ilimitada de crear estos aviones a necesidad (por si se vendieran 1000 tiquetes de primera clase o algo así, simplemente suponemos que la aerolinea está en capacidad de proveer los aviones necesarios para esa demanda, y serán aviones de primera clase**)

**Retorno**: El vuelo creado.

- \- aprobarVuelo(Vuelo vuelo):

**Argumentos**: Un vuelo.

**Funcionamiento**: Revisa la capacidad del avión asociada al vuelo junto a la cantidad de tiquetes que tiene el vuelo, para determinar si cumplió con un mínimo y puede, por parte de la aerolínea, despegar.

*Adicion a considerar: Si el vuelo recibe el aprobado por parte de la aerolinea, ya debería solicitar permiso de la torre de control para despegar.*

**Retorno**: Verdadero o falso.
