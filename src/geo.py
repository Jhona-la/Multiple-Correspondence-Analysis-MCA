import pandas as pd

def get_city_coords():
    """Returns approximate coordinates for top Cundinamarca municipalities."""
    return {
        'Cajica': [4.9197, -74.0272],
        'Sibate': [4.4925, -74.2600],
        'Guaduas': [5.0672, -74.5964],
        'Guacheta': [5.3833, -73.6833],
        'Anolaima': [4.7633, -74.4700],
        'Subachoque': [4.9317, -74.1750],
        'Tocancipa': [4.9644, -73.9114],
        'Nocaima': [5.0833, -74.4667],
        'Viota': [4.4411, -74.5236],
        'Ubaque': [4.4900, -73.9400],
        'Yacopi': [5.4667, -74.3333],
        'Paratebueno': [4.3833, -73.2167],
        'Sopo': [4.9100, -73.9400],
        'Caparrapi': [5.3333, -74.5000],
        'Choachi': [4.5300, -73.9200],
        'Gachancipa': [4.9900, -73.8700],
        'Villapinzon': [5.2100, -73.6000],
        'Guasca': [4.8600, -73.8700],
        'Pacho': [5.1300, -74.1600],
        'Quetame': [4.3300, -73.9100]
    }

def clean_city_name(name):
    if not isinstance(name, str): return name
    return name.split('(')[0].strip()
