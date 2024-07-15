# Instalación de Docker

Primero recordemos que Docker, como decíamos en la *Unidad 1*, esta diseñado para *Linux*. Pero es este tutorial veremos como utilizar **Docker Desktop** en **Windows**.

### Qué es WSL?
El Subsistema de Windows para Linux (WSL) es una característica de Windows que permite ejecutar un entorno Linux en la máquina Windows, sin necesidad de una máquina virtual independiente ni de arranque dual. WSL está diseñado para proporcionar una experiencia perfecta y productiva para los desarrolladores que quieren usar Windows y Linux al mismo tiempo.

Para utilizar Docker Desktop debemos instalar **WSL2** por lo que es importantes saber que es esto que debemos instalar.

### Qué es WSL2?
**WSL2** es el tipo de distribución predeterminado al instalar una distribución de Linux. **WSL2** usa tecnología de virtualización para ejecutar un kernel de Linux en una máquina virtual (VM) de utilidad ligera. Las distribuciones de Linux se ejecutan como contenedores aislados dentro de la máquina virtual administrada de WSL 2. Las distribuciones de Linux que se ejecutan desde WSL 2 compartirán el mismo espacio de nombres de red, árbol de dispositivos (distinto de /dev/pts), CPU, kernel, memoria o intercambio, /init binario, pero tienen su propio espacio de nombres PID, espacio de nombres de montaje, espacio de nombres de usuario, espacio de nombres de grupo de C y proceso init.

**WSL2** aumenta el rendimiento del sistema de archivos y agrega compatibilidad completa de llamadas del sistema en comparación con la arquitectura de **WSL1**. 