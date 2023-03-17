# Instrucciones generales

## Prerequisitos
Para ejecutar este componente es necesario contar con la ejecución de OrientDB, parea ello utilizamos el siguiente comando

``` bash 
docker run -it -p 5080:5080 -p 6080:6080 -p 8080:8080 -p 9080:9080 --name dgraph dgraph/standalone:latest
```

El comando anterior instanciará los componentes Dgraph Zero (componente encargado de gestionar nodos Dgraph dentro de un cluster balanceando los datos almacenados en los nodos)
 y Dgraph Alpha (componente encargado de almacenar y gestionar los datos así como los indices y los predicados de consulta).
 
 
Adicionalmente existe un componente que permite la interacción visual con Dgraph llamado Dgraph Ratel, para ello podemos utilizar el siguiente comando:

``` bash
docker run --name ratel  -d -p "8000:8000" dgraph/ratel:latest
```

Para acceder a este componente e interactuar con Dgraph nos podemos dirigir a http://localhost:8000 desde cualquier navegador.

Clonar el repositorio: 

`git clone https://github.com/AdalbertoCV/ETL-Equipo4/`

 Consultar estructura e instalación del gestor de datos en la carpeta gestor-de-datos.
 
 `cd gestor-de-datos`
 
 Consultar estructura e instalación del cliente.
 
 `cd cliente`
 
# Autores

* Adalberto Cerrillo Vázquez.
* Brayan Saucedo Domínguez.
* Elliot Axel Noriega. 
* Héctor Abraham González Durán.
* Narda Viktoria Gómez Aguilera.