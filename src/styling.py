import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
from IPython.display import display, HTML

def apply_elite_styling():
    """Applies global aesthetics to the analysis environment."""
    pio.renderers.default = "png"
    sns.set_theme(style="white", context="talk")
    plt.rcParams.update({
        "figure.figsize": (12, 7),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titleweight": "bold",
        "font.family": "sans-serif",
        "figure.dpi": 100
    })

def get_custom_css():
    """Returns the CSS string for notebook styling."""
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Open+Sans:wght@300;400;600&display=swap');
        body { font-family: 'Open Sans', sans-serif; background-color: #f4f7f6; }
        h1, h2, h3 { font-family: 'Montserrat', sans-serif; color: #2c3e50; }
        .rendered_html h1 { border-bottom: 4px solid #3498db; padding-bottom: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
        .rendered_html h2 { border-left: 8px solid #2980b9; padding-left: 15px; margin-top: 40px; background: #ebf5fb; padding-top: 5px; padding-bottom: 5px; }
        .insight-card {
            background: #fff; border-radius: 8px; border-left: 5px solid #e67e22;
            padding: 15px; margin: 15px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            font-style: italic; color: #d35400;
        }
        .data-table { width: 100%; border-collapse: collapse; margin: 25px 0; font-size: 0.9em; box-shadow: 0 0 20px rgba(0,0,0,0.15); }
        .data-table thead tr { background-color: #3498db; color: #ffffff; text-align: left; }
        .data-table th, .data-table td { padding: 12px 15px; }
        .data-table tbody tr { border-bottom: 1px solid #dddddd; }
        .data-table tbody tr:nth-of-type(even) { background-color: #f3f3f3; }
        .data-table tbody tr:last-of-type { border-bottom: 2px solid #3498db; }
    </style>
    """

def show_insight(text):
    """Displays a stylized insight card."""
    display(HTML(f'<div class="insight-card"><b>💡 Insight:</b> {text}</div>'))

def display_kpi_dashboard(total_dias, promedio_dias, total_casos):
    """Displays the executive KPI dashboard using HTML."""
    html_kpis = f"""
    <div style="display: flex; justify-content: space-around; background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #dee2e6;">
        <div style="text-align: center;">
            <h2 style="color: #4a4a4a; margin-bottom: 5px;">{total_dias:,.0f}</h2>
            <p style="color: #6c757d; font-size: 14px;">Total Días de Ausencia</p>
        </div>
        <div style="text-align: center; border-left: 1px solid #dee2e6; border-right: 1px solid #dee2e6; padding: 0 40px;">
            <h2 style="color: #4a4a4a; margin-bottom: 5px;">{promedio_dias:.2f}</h2>
            <p style="color: #6c757d; font-size: 14px;">Promedio Días / Caso</p>
        </div>
        <div style="text-align: center;">
            <h2 style="color: #4a4a4a; margin-bottom: 5px;">{total_casos:,.0f}</h2>
            <p style="color: #6c757d; font-size: 14px;">Total de Registros</p>
        </div>
    </div>
    """
    display(HTML(html_kpis))
