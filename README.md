# Comparación y Análisis de Precios de Supermercados en España 🛒

## Descripción del Proyecto

Este proyecto busca analizar la variabilidad y evolución de precios de productos básicos en seis grandes supermercados de España (Alcampo, Carrefour, Dia, Eroski, Hipercor y Mercadona) a partir de datos recolectados de la plataforma [FACUA: Precios Supermercados](https://super.facua.org/). FACUA ofrece datos actualizados diariamente sobre precios de productos, permitiendo a los usuarios comparar y observar fluctuaciones de precio. Aquí empleamos herramientas de scraping y procesamiento de datos para crear una base de datos en SQL, analizar la información y generar visualizaciones para obtener conclusiones claras sobre tendencias y prácticas de precios en los supermercados.

## Objetivos Específicos

1. **Scraping de datos**: Extraer información detallada de productos y precios.
2. **Almacenamiento estructurado**: Crear una base de datos en SQL para organizar los datos.
3. **Análisis de datos**:
   - Comparación de precios entre supermercados.
   - Evaluación de la evolución temporal de precios.
   - Detección de anomalías de precios.
   - Análisis de dispersión y comparación de precios promedio.
4. **Visualización de datos**: Crear gráficos para comunicar los resultados.

## Estructura del Proyecto

```
├── datos/                  # Archivos CSV y datos en crudo
│   ├── df_complete.csv      # Archivo csv con todos los datos recopilados
├── notebooks/              # Notebooks Jupyter para EDA y análisis específicos
│   ├── 1-scraping.ipynb    # Scrapeo de la web de facua
│   ├── 2-ddbb_creation     # Creación de la BBDD e inserción de valores
│   ├── 3-analysis          # Análisis de los datos y visualizaciones
├── scripts/                # Scripts de scraping y procesamiento de datos
│   ├── scraping_funcs.py   # Funciones para scrapeo
│   ├── query_funcs.py      # Funciones para ejecutar queries SQL desde python
│   ├── analysis_funcs.py   # Funciones usadas para el análisis de los datos
├── environment.yml         # Archivo de configuración para gestionar dependencias del entorno
└── README.md               # Documentación del proyecto
```

## Instalación y Requisitos

Para configurar el entorno de desarrollo y asegurarte de que todas las dependencias necesarias estén instaladas, sigue estos pasos:

### Requisitos

- Python 3.7 o superior 🐍
- [Anaconda](https://www.anaconda.com/products/distribution) o [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (opcional, pero recomendado)

### Paquetes Necesarios

El proyecto utiliza los siguientes paquetes:

- [`pandas`](https://pandas.pydata.org/pandas-docs/stable/): Para la manipulación y análisis de datos.
- [`numpy`](https://numpy.org/doc/stable/): Para operaciones numéricas y manejo de arrays.
- [`matplotlib`](https://matplotlib.org/stable/users/index.html): Para la visualización de datos.
- [`seaborn`](https://seaborn.pydata.org/): Para visualización estadística de datos.
- [`plotly`](https://plotly.com/python/): Para gráficos interactivos.
- [`tqdm`](https://tqdm.github.io/): Para mostrar barras de progreso en loops.
- [`psycopg2`](https://www.psycopg.org/): Para conectar Python con PostgreSQL.
- [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Para el scraping de datos.
- [`requests`](https://docs.python-requests.org/en/latest/): Para realizar solicitudes HTTP sencillas.

### Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/yanruwu/Proyecto4-Analisis-Supermercados
   cd Proyecto4-Analisis-Supermercados
2. **Crea un entorno virtual:**

    Para crear el entorno de Conda, usa el siguiente comando:
    ```bash
    conda env create -f environment.yml
    ```
    O si prefieres usar venv:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate     # En Windows
    ```
    