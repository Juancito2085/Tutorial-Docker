# Instalación de Docker

Primero recordemos que Docker, como decíamos en la *Unidad 1*, esta diseñado para *Linux*. Pero es este tutorial veremos como utilizar **Docker Desktop** en **Windows**.

### Qué es WSL?
El Subsistema de Windows para Linux (WSL) es una característica de Windows que permite ejecutar un entorno Linux en la máquina Windows, sin necesidad de una máquina virtual independiente ni de arranque dual. WSL está diseñado para proporcionar una experiencia perfecta y productiva para los desarrolladores que quieren usar Windows y Linux al mismo tiempo.

Para utilizar Docker Desktop debemos instalar **WSL2** por lo que es importantes saber que es esto que debemos instalar.

### Qué es WSL2?
**WSL2** es el tipo de distribución predeterminado al instalar una distribución de Linux. **WSL2** usa tecnología de virtualización para ejecutar un kernel de Linux en una máquina virtual (VM) de utilidad ligera. Las distribuciones de Linux se ejecutan como contenedores aislados dentro de la máquina virtual administrada de WSL 2. Las distribuciones de Linux que se ejecutan desde WSL 2 compartirán el mismo espacio de nombres de red, árbol de dispositivos (distinto de /dev/pts), CPU, kernel, memoria o intercambio, /init binario, pero tienen su propio espacio de nombres PID, espacio de nombres de montaje, espacio de nombres de usuario, espacio de nombres de grupo de C y proceso init.

**WSL2** aumenta el rendimiento del sistema de archivos y agrega compatibilidad completa de llamadas del sistema en comparación con la arquitectura de **WSL1**. 

Para instalar **WSL** podemos ir al siguiente [link](https://learn.microsoft.com/es-es/windows/wsl/install) donde se encuentran detalladas las instrucciones para la instalación.

Pero basicamente lo que debemos hacer es abrir *Windows Power Shell* e introducir el siguiente comando:

```
wsl --install
```
Si tenemos algún problema a la hora de instalar con línea anterior podemos ir al link anterior donde explica de manera detallada como instalarlo. Una vez instalado reiniciamos la PC.

Luego de reiniciar el equipo nos aparecerá que el *Windows Power Shell* que Ubuntu se ha instalado y nos pedira que elijamos un nombre de usuario y una contraseña.

### Docker Desktop

Luego procedemos a instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/), elegimos la versión para Windows y una vez que termina el proceso nos pedira reiniciar la PC nuevamente.

También debemos tener habilitado el **Hyper-V** y la virutalización. Para más detalles dejo este [video](https://www.youtube.com/watch?v=KISyPtUBqbc&list=WL&index=3&t=1s   ) con la instalación bien detallada y paso a paso.

### Verificación de la instalación

Podemos verificar la versión de Docker que tenemos intaladar con la siguiente línea de comando en Windows Power Shell.

```
docker version
```
Con lo cual podremos ver la versión como se muestra en la siguiente figura.

![docker version](/img/docker%20version.png)

Ahora para probar Docker podemos ejecutar el siguiente comando.

```
docker run hello-world
```

Con esto Docker busca la image en local llamada *hello-world*, si no la encuentra la descarga, crea un contenedor a partir de laimage y ejecuta ese contenedor.

![docker hello-world](/img/docker-hello-world.png)

Como se puede ver en la imagen anterior, aparece un mensaje explicando lo que acaba de ocrurrir, confirma que Docker este funcionando en tu sistema y además hay un mensaje de bienvenida. 