# Vuelo

## A tener en cuenta

- Pertenece al paquete: ????.
- Se relaciona con: ????.
- ???? (algo más).

## Atributos

- \- idVuelo: int
- \- origen: Final String
- \- destino: String
- \- aerolineaPadre: Aerolinea
- \- tipoClase: enum[] (**Ver comentario de la clase Aerolinea - Crear vuelo**)
- \- avion: Avion
- \- tiquetes: ArrayList (**PROPUESTA Lo habiamos planeado como un array simple, pero creo que es más conveniente usarlo como una lista para aprovechar el método size()**)
- \- aprobadoAerolinea: boolean ->
- \- aprobadoPasajeros: boolean -> (*Cuál era la diferencia entree esta y la anterior?*)

## Métodos

- \+ agregarPasajero(Tiquete tiquete):

Argumentos: El tiquete del pasajero que se agregará.

Funcionalidad: Añade el tiquete a su ArrayList de tiquetes.

Retorno: Void

- \+ quitarPasajero(Tiquete tiquete):

Argumentos: El tiquete del pasajero que se quitará.

Funcionalidad: Retira el tiquete de su ArrayList de tiquetes.

Retorno: Void
