import xgboost as xgb
import shap
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def train_risk_model(df):
    """Trains an XGBoost model to predict high absenteeism risk (> 5 days)."""
    # Feature Engineering for Model
    model_df = df[['EDAD', 'FEMENINO', 'TIPO', 'SUBTIPO', 'DIAS HABILES']].copy()
    model_df['target'] = (model_df['DIAS HABILES'] > 5).astype(int)

    le_tipo = LabelEncoder()
    le_sub = LabelEncoder()
    model_df['TIPO_CODE'] = le_tipo.fit_transform(model_df['TIPO'].astype(str))
    model_df['SUBTIPO_CODE'] = le_sub.fit_transform(model_df['SUBTIPO'].astype(str))

    features = ['EDAD', 'FEMENINO', 'TIPO_CODE', 'SUBTIPO_CODE']
    X = model_df[features]
    y = model_df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)

    # Calculate SHAP values
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    return model, explainer, shap_values, X_test, features

def get_risk_probability(model, data_row):
    """Returns the probability of high risk for a single record."""
    return model.predict_proba(data_row)[:, 1]
