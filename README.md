# Análisis de Absentismo Docente: Edición de Élite

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Data Science](https://img.shields.io/badge/Data-Science-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## 📋 Resumen del Proyecto

Este repositorio contiene una solución integral de análisis de datos para el **absentismo docente** en el sector educativo. Utilizando técnicas avanzadas de Machine Learning, Series Temporales y Visualización de Datos, el proyecto transforma registros administrativos en inteligencia accionable para la toma de decisiones estratégicas.

La solución aborda el problema desde múltiples dimensiones: demográfica, geográfica, temporal y conductual, permitiendo identificar no solo *qué* está pasando, sino *por qué* y *qué pasará* en el futuro.

## 🚀 Características Principales

*   **Dashboards Ejecutivos**: Resúmenes visuales de alto impacto mediante Plotly y CSS personalizado.
*   **Forecasting con Prophet**: Predicción del volumen de ausencias para los próximos 6 meses.
*   **Segmentación Inteligente**: Agrupación de docentes mediante MCA (Análisis de Correspondencias Múltiples) y K-Means.
*   **Detección de Anomalías**: Identificación de patrones de absentismo inusuales mediante Isolation Forest.
*   **Scoring de Riesgo**: Algoritmo ponderado para identificar funcionarios críticos que requieren intervención.
*   **Visualización Multidimensional**: Diagramas de Sankey, Mapas de Calor, Parallel Categories y Gráficos de Piruleta.

## 📊 Estructura de Datos

El análisis se basa en el archivo `Consolidado.xlsx` (ubicado en `Proyecto/`), que contiene registros de novedades administrativas. Las variables clave incluyen:

*   **TIPO**: Vinculación (1: Planta, 2: Provisional).
*   **SUBTIPO**: Motivo específico de la novedad (Licencias, Permisos, Traslados).
*   **DIAS HABILES**: El KPI principal; impacto en la continuidad educativa.
*   **EDAD / SEXO**: Dimensiones demográficas para el perfilado.

## 📁 Organización del Repositorio

*   `Proyecto/Final.ipynb`: Cuaderno principal con el análisis completo y visualizaciones de élite.
*   `Proyecto/Consolidado.xlsx`: Dataset principal procesado.
*   `Datos filtrados.xlsx / .csv`: Archivos de datos complementarios.

## 🛠️ Tecnologías Utilizadas

*   **Análisis**: Pandas, NumPy, Scipy.
*   **Machine Learning**: Scikit-Learn (Isolation Forest, KMeans, RandomForest).
*   **Forecasting**: Meta Prophet.
*   **Visualización**: Plotly, Seaborn, Matplotlib, Bokeh, WordCloud, NetworkX.

## 💻 Ejecución

Para visualizar los resultados, simplemente abra el cuaderno `Proyecto/Final.ipynb` en GitHub. El cuaderno ha sido pre-ejecutado y todos los gráficos dinámicos se renderizan automáticamente en formato estático de alta resolución.

---
*Desarrollado como una herramienta de apoyo a la gestión humana en el sector educativo.*

## 🌐 Dashboard Interactivo (Streamlit)

Para ejecutar la aplicación web interactiva, asegúrese de tener instaladas las dependencias y ejecute:

```bash
streamlit run dashboard.py
```

El dashboard permite filtrar datos en tiempo real por sede y vinculación, visualizando KPIs dinámicos y análisis de impacto.
