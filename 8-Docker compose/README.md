# Docker Compose

Docker Compose es una herramienta para definir y ejecutar aplicaciones Docker de múltiples contenedores. Con Docker Compose, podemos usar un archivo YAML para configurar los servicios de una aplicación. Luego, con un solo comando, podemos crear e iniciar todos los servicios desde tu configuración.

En pocas palabras todo lo que hemos hecho en la unidad anterior lo podemos incorporar a un archivo YAML y al ejecutarlo se realizará todo el proceso de una vez.

Las características principales son:
1. Definición de servicios: Podemos definir todos los servicios que componen una aplicación en un solo archivo docker-compose.yml.
2. Redes y volúmenes: Podemos configurar redes y volúmenes compartidos entre contenedores.
3. Escalabilidad: Podemos escalar servicios hacia arriba o hacia abajo con un solo comando.

Veremos esto con el mismo ejemplo de la unidad anterior, es decir que haremos un docker compose que nos permite crear los 2 contenedores de antes pero todas las instrucciones estarán en un solo archivo.

### docker-compose.yaml