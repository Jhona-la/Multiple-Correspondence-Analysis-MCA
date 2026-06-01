import pandas as pd
import numpy as np
import os
import prince
from sklearn.cluster import KMeans
from prophet import Prophet

try:
    print("Loading data...")
    df = pd.read_excel('Proyecto/Consolidado.xlsx')
    df.columns = [col.strip() for col in df.columns]

    print("Preprocessing...")
    birth_col = "TO_CHAR(E.FECHANACIMIENTO,'DD-MM-YYYY')"
    if birth_col not in df.columns: birth_col += ' '
    df['birth_date'] = pd.to_datetime(df[birth_col], unit='D', origin='1899-12-30')
    ref = pd.to_datetime('2022-01-01')
    df['EDAD'] = df['birth_date'].apply(lambda x: ref.year - x.year - ((ref.month, ref.day) < (x.month, x.day)))
    df['FEMENINO'] = df['SEXO'].apply(lambda x: 1 if str(x).strip().upper() == 'F' else 0)
    df['RANGO DE EDAD'] = pd.cut(df['EDAD'], bins=[0,18,25,35,45,55,65,120], labels=['0-18','19-25','26-35','36-45','46-55','56-65','66+'])
    df['FECHA INICIAL'] = pd.to_datetime(df['INICIO_OCURRENCIA'])

    print("MCA...")
    mca_cols = ['TIPO', 'SUBTIPO', 'SEXO', 'RANGO DE EDAD']
    mca = prince.MCA(n_components=2)
    mca.fit(df[mca_cols].astype(str))
    row_coords = mca.row_coordinates(df[mca_cols].astype(str))

    print("Clustering...")
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(row_coords)

    print("Prophet...")
    df_time = df.copy()
    df_time['ds'] = df_time['FECHA INICIAL']
    df_monthly = df_time.set_index('ds').resample('ME').size().reset_index()
    df_monthly.columns = ['ds', 'y']
    m = Prophet()
    m.fit(df_monthly)

    print("DIAGNOSTIC SUCCESS")
except Exception as e:
    print(f"DIAGNOSTIC FAILED: {e}")
    import traceback
    traceback.print_exc()
