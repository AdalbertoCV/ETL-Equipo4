# Gestor de datos

Componente responsable de ejecutar el proceso de *extracción*, *transformación* y *carga* de datos

## Estructura del proyecto

```bash
    ├── assets                          # carpeta con datos fuente
    │  ├── source.zip                   # archivo de datos fuente
    ├── result                          # carpeta temporal de procesamiento
    ├── src                             # código fuente del sistema
    │  ├── extractors                   # extractores de datos
    │        ├── csv_extractor.py       # extractor de datos de archivos CSV
    │        ├── htm_extractor.py       # extractor de datos de archivos HTM
    │        ├── xml_extractor.py       # extractor de datos de archivos XML
    │  ├── helpers                      # archivos auxiliares
    │        ├── provider.py            # definición de la interacción con la base de datos
    │        ├── processor.py           # definición de procesamiento de respuestas 
    │        ├── queries.py             # definición de consultas utilizadas en la base de datos
    │  ├── readers                      # lectores de datos
    │        ├── zip_extractor.py       # lector de datos de archivos ZIP
    │  ├── transformers                 # transformadores de datos
    │        ├── csv_transformer.py     # transformador de datos de archivos CSV
    │        ├── htm_transformer.py     # transformador de datos de archivos HTM
    │        ├── xml_transformer.py     # transformador de datos de archivos XML
    ├── .gitignore                      # exclusiones de git
    ├── README.md                       # este archivo
    ├── requirements.txt                # dependencias del sistema
```

## Prerequisitos

Para ejecutar este componente es necesario contar con la ejecución de OrientDB, parea ello utilizamos el siguiente comando:

```shell
docker run -d -p 5080:5080 -p 6080:6080 -p 8080:8080 -p 9080:9080 -p 8000:8000 --name dgraph dgraph/standalone
```

## Instalación

Descarga el código del repositorio utilizando el siguiente comando:

`git clone https://gitlab.com/tareas-arquitectura-de-software-curso/flujo-de-datos/gestor-de-datos.git`

accede a la carpeta del componente:

`cd gestor-de-datos`

construye la imagen de Docker

```shell
docker build -t gestor-de-datos .
```

## Ejecución

Para ejecutar el componente y correr el proceso de *extracción*, *transformación* y *carga* de datos, utiliza el comando:

```shell
docker run --rm --name gestor-de-datos --link dgraph:dgraph gestor-de-datos
```

## Versión

v1.1.0 - Noviembre 2022

## Autores

- Perla Velasco
- Yonathan Martinez
- Jorge Solis

# Preguntas Frecuentes

### ¿Necesito instalar Docker?

Por supuesto, la herramienta Docker es vital para la ejecución de este sistema. Para conocer más acerca de Docker puedes visitar el siguiente [enlace](https://medium.com/@javiervivanco/que-es-docker-79d506f7b2fc).

> Para realizar la instalación de Docker en Windows puedes consultar el siguiente [enlace](https://medium.com/@tushar0618/installing-docker-desktop-on-window-10-501e594fc5eb)


> Para realizar la instalación de Docker en Linux puedes consultar el siguiente [enlace](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)