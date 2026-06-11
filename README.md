# Análisis de Absentismo Docente: Plataforma de Inteligencia "Mastermind"

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![ML](https://img.shields.io/badge/Machine-Learning-orange.svg)
![XAI](https://img.shields.io/badge/Explainable-AI-red.svg)
![Status](https://img.shields.io/badge/Status-Elite-success.svg)

## 🧠 Resumen de la Solución

Esta plataforma representa el estándar más alto en análisis de datos para el sector educativo. No es solo un cuaderno de análisis; es una **arquitectura modular de inteligencia de datos** diseñada para diagnosticar, predecir y explicar los fenómenos de absentismo docente en Cundinamarca.

## 🚀 Capacidades de Vanguardia

*   **Arquitectura Modular**: Lógica desacoplada en el paquete `src/` (ML, Geo, Styling, Utils).
*   **Inteligencia Artificial Explicable (XAI)**: Motor SHAP que desglosa la contribución individual de cada variable al riesgo de un docente.
*   **Análisis de Supervivencia (KM)**: Modelado de la probabilidad de retorno al trabajo tras una ausencia.
*   **Geospatial Intelligence**: Mapeo preciso de "hotspots" de absentismo en municipios de Cundinamarca.
*   **Segmentación Multidimensional**: Identificación de perfiles mediante MCA (3D) y K-Means.
*   **Análisis de Cohortes**: Evaluación del impacto basado en la antigüedad del funcionario.
*   **Visualización de Élite**: Dashboards interactivos en Streamlit, diagramas de Sankey, curvas de Lorenz y grafos de red.

## 📊 Diccionario de Datos Maestro

El proyecto incluye un **Diccionario de Datos (Mastermind Level)** integrado directamente en el notebook, detallando tipos, formatos y el rol estratégico de cada columna en el pipeline analítico.

## 🛠️ Stack Tecnológico

*   **Core**: Pandas, NumPy, XGBoost, Scikit-Learn.
*   **Insights**: Meta Prophet, Lifelines (Survival), SHAP.
*   **Viz**: Plotly, Seaborn, Matplotlib, NetworkX, WordCloud.
*   **App**: Streamlit.

## 💻 Ejecución

### Visualización Rápida
Abra `Proyecto/Final.ipynb`. Todos los resultados están pre-renderizados en alta fidelidad.

### Dashboard Interactivo
```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

---
*Transformando registros administrativos en decisiones estratégicas de alta fidelidad.*
