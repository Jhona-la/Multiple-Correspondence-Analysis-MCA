import json
import uuid

def add_advanced_analysis(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # 1. Update imports
    nb['cells'][0]['source'].extend([
        "from sklearn.cluster import KMeans\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "import plotly.graph_objects as go\n"
    ])

    # 2. Add advanced analysis cells
    advanced_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# Análisis Avanzado: Clustering y Profundización MCA\n", "En esta sección realizamos una segmentación de datos y un análisis detallado de las contribuciones de las variables."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Preparación de datos para MCA profundo\n",
                "cols_para_mca = ['TIPO', 'SUBTIPO', 'SEXO', 'ZONA', 'RANGO DE EDAD', 'NIVELCONTRATACION']\n",
                "df_mca = datos_total[cols_para_mca].copy().astype(str)\n",
                "\n",
                "mca_final = prince.MCA(n_components=5)\n",
                "mca_final.fit(df_mca)\n",
                "\n",
                "# Obtener coordenadas de filas (individuos)\n",
                "row_coords = mca_final.row_coordinates(df_mca)\n",
                "print('Coordenadas MCA calculadas.')\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Segmentación de Usuarios (K-Means sobre MCA)\n",
                "n_clusters = 4\n",
                "kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)\n",
                "clusters = kmeans.fit_predict(row_coords)\n",
                "datos_total['Cluster'] = clusters.astype(str)\n",
                "\n",
                "print(f'Segmentación completada en {n_clusters} clusters.')\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Visualización de Clusters en 2D (MCA Dim 1 vs Dim 2)\n",
                "fig_clusters = px.scatter(row_coords, x=0, y=1, color=datos_total['Cluster'],\n",
                "                         title='Segmentación de Usuarios basada en MCA',\n",
                "                         labels={'0': 'Dimensión 1', '1': 'Dimensión 2'},\n",
                "                         template='plotly_white', opacity=0.6)\n",
                "fig_clusters.show()\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Perfilado de Clusters: ¿Qué define a cada grupo?\n",
                "cluster_profile = datos_total.groupby('Cluster')[['EDAD', 'TIPO', 'SUBTIPO']].agg(['mean', 'median'])\n",
                "print('Perfil promedio de los clusters:')\n",
                "display(cluster_profile)\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Análisis de Contribuciones de Variables\n",
                "col_coords = mca_final.column_coordinates(df_mca)\n",
                "fig_contrib = px.bar(col_coords, y=0, x=col_coords.index, \n",
                "                     title='Contribución de Categorías a la Dimensión 1',\n",
                "                     labels={'0': 'Peso en Dim 1', 'index': 'Categoría'},\n",
                "                     color=col_coords[0])\n",
                "fig_contrib.show()\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Análisis Temporal: Evolución de Casos por Mes\n",
                "datos_total['Mes_Ano'] = datos_total['FECHA INICIAL'].dt.to_period('M').astype(str)\n",
                "temporal_trend = datos_total.groupby(['Mes_Ano', 'TIPO']).size().reset_index(name='Casos')\n",
                "\n",
                "fig_time = px.line(temporal_trend, x='Mes_Ano', y='Casos', color='TIPO', \n",
                "                   title='Evolución Temporal de Casos por Tipo',\n",
                "                   markers=True)\n",
                "fig_time.show()\n"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Heatmap de Correlación entre Categorías (vía Cramer's V simplificado)\n",
                "import seaborn as sns\n",
                "plt.figure(figsize=(12, 8))\n",
                "pivot_table = pd.crosstab(datos_total['RANGO DE EDAD'], datos_total['SUBTIPO'])\n",
                "sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')\n",
                "plt.title('Relación entre Rango de Edad y Subtipo')\n",
                "plt.show()\n"
            ]
        }
    ]

    for cell in advanced_cells:
        cell['id'] = str(uuid.uuid4())[:8]

    nb['cells'].extend(advanced_cells)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    add_advanced_analysis('Proyecto/Final.ipynb')
    print("Advanced analysis added.")
