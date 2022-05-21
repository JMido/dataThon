from cgitb import html
import requests
from requests import get
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

# Función para imprimir DFs
def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

# Función para realizar el analisis de los csv:)
def analysis(file_name: str) -> None:
    df = pd.read_csv(file_name)

    # Se revisan datos por region
    print_tabulate(df.groupby(["Region"], as_index=False)["Ingresos"].agg(['sum', 'mean', 'count']))
    print("\n")

    # Se revisan datos por fecha
    print_tabulate(df.groupby(["Fecha"], as_index=False)["Ingresos"].agg(['sum', 'mean', 'count', 'min', 'max']))
    print_tabulate(df.describe())
    print("\n\n")

    # Datos para analizar la distribución de las variables
    print(df.kurtosis(numeric_only=True))
    print("\n\n")

    print(df.skew(numeric_only=True))
    print("\n\n")

analysis("csv/2019_cleaned_v2.csv")

df1 = pd.read_csv("csv/2019_cleaned.csv")

# Verificar si datos están correctos (parece que sí) // Checar si hay datos nulos o faltantes
df1.info()
print(f"\n---------------\n {df1.isna()} \n---------------\n\n")
print_tabulate(df1.head())

# Hacer otro csv para trabajar en él y no modificar el archivo original
correct_df = df1.copy()
correct_df.rename(columns={'Empresa': 'Empresa', 'Region': 'Region', 'Filial': 'Filial', 'Tipo': 'Tipo',
                           'Punto de venta': 'Punto de venta', '%Key_Cliente': 'Cliente', '%Key_FechaID': 'Fecha',
                           '%Key_Folio': 'Folio', '%Key_Ticket': 'Ticket', 'Litros': 'Litros vendidos', '$': 'Ingresos', 'Tem_prom': 'Temperatura'}, inplace=True)
                           
print_tabulate(correct_df.head())
correct_df.to_csv(r'csv/2019_cleaned_v2.csv', index=False)



