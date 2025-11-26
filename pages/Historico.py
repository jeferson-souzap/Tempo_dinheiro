import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta
import time
import matplotlib.pyplot as plt

#Importa outras paginas
from utils.config_db import LOCAL_DB_PATH
from utils.config_historico import *


st.set_page_config(
    page_title='Calculo de Tela - Tempo é Dinheiro',
    layout= 'wide'

)   

df = obter_registros()


with st.container(border=True):
    st.header('Grafico de Uso do Tempo no Celular')
    
    plt.figure(figsize=(15, 5))

    #Somente com tempo total e data
    datas = [registro[1] for registro in df]
    tempos = []
    for registro in df:
        h = registro[2]
        m = registro[3]
        total_minutos = h * 60 + m
        tempos.append(total_minutos)
    plt.plot(datas, tempos, marker='o')
    plt.title('Uso do Tempo no Celular ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Tempo Total (minutos)')
    plt.xticks(rotation=45)    
    st.pyplot(plt)
    


with st.container(border=True):
    st.subheader('Histórico de Registros')
    

    st.dataframe(df, use_container_width=True, column_config={
        1: "ID",
        2: "Data",
        3: "Horas",
        4: "Minutos",
        5: "Tempo Total",
    })
    
    