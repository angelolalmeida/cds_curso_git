import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def main():
  print('Esta é a main!')
  df = load_data()
  print(df.head())
  

if __name__ == '__main__':
  main()