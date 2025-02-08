import pandas as pd

def load_data():
  # Informações sobre emprego e salário por setor no estado de São Paulo
  # https://repositorio.seade.gov.br/dataset/emprego-rais-e-arquivos-auxiliares
  return pd.read_excel("data\escolaridade-2022-2023.xlsx")