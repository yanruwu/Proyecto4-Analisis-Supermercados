

def get_outliers(data):
    q1,q3 = data.quantile([0.25,0.75])
    iqr = q3-q1
    upper_fence = q3 + (1.5*iqr)
    lower_fence = q1 - (1.5*iqr)
    outliers = data[(data < lower_fence) | (data > upper_fence)]
    # print(iqr)
    # print(lower_fence, upper_fence)
    return outliers

def get_outliers_especificos(df, nombre_super, subcat):
    datos = df[(df["supermercado"] == nombre_super) & (df["subcategoria"] == subcat)]["precio_norm"].astype(float)
    return get_outliers(datos)


def get_min(df, supermercado, subcat):
    prods = df[(df["supermercado"] == supermercado)&(df["subcategoria"] == subcat)]
    return df.iloc[prods["precio_norm"].idxmin()]

def get_max(df, supermercado, subcat):
    prods = df[(df["supermercado"] == supermercado)&(df["subcategoria"] == subcat)]
    return df.iloc[prods["precio_norm"].idxmax()]