# Torre de Control

## A tener en cuenta

- Pertenece al paquete: ????.
- Se relaciona con: ????.
- ???? (algo más).

## Atributos

- \- numeroPistas: int
- \- pistasDisponibles: int
- \- clima: enum[]

## Métodos

- \+ aprobarSalida(Avion avion): 

Argumentos: El avión que solicita la salida.

Funcionamiento: Autoriza o no el despegue de un avión según el clima.

Si el clima es soleado o lluvioso, retorna true, de lo crontrario false.

**Pregunta** Debe hacer una selección del clima?

Retorno: Verdadero o falso.

- \+ aprobarEntrada(Avion avion):

Argumentos: El avión que solicita la entrada.

Funcionamiento: Autoriza o no le aterrizaje de un avión según si hay pistas disponibles.

Si hay al menos una pista disponible permite el aterrizaje, de lo contrario lo rechaza.

**OPCIONAL** Hacer que el atributo de pistas disponibles sea un Array, y que al solicitar el permiso la torre le asgine a un atributo 'pistaLlegada' del avión, la pista que está libre.


## Problemas

- ¿Cómo asignaremos el cambio de clima? Por una parte, si hacemos que la selección se haga de forma aleatoria cada vez que se envíe una aprobación de salida, tenemos que pensar en cómo regularemos las solicitudes que haga el avión para salir una vez que esté aprobada por la aerolinea (por ejemplo, qué pasa si lo aprueba la aerolinea, pide la solicitud a la torre, y la torre se la rechaza? Debe esperar, debe re enviar la solicitud...? Qué debe hacer? 
Por otra parte, si el clima no se 'refresca' cada vez que se hace la solicitud, cómo podríamos hacer que cambie cada cierto tiempo? O qué otra situación podría desencadenar el cambio del clima?

POSIBLE SOLUCIÓN: Hacemos que si la respuesta a la solicitud es negativa, en la UI se muestre un mensaje como "Han rechazado el primer vuelo por dificultades meteorológicas, por favor espere un momento mientras mejora el clima", luego ponemos algo como el 'sleep' de python por unos 5 segundos, y después de eso se vuelva a solicitar el permiso, y se vuelva a hacer una selección aleatoria del clima... (en este caso el método de solicitar aprobación del avión deberá ser un while que mientras la torre no le de salida, muestre el mensaje anterior y espere para volver a hacer la solicitud)
