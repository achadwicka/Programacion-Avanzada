# README T02 Alberto Chadwick A.

	En primer lugar existen 5 modulos, uno en que se guardan todas las CLASES, otra en el que se almacenan los datos, otro en donde se guardan todas las funciones, el demo editado y un main que corre el programa (o al menos a mi me funciona, le cambie al demo el name == __main__ a name == demo (porque lo llamo de otro modulo)), pero si no funciona es cosa de cambiarle a __main__ y correrlo desde demo…

	Como en el enunciado decía que al apretar retroceder se borraba
la pieza puesta en la ultima jugada, hice que si es que la ultima jugada del jugador
no era poner una pieza (sino que retroceder), este no pudiera retroceder ya que su ultima
jugada no fue poner una pieza.

	Una cosa que no estaba especificada era que si un jugador azul guardaba un estado de tablero, el rojo si podia acceder a este, por lo que en mi programa estos son de acceso libre.
	Como dice el enunciado, el juego se termina cuando no quedan piezas, por lo que si se acaban el programa cuenta los puntajes de los jugadores y se termina el juego.
	Aquí tuve un problema: ya que si bien se terminaba el juego, tenia dos opciones, que no se muestren los puntajes y se cierre la venta (así lo jugadores no pueden seguir jugando) o bien mostrar puntajes y los jugadores si pueden seguir (en teoría pueden seguir.. ya que no se cierra la ventana para que estos puedan ver sus puntajes), pero se imprime un mensaje de que el juego se terminó.

	Para el add_hint la verdad es que es muy difícil hacer uno que busque la que mas sume puntos, por lo que creé una que propusiera una jugada valida (que calcen los bordes).
	Un problema acá es que como llamo a la función revisar_bordes, esta me imprime varias veces el mensaje “posición ocupada”, la cual debería imprimir solo para el caso de agregar pieza, pero en fin funciona bien.

	Otra cosa que decidí fue que como en el enunciado salía que el juego se terminaba cuando el jugador no podia poner una pieza, esta se acaba y se cuenta el puntaje. (la otra opción ahi pudo ser apretar uno de los números y se crea otra pieza, pero elegí que se termine)

	Otra cosa que no se entendió fue que si tengo por ejemplo el 1,2,3,4,5 guardados y se aprieta el 4, si quedan el 1,2,3,4 o parte de nuevo desde el 1. Yo hice que se mantuvieran los anteriores y se pudieran elegir esos estados.

	En la tarea hay una parte en donde se crea un grafo como estructura, la cual no se por que no pude implementar bien (le dedique demasiado tiempo a tratar de que funcionara pero no hubo caso :( ). Por lo que use las listas que ya tenia creadas de antes.
