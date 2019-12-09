# README Tarea 04 

“”” El modulo a correr es simulation.py “””

	En primer lugar quiero partir comentando un grave error ya que para hacer mas corta la simulación al correr todos los escenarios, cambie la cantidad de días a 8 en vez de 80 :S y al final se me olvido devolverlo :(

	Es por esto que la verdadera simulación, en el modulo clase_simulacion.py se debe editar el while self.dias <= 8: ——> self.dias <= 80:  De verdad perdón por ese error y asumo que antes de correrlo lo pueden cambiar para que todo funcione bien :).

	Ahora hablando de los supuestos que asumí, el primero fue que si el miembro UC decide almorzar antes de que llega (miembro not in campus), este no almuerza ese día ya que se asume que almuerza en su casa.

	Los días van a tener un tiempo, el que va de 0 a 420, los cuales representan los minutos de las 8:00 a las 15:00, ya que en el resto del día no ocurren eventos.
	
	Las semanas van a tener 5 días representando los días hábiles, ya que los fines de semana no nos influye lo que pasa, así que no las tomé en cuenta.

	Los meses por lo tanto tienen 20 días, de lunes a viernes, durante 4 semanas.

	En resumen, el semestre tiene 80 días, comenzando un lunes y terminando un viernes. 

	Para la aproximación de números, cuando se necesitaban enteros (para determinar el tiempo ya que el tiempo toma puros valores enteros), utiliza round().

	Otro supuesto que asumí fue que si un vendedor llega después de las 13:00, y hay carabineros, estos no lo fiscalizan.

	También asumí que si un carabinero fiscaliza al vendedor, y lo clausura, todos los que estaban en la cola quedan sin almorzar.

	Para el cálculo de las estadísticas, en la parte que nos pedían calcular la cantidad de dinero perdido en las fiscalizaciones, utilicé el valor del producto mas caro del vendedor, y lo multipliqué por el stock que este tenía disponible, ya que no se sabe de antemano que producto compraba cada persona.

	Los únicos tiempos que no se redondean dentro de la simulacion corresponden a los de los carabineros al revisar los vendedores, ya que como era 40/n, para que queden bien distribuíos y termine a las 13:40 en punto, hice que no se redondearan.

	Lamentablemente hay un caso en particular en que las estadísticas me dan que la cantidad de personas que se enfermaron por vendedor son 0 para todos los vendedores, la verdad es que estuve mucho rato intentando buscar el error pero lamentablemente no lo encontré. Por lo que a veces tira 0, pero si se corre hartas veces, la mayoría dan bien los datos.

	Al correr todos los escenarios al mismo tiempo (para compararlos), hay que esperar hasta que se impriman los resultados ya que como no había que mostrar nada en consola no imprimí nada, pero si está corriendo.




