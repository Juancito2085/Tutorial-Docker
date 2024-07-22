# Ejercicio 1
En esta sección realizaremos el primer ejercicio de este tutorial de Docker.

### Enunciado
La idea de este ejercicio es que crees un contenedor con la image de **mysql** sin un tag en particular por lo que estarás utilizando la última versión.

#### Con un script de python deberás
Conectarte al contenedor, crear una base de datos llamada Ejercicio1. Tambien crearás una tabla llamada **personas** la cual tendra solo tres columnas:

1) ID: la cual será una Primary Key de tipo entero autoincrementable
2) Nombre: que será un string.
3) Edad: que también será un entero.

Luego realizarás consulta para llenar 3 filas con los valores que deseés.

Finalmente comprobarás que los valores esten en la base de datos haciendo una consulta *SELECT * FROM personas*.

#### Si te animas
Prueba hacer lo mismo que hiciste con python pero en el bash del contenedor (en Docker Hub está el comando para acceder).
No sabes que es el bash del contenedor? 
INVESTIGÁ!!!!

### TIPS

Recuerda que hay mas de una forma de crear el contenedor.

No olvides exponer un puerto.

Acostumbrate a **leer** el la documentación de la imagen en **Docker Hub** para ver que variables de ambiente necesitas configurar para que funcione el contenedor.