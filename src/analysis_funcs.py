import pandas as pd
from pandas import DataFrame, Series

def get_outliers(data: Series) -> Series:
    """
    Detecta valores atípicos en un conjunto de datos utilizando el método del rango intercuartílico (IQR).

    Args:
        data (Series): Serie de pandas que contiene los datos numéricos para analizar.

    Returns:
        Series: Serie de pandas que contiene los valores atípicos detectados.
    """
    q1,q3 = data.quantile([0.25,0.75])
    iqr = q3-q1
    upper_fence = q3 + (1.5*iqr)
    lower_fence = q1 - (1.5*iqr)
    outliers = data[(data < lower_fence) | (data > upper_fence)]
    # print(iqr)
    # print(lower_fence, upper_fence)
    return outliers

def get_outliers_especificos(df: DataFrame, nombre_super: str, subcat: str) -> Series:
    """
    Detecta valores atípicos específicos para una subcategoría y supermercado dados.

    Args:
        df (DataFrame): DataFrame que contiene los datos de precios y supermercados.
        nombre_super (str): Nombre del supermercado para filtrar los datos.
        subcat (str): Nombre de la subcategoría para filtrar los datos.

    Returns:
        Series: Serie de pandas que contiene los valores atípicos detectados para la subcategoría y supermercado especificados.
    """
    datos = df[(df["supermercado"] == nombre_super) & (df["subcategoria"] == subcat)]["precio_norm"].astype(float)
    return get_outliers(datos)


def get_min(df: DataFrame, supermercado: str, subcat: str) -> Series:
    """
    Obtiene el producto con el precio mínimo en una subcategoría y supermercado dados.

    Args:
        df (DataFrame): DataFrame que contiene los datos de precios y supermercados.
        supermercado (str): Nombre del supermercado para filtrar los datos.
        subcat (str): Nombre de la subcategoría para filtrar los datos.

    Returns:
        Series: Serie de pandas que representa la fila del producto con el precio mínimo en la subcategoría y supermercado especificados.
    """
    prods = df[(df["supermercado"] == supermercado)&(df["subcategoria"] == subcat)]
    return df.iloc[prods["precio_norm"].idxmin()]

def get_max(df: DataFrame, supermercado: str, subcat: str) -> Series:
    """
    Obtiene el producto con el precio máximo en una subcategoría y supermercado dados.

    Args:
        df (DataFrame): DataFrame que contiene los datos de precios y supermercados.
        supermercado (str): Nombre del supermercado para filtrar los datos.
        subcat (str): Nombre de la subcategoría para filtrar los datos.

    Returns:
        Series: Serie de pandas que representa la fila del producto con el precio máximo en la subcategoría y supermercado especificados.
    """
    prods = df[(df["supermercado"] == supermercado)&(df["subcategoria"] == subcat)]
    return df.iloc[prods["precio_norm"].idxmax()]