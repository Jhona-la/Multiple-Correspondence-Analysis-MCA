import pandas as pd
import numpy as np
import os
from scipy.stats import chi2_contingency

def load_and_preprocess_data(filename="Consolidado.xlsx"):
    """Robustly loads and pre-processes the teacher absenteeism dataset."""
    possible_paths = [filename, f"Proyecto/{filename}", f"../data/{filename}", f"data/{filename}"]
    data_path = next((p for p in possible_paths if os.path.exists(p)), None)

    if not data_path:
        raise FileNotFoundError(f"Data file {filename} not found in expected paths.")

    df = pd.read_excel(data_path)
    df.columns = [col.strip() for col in df.columns]

    # Date processing
    birth_col = "TO_CHAR(E.FECHANACIMIENTO,'DD-MM-YYYY')"
    if birth_col not in df.columns: birth_col += " "

    if not pd.api.types.is_datetime64_any_dtype(df[birth_col]):
        df["birth_date"] = pd.to_datetime(df[birth_col], unit="D", origin="1899-12-30")
    else:
        df["birth_date"] = df[birth_col]

    reference_date = pd.to_datetime("2022-01-01")
    df["EDAD"] = df["birth_date"].apply(lambda x: reference_date.year - x.year - ((reference_date.month, reference_date.day) < (x.month, x.day)))
    df["FEMENINO"] = df["SEXO"].apply(lambda x: 1 if str(x).strip().upper() == "F" else 0)

    bins = [0, 18, 25, 35, 45, 55, 65, 120]
    labels = ["0-18", "19-25", "26-35", "36-45", "46-55", "56-65", "66+"]
    df["RANGO DE EDAD"] = pd.cut(df["EDAD"], bins=bins, labels=labels)

    df["FECHA INICIAL"] = pd.to_datetime(df["INICIO_OCURRENCIA"])
    return df

def calculate_cramers_v(tab):
    """Calculates Cramer's V for a contingency table."""
    if tab.size == 0 or min(tab.shape) <= 1:
        return 0
    chi2 = chi2_contingency(tab)[0]
    n = tab.sum().sum()
    return np.sqrt(chi2 / (n * (min(tab.shape)-1)))

def get_phi_coefficient(c_matrix):
    """Calculates the Phi coefficient for a 2x2 contingency table."""
    if c_matrix.shape == (2, 2):
        a, b = c_matrix[0, 0], c_matrix[0, 1]
        c, d = c_matrix[1, 0], c_matrix[1, 1]
        denom = np.sqrt(float(a + b) * (c + d) * (a + c) * (b + d))
        if denom == 0: return 0
        return (a * d - b * c) / denom
    return 0
