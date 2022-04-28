# Pasajero

## A tener en cuenta

- Pertenece al paquete: ????.
- Se relaciona con: ????.
- ???? (algo más).

## Atributos

- \- idPasajero: int
- \- edad: int
- \- nombre: String
- \- tiquete: Tiquete

## Métodos

- POR DEFINIR cuáles métodos get y set será necesario implementar. (Si es necesario implementar alguno)

- \+ comprarTiquete(Aerolinea aerolinea):

**Argumentos**: La aerolinea que venderá el tiquete.

**Funcionamiento**: Llamará al método venderTiquete pasándole como arguento al pasajero de la aerolinea.

**Retorno**: Un tiquete asociado al pasajero.

- \+ cancelarTiquete(Tiquete tiquete):

**Argumentos**: El atributo tiquete.

**Funcionamiento**: Mediante los atributos del tiquete se ubicará la aerolinea asociada y ejecurá el método cancelaciónTiquete de dicha aerolinea (este método desasigna del array de Tiquetes que tiene la aerolinea, al tiquete del pasajero). Al finalizar se desasignará el Tiquete de la variable tiquete.

**Retorno**: Void

