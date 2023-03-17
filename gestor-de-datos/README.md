# Gestor de datos
Componente responsable de ejecutar el proceso de extracción, transformación y carga de datos.

# Estructura del proyecto
``` bash 
    ├── assets                          # carpeta con datos fuente
    │  ├── source.zip                   # archivo de datos fuente
    ├── result                          # carpeta temporal de procesamiento
    ├── src                             # código fuente del sistema
    │  ├── extractors                   # extractores de datos
    │        ├── csv_extractor.py       # extractor de datos de archivos CSV
    │        ├── htm_extractor.py       # extractor de datos de archivos HTM
    │        ├── xml_extractor.py       # extractor de datos de archivos XML
    │        ├── txt_extractor.py       # extractor de datos de archivos TXT
    │  ├── helpers                      # archivos auxiliares
    │        ├── provider.py            # definición de la interacción con la base de datos
    │        ├── processor.py           # definición de procesamiento de respuestas 
    │        ├── queries.py             # definición de consultas utilizadas en la base de datos
    │  ├── readers                      # lectores de datos
    │        ├── zip_reader.py          # lector de datos de archivos ZIP
    │  ├── transformers                 # transformadores de datos
    │        ├── csv_transformer.py     # transformador de datos de archivos CSV
    │        ├── htm_transformer.py     # transformador de datos de archivos HTM
    │        ├── xml_transformer.py     # transformador de datos de archivos XML
    │        ├── txt_transformer.py     # transformador de datos de archivos TXT
    ├── .gitignore                      # exclusiones de git
    ├── README.md                       # este archivo contiene las instrucciones para deployar el sistema
    ├── loader.py                       # archivo para cargar los datos de la base
    ├── requirements.txt                # dependencias del sistema
```

## Instalación 

construye la imagen de Docker:

``` bash
docker build -t gestor-de-datos .
```

## Ejecución
Para ejecutar el componente y correr el proceso de _extracción_, _transformación_ y _carga_ de datos, utiliza el comando:

``` bash 
docker run --rm --name gestor-de-datos --link dgraph:dgraph gestor-de-datos
```

## Versión
v1.2.0 - Marzo 2023

## Autores
* Adalberto Cerrillo Vázquez.
* Brayan Saucedo Domínguez.
* Elliot Axel Noriega. 
* Héctor Abraham González Durán.
* Narda Viktoria Gómez Aguilera.