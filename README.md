# Pipeline ETL sobre base de datos de grafos (Dgraph)

Sistema de **extracción, transformación y carga** que consolida datos de compras y proveedores dispersos en cuatro formatos heterogéneos (CSV, XML, HTM y TXT) dentro de una única **base de datos de grafos Dgraph**, y los expone en un dashboard analítico interactivo.

Proyecto desarrollado para el curso de **Almacenes de Datos / Gestión de Datos** de la Licenciatura en Ingeniería de Software (Universidad Autónoma de Zacatecas, marzo 2023).

---

## Por qué un grafo

Los datos fuente describen relaciones —qué proveedor surtió qué producto en qué orden— que en un modelo relacional exigirían múltiples tablas puente y *joins* costosos. Modelarlos como grafo (`Product`, `Order`, `Provider` y sus aristas) permite recorrer esas relaciones directamente y consultar con **DQL** sin reconstruirlas en cada consulta.

---

## Arquitectura

El sistema se compone de dos servicios independientes, cada uno con su propia imagen de Docker, más la base de datos:

```
   ┌──────────────┐   ZIP    ┌──────────────────┐   DQL    ┌────────────┐   DQL   ┌───────────┐
   │ Datos fuente │ ───────► │  gestor-de-datos │ ───────► │   Dgraph   │ ◄────── │  cliente  │
   │ CSV/XML/HTM/ │          │   (ETL, Luigi)   │  carga   │  (grafo)   │ consulta│ (Dash GUI)│
   │     TXT      │          └──────────────────┘          └────────────┘         └───────────┘
   └──────────────┘
```

### `gestor-de-datos` — El pipeline ETL

Implementa el proceso completo con una separación limpia por etapa:

| Capa | Módulos | Responsabilidad |
|---|---|---|
| **Readers** | `zip_reader.py` | Descomprime el archivo fuente y expone los archivos individuales |
| **Extractors** | `csv_extractor.py`, `xml_extractor.py`, `htm_extractor.py`, `txt_extractor.py` | Un extractor por formato; el de HTM usa **BeautifulSoup** para parsear tablas HTML |
| **Transformers** | `csv_transformer.py`, `xml_transformer.py`, `htm_transformer.py`, `txt_transformer.py` | Normalizan cada fuente al modelo común: limpieza, `Unidecode`, tipado y deduplicación |
| **Helpers** | `provider.py`, `processor.py`, `queries.py` | Comunicación con Dgraph, procesamiento de respuestas y definición del esquema y las mutaciones DQL |
| **Orquestación** | `loader.py` | Encadena las etapas con **Luigi**, que gestiona dependencias entre tareas y reanudación ante fallos |

El diseño es **extensible por formato**: agregar una fuente nueva significa añadir un extractor y un transformador, sin tocar el resto del pipeline.

### `cliente` — Dashboard analítico

Aplicación **Dash (Plotly)** con arquitectura en tres capas:

- **`view/dashboard.py`** — componentes visuales con Dash Bootstrap Components y gráficas de Plotly Express.
- **`controller/dashboard_controller.py`** — lógica de negocio y preparación de los datos.
- **`data/`** — `provider.py` (API), `queries.py` (consultas DQL) y `repository.py` (interfaz con la base), aislando la GUI de los detalles de Dgraph.

---

## Estructura del repositorio

```
.
├── gestor-de-datos/            # Servicio ETL
│   ├── src/
│   │   ├── readers/            #   lectura de ZIP
│   │   ├── extractors/         #   CSV, XML, HTM, TXT
│   │   ├── transformers/       #   normalización por formato
│   │   └── helpers/            #   provider, processor, queries (DQL)
│   ├── assets/source.zip       #   datos fuente
│   ├── result/                 #   salida intermedia
│   ├── loader.py               #   orquestación con Luigi
│   ├── Dockerfile
│   └── requirements.txt
├── cliente/                    # Dashboard
│   ├── src/
│   │   ├── view/               #   componentes Dash
│   │   ├── controller/         #   lógica del dashboard
│   │   └── data/               #   provider, repository, queries
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
└── README.md
```

---

## Cómo ejecutarlo

### 1. Levantar Dgraph

```bash
docker run -it -p 5080:5080 -p 6080:6080 -p 8080:8080 -p 9080:9080 \
  --name dgraph dgraph/standalone:latest
```

Esto arranca **Dgraph Zero** (balanceo de datos entre nodos del clúster) y **Dgraph Alpha** (almacenamiento, índices y predicados de consulta).

Opcionalmente, **Ratel** para inspeccionar el grafo visualmente en `http://localhost:8000`:

```bash
docker run --name ratel -d -p "8000:8000" dgraph/ratel:latest
```

### 2. Ejecutar el pipeline ETL

```bash
cd gestor-de-datos
docker build -t gestor-de-datos .
docker run --rm --name gestor-de-datos --link dgraph:dgraph gestor-de-datos
```

Al terminar, el esquema y los datos quedan cargados en Dgraph.

### 3. Levantar el dashboard

```bash
cd cliente
docker build -t cliente .
docker run --rm -p 8050:8050 --link dgraph:dgraph cliente
```

El dashboard queda disponible en `http://localhost:8050`.

---

## Stack

`Python 3` · `Dgraph` · `DQL` · `Luigi` · `BeautifulSoup4` · `Dash` · `Plotly` · `pandas` · `Docker`

---

## Autores

Proyecto desarrollado en equipo:

- **Adalberto Cerrillo Vázquez**
- **Brayan Saucedo Domínguez**
- **Elliot Axel Noriega**
- **Héctor Abraham González Durán**
- **Narda Viktoria Gómez Aguilera**

Universidad Autónoma de Zacatecas — Licenciatura en Ingeniería de Software.
