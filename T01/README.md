# README TAREA 1 Alberto Chadwick.

  En primer lugar me gustaria partir comentando algo que probablemente se nota en el minuto de abrir la tarea, y esto 
es el largo del codigo. Lamentablemente después de tanto tiempo sin programar se va perdiendo la practica y es por eso que
como no estaba tan a ritmo, y como se dijo que no se iba a descontar por el largo del codigo, preferi copiar varias veces 
algunas cosas (tales como los with open para leer los archivos), para evitar llamar a variables que las habia redefinido
o en fin, evitar problemas.
  
  Voy a comentar primero las cosas que asumí para el desarrollo de la tarea y luego con las funcionalidades.
  Una de las cosas que asumí era que cada usuario tenia solo el dinero inicial de las orders que este tenía, y que ya
estaban inscritos en esos mercados.
  Otra cosa que asumí era que en las opciones solo iban a ingresar numeros en los inputs o letras (excepto en la fecha) 
ya que ahi se necesita corroborar el formato.
  Como se supone que los usuarios para ingresar los ask tenian el dinero para hacerlo, asumí tambien que si el balance
de los orders les daba negativo lo dejaba en 0.

  Claramente todos los que tenian orders de venta (con match) parten con 0.
  Otro punto no menor, es que el dinero que cada usuario tiene no se modifica cuando ingresa una order, sino cuando esta se 
efectua. Por lo tanto cree dos dineros en cada usuario. Un dinero y un dinero_disponible. Uno es lo que tiene para crear
orders (que claramente no incluye lo que esta en otras orders porque se supone que ese dinero ya lo "entrego"). Por si no
se entiende: si tengo 2 pesos, no puedo ingresar 10 ofertas de venta de 2 pesos ya que no tengo 20 sino que solo 2. 
Pero cuando se pregunta por el dinero total, muestro el que incluye lo que tiene ingresado en orders ya que realmente lo tiene.

  Otro punto a aclarar es que como la comision de cada mercado era un random entre 0 y 1, solo usé el numero que me entrega 
para darle al cliente, es decir no use como 1-comision la ganancia del usuario ya que sigue siendo aleatorio entonces para
evitar complicaciones use solo uno. (Otra cosa que no me quedó claro fue cuando dijeron que la comision era entre 0 y 1, 
no entendi si era entre 0 y 1 porciento (que seria bastante mas realista), pero en fin use solo entre 0 y 1 como entre 
0 y 100% de comision.. que era lo que se dio a entender en las issues).

  Ahora comentare el codigo:
  
  En primer lugar cree solo tres clases, la clase usuario, la clase mercado y la clase DCCapital (si bien pudiera haber
creado tambien la clase moneda o menú, no encontre necesario hacerlo) y cree un main con el menu entero y los import
a los archivos de las clases (La verdad es que intente crear un main con muy pocas lineas pero no sabia como crearlo
para llamar al archivo menu ya que no lo habia definido como funcion), asique tuve que hacer que el menu sea el main.

  En la clase mercado se encuentra basicamente las cosas del mercado, es decir los matches que existen en este, los 
ask y bid, y las orders.

  En la clase usuario se encuentra todas las funciones que este ejerce, tales como ver dinero, ingresar ask, ingresar a 
un mercado, etc...

  Funcionalidades y errores:
  
  De todas las opciones que se ofrecen en los distintos menu (hablare mejor del caso mas completo que es para cuando 
el tipo de usuario es trader, ya que aqui se encuentran todas las funcionalidades de los otros 2, mas algunas)

  El usuario en primer lugar queda bien registrado y guardado en los csv, puede ingresar orders con los limites respectivos
y dependiendo de si es underaged claramente. Puede ver los mercados y registrarse en ellos, lo cual implica los aumentos 
en las monedas respectivas.

  Las monedas como se requeria agregan a DCC y se crean mercados con esa moneda tambien.
  
  Lo de los tipos de usuario funciona bien, se puede cambiar a investor, un underaged no puede ingresar orders y los limites
para cada tipo estan bien restringidos.

  El usuario puede ingresar orders y se graban en los csv, eso si la verdad es que funciona muy bien pero a veces esto se 
guarda mal, no pude encontrar cuando ni porque. A veces me corria perfecto y se guardaba todo bien por mucho que editara
o me saliera del programa, y a veces se guardaba mal. No pude encontrar ese error, pero por si al correrlo aparece mal es
porque se grabo mal en el csv. (cosa que raramente pasa)...

  La opcion banco no alcance a crearla, por lo que no esta funcional. 
  
  El ver dinero disponible funciona bien.
  
  Lamentablemente tampoco esta implementado el ver orders (la verdad me hubiera costado mucho ver entre distintas fechas o 
las otras opciones que se requerian).

  Uno de mis principales errores para esta tarea fue actuar solamente con un Mercado y un Usuario al mismo tiempo, es decir,
en un principio no se me ocurrio como "poblar" la aplicacion con todos los usuarios y mercados y asi poderle editar toda la
informacion de cada uno desde el mismo programa y asi luego pasarlo a los csv. En cambio lo que hice fue cargar solamente 
el usuario que ingresaba y solo el mercado en el que se trabajaba.

  Otro problema llegado el minuto de hacer match, esto si se logra, lo que no se logra es el cambio de la fecha_match, 
o al menos no se logra reescribir en lo csv respectivos. Cuando se hacen match se me paso un print("match") que se me
olvido sacar :S .

  La funcion match esta correcta, es decir detecta todos los matches que existen en ese mercado (ya sean pasados o de ahora),
pero no se por que no se escribe la fecha de match. 

  Eso es todo, quizas a veces tire algun error inesperado que a mi se me puede estar pasando, pero ojala que no sea asi :D . 
  

