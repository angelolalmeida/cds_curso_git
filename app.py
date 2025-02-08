# arquivo de teste do git
import pandas as pd

def main():
  print('Esta é a main!')
  print('Este é um teste na main!')
  df = load_data()
  print(df.head())
  
def load_data():
  # Informações sobre emprego e salário por setor no estado de São Paulo
  # https://repositorio.seade.gov.br/dataset/emprego-rais-e-arquivos-auxiliares
  escolaridade = pd.read_excel("dados/escolaridade-2022-2023.xlsx")
  return escolaridade

if __name__ == '__main__':
  main()