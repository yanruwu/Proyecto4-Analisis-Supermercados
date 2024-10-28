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

