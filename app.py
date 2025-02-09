import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def main():
  print('Esta é a main!')
  df_raw = load_data()
  print(df_raw.head())
  

if __name__ == '__main__':
  main()