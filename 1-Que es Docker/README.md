# Qué es Docker?

De manera muy resumida podríamos decir que Docker es una tecnología de contenedores que permite crear y utilizar aplicaciones de manera modular y liviana en Linux. Pero también se puede utilizar en Windows mediante Docker Desktop.

Para entender bien Docker deberáamos saber que es un container y cual son sus principales características.

Un **container** es una unidad estandarizada de software que empaqueta el código y todas sus dependencias, por lo que la aplicación puede correr de manera rápida y confiable en diferentes ambientes de computo.

Una **imagen** de un contenedor de Docker es un paquete de software ejecutable, liviano e independiente que incluye todo lo necesario para ejecutar una aplicación: código, tiempo de ejecución, herramientas del sistema, bibliotecas del sistema y configuraciones.


Las imágenes de contenedores se convierten en contenedores en tiempo de ejecución y, en el caso de los contenedores Docker, las imágenes se convierten en contenedores cuando se ejecutan en Docker Engine. 

Disponible para aplicaciones basadas en Linux y Windows, el software en contenedores siempre se ejecutará igual, independientemente de la infraestructura. Los contenedores aíslan el software de su entorno y garantizan que funcione de manera uniforme a pesar de las diferencias, por ejemplo, entre desarrollo y puesta en escena como podemos ver en la siguiente imagen.

![Container de Docker](/img/containers.png)

Los containers de Docker que corren en el Engine de Docker tienen las siguientes características:

- ) **Estándar**: Docker creó el estándar de la industria para contenedores, por lo que podrían ser portátiles en cualquier lugar.

- ) **Ligero**: los contenedores comparten el núcleo del sistema operativo de la máquina y, por lo tanto, no requieren un sistema operativo por aplicación, lo que genera una mayor eficiencia del servidor y reduce los costos de servidor y licencias.

- ) **Seguro**: las aplicaciones son más seguras en contenedores y Docker proporciona las capacidades de aislamiento predeterminadas más sólidas de la industria.

Si bien estos son conocimientos báscios para entender Docker, no esta demás profundizar y adquirir conocimientos valiosos para el área IT.

### Cual es la diferencia entre Contenedores y Máquinas virtuales?

Esta es una muy buena pregunta ya que surge si tenemos un poco de conocimiento en el área de la tecnología. Por lo que la responderemos a continuación viendo un pequeño resumen sobre ambos.

Los **contenedores** son una abstracción de la capa de aplicación que empaqueta el *código* propiamente dicho y *dependencias* juntos. 
Se pueden ejecutar varios contenedores en la misma máquina y compartir el kernel del sistema operativo con otros contenedores, cada uno de los cuales se ejecuta como procesos aislados en el espacio del usuario. Los contenedores ocupan menos espacio que las máquinas virtuales (las imágenes de los contenedores suelen tener un tamaño de decenas de MB), pueden manejar más aplicaciones y requieren menos máquinas virtuales y sistemas operativos.

Las **máquinas virtuales** (VM) son una abstracción del hardware físico que convierte un servidor en muchos servidores. El hipervisor permite ejecutar varias máquinas virtuales en una sola máquina. Cada **VM** incluye una copia completa de un sistema operativo, la aplicación, los archivos binarios y las bibliotecas necesarios, lo que ocupa decenas de GB. Las máquinas virtuales también pueden tardar en arrancar.

En definitiva como vemos a continuación de manera esquemática y podemos decir como un resumen de lo anterior.

*Los **contenedores** contiene la aplicación más todo lo necesario para que esta funcione, son livianos y utilizan los recursos del sistema operativo que tienen a diposición mientras que las **VM** son una abstracción del hardware que convierte un servidor en muchos de estos, y contiene una copia completa no solo de la aplicación sino de todo el sistema operativo y las librerias necesarias para su funcionamiento*

![comparacion](/img/cont_vs_mv.png)