# Cliente

Componente GUI que funciona como un cliente en este sistema proporcionando la visualización del reporte de datos y parámetros del negocio.

## Estructura del proyecto

Este repositorio contiene los siguientes directorios y archivos

```bash
├── src                             # código fuente del sistema
│  ├── controller                   # capa de lógica
│  │   ├── dashboard_controller.py  # definición de lógica del sistema
│  ├── data                         # capa de datos
│  │   ├── provider.py              # definición de API
│  │   ├── queries.py               # definición de consultas a la BD
│  │   ├── repository.py            # interfaz de comunicación con API
│  ├── view                         # capa de presentación
│  │   ├── dashboard.py             # definición de los componentes visuales
│  ├── application.py               # definición de la aplicación
├── static                          # carpeta de recursos estáticos
├── .gitignore                      # exclusiones de git
├── Dockerfile                      # definición de imagen de docker
├── main.py                         # archivo principal de ejecución
├── README.md                       # este archivo
├── requirements.txt                # dependencias del sistema
```

## Instalación

Descarga el código del repositorio utilizando el siguiente comando:

`git clone https://gitlab.com/tareas-arquitectura-de-software-curso/flujo-de-datos/cliente`

accede a la carpeta del componente

`cd cliente`

construye la imagen de Docker

```shell
docker build -t cliente .
```

## Ejecución

Para ejecutar el sistema utiliza el siguiente comando:

```shell
docker run --name cliente -p 0.0.0.0:5000:5000 --link dgraph:dgraph cliente
```

desde un navegador, accede a la url `http://localhost:5000` para visualizar el reporte del sistema

## Versión

v1.0.0 - Noviembre 2022

## Autores

- Perla Velasco
- Yonathan Martinez
- Jorge Solis

# Preguntas Frecuentes

### ¿Necesito instalar Docker?

Por supuesto, la herramienta Docker es vital para la ejecución de este sistema. Para conocer más acerca de Docker puedes visitar el siguiente [enlace](https://medium.com/@javiervivanco/que-es-docker-79d506f7b2fc).

> Para realizar la instalación de Docker en Windows puedes consultar el siguiente [enlace](https://medium.com/@tushar0618/installing-docker-desktop-on-window-10-501e594fc5eb)


> Para realizar la instalación de Docker en Linux puedes consultar el siguiente [enlace](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)