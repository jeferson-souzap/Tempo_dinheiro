import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta
import time
import plotly.express as px

#Importa outras paginas
from utils.config_historico import *

st.set_page_config(
    page_title='Calculo de Tela - Tempo é Dinheiro',    
    layout= 'wide',
    initial_sidebar_state='collapsed'
)

# Testando o uso de CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem !important;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .result-card {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #ff6b6b;
    }
    .time-unit {
        font-weight: bold;
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Tempo é Dinheiro</h1>', unsafe_allow_html=True)

st.info('Veja o que pode ser feito com o tempo que você ~PERDE~ no celular.')

#Entrada de dados
with st.container(border=True):
    st.subheader('Entrada de Dados')
    st.markdown('Preencha os campos abaixo para calcular o tempo gasto no celular e descubra o que poderia ser feito com esse tempo.')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('**Tempo gasto no celular por dia:**')
        tempo_horas = st.number_input(
            'Horas por dia', 
            min_value=0, 
            max_value=24,
            value=2,
            help="Quantidade de horas que você usa o celular por dia"
        )

    with col2:
        st.markdown('**Tempo adicional em minutos:**')
        tempo_minutos = st.number_input(
            'Minutos por dia', 
            min_value=0, 
            max_value=59,
            value=0,
            help="Minutos adicionais de uso diário"
        )
    
    st.markdown("---")
    
    # Resumo do tempo diário
    tempo_total_diario_minutos = tempo_horas * 60 + tempo_minutos
    tempo_total_diario_horas = tempo_total_diario_minutos / 60
    
    with st.expander('Botão para salvar o registro diário'):

        if st.button('Salvar Registro', type='primary', use_container_width=True):
            data_atual = datetime.datetime.now().date()
            
            inserir_registro(
                data=data_atual,
                hora=tempo_horas,
                minuto=tempo_minutos,
                tempo_total=str(timedelta(minutes=tempo_total_diario_minutos))
            )
            st.success('Registro salvo com sucesso!')



# Grafico de horas

with st.container(border=True):
    st.subheader('Comparação do tempo de um dia')

    col01, col02 = st.columns(2)

    with col01:
        TEMPO_MIN_DIA = 24
        HR_SONO = 8
        HR_TRABALHO = 8
        HR_TRAJETO = 1

        
        horas_sono = st.slider("Horas de Sono", min_value=0, max_value=24, value=HR_SONO, step=1, key='sono')
        horas_trabalho = st.slider("Horas de trabalho", min_value=0, max_value=24, value=HR_TRABALHO, step=1, key='trabalho')    
        horas_trajeto = st.slider("Horas de Trajeto", min_value=0, max_value=24, value=HR_TRAJETO, step=1, key='trajeto')
        
        horas_celular = st.slider("Horas de Celular", min_value=0, max_value=24, value=tempo_horas, step=1, key='hr_cel', disabled=True)    
        
        HR_RESTANTE = TEMPO_MIN_DIA - (horas_sono + horas_trabalho + horas_trajeto + tempo_horas)
        horas_restantes = st.slider("Horas Restante", min_value=0, max_value=24, value=HR_RESTANTE, step=1, key='restante', disabled=True)

        TOTAL_HR = horas_sono + horas_trabalho + horas_trajeto + horas_celular + horas_restantes
        st.info(f"Soma horas = {TOTAL_HR}h")
        if HR_RESTANTE < 0:
            st.warning("Verifique o valor das horas, **horario** restante não pode ficar negativo!")
    
    with col02:
        
        dados = {
            "Atividades":['Sono', 'Trabalho', 'Trajeto', 'Tela', 'Livre'],
            "Horas":[horas_sono, horas_trabalho, horas_trajeto, tempo_horas, horas_restantes]
        }

        df = pd.DataFrame(dados)

        fig = px.pie(
            df,
            values='Horas',
            names='Atividades',
            title='Distribuição de 24 Horas',
            color='Atividades',
            color_discrete_map={
                'Sono': '4C72B0',
                'Trabalho': 'DD8452',
                'Trajeto': '8C8C8C',
                'Tela': 'A44C9E',
                'Livre': '55A868'
            }           

        )

        fig.update_traces(
            textposition='inside',
            textinfo='percent+label'
            #hovertemplate='%{label}<br>Horas: %{value} (%{percent})<extra></extra>' # Adicionei este detalhe útil
        )
        
        st.plotly_chart(fig, use_container_width=True)
    

    






# Resultados
with st.container(border=True):
    st.subheader('Resultados')
    
    st.markdown("**Selecione o período para análise:**")
    qtd_anos = st.select_slider(
        'Quantidade de anos:',
        options=[1, 2, 3, 4, 5, 10, 20, 30, 40, 50],
        value=1,
        label_visibility="collapsed"
    )
    
    # Cálculos
    tempo_total_minutos_diario = tempo_horas * 60 + tempo_minutos
    tempo_total_minutos_anual = tempo_total_minutos_diario * 365 * qtd_anos
    
    # Conversões
    horas_totais = tempo_total_minutos_anual / 60
    dias_totais = horas_totais / 24
    semanas_totais = dias_totais / 7
    meses_totais = dias_totais / 30
    anos_totais = dias_totais / 365
    
    
    st.markdown("---")
    if qtd_anos > 1:
        st.markdown(f'### Em {qtd_anos} anos, você gastará:')
    else:
        st.markdown(f'### Em {qtd_anos} ano, você gastará:')
    
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<div class="result-card">'
                   f'<span class="time-unit"> Horas totais:</span><br>'
                   f'<span style="font-size: 1.5rem; font-weight: bold;">{horas_totais:,.0f} horas</span>'
                   f'</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="result-card">'
                   f'<span class="time-unit"> Dias totais:</span><br>'
                   f'<span style="font-size: 1.5rem; font-weight: bold;">{dias_totais:,.0f} dias</span>'
                   f'</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="result-card">'
                   f'<span class="time-unit"> Meses totais:</span><br>'
                   f'<span style="font-size: 1.5rem; font-weight: bold;">{meses_totais:,.0f} meses</span>'
                   f'</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="result-card">'
                   f'<span class="time-unit"> Minutos totais:</span><br>'
                   f'<span style="font-size: 1.5rem; font-weight: bold;">{tempo_total_minutos_anual:,.0f} minutos</span>'
                   f'</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="result-card">'
                   f'<span class="time-unit"> Semanas totais:</span><br>'
                   f'<span style="font-size: 1.5rem; font-weight: bold;">{semanas_totais:,.0f} semanas</span>'
                   f'</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="result-card">'
                   f'<span class="time-unit"> Anos totais:</span><br>'
                   f'<span style="font-size: 1.5rem; font-weight: bold;">{anos_totais:.2f} anos</span>'
                   f'</div>', unsafe_allow_html=True)


st.divider()

with st.container():
    st.subheader('Oportunidades de Uso do Tempo')

    tempo_leitura_horas = 6 # Média de horas para ler um livro de 250 páginas
    tempo_curso_horas = 150    # Média de horas para completar um curso online
    tempo_exercicio_horas = 1000  # Média de horas para treinar para uma maratona
    tempo_idioma_horas = 600   # Média de horas para aprender um novo idioma
    tempo_voluntariado_horas = 500  # Média de horas para trabalho voluntário significativo
    tempo_projeto_horas = 300  # Média de horas para completar um projeto pessoal
    


    #col1, col2, col3, col4 = st.columns(4)
    
    noites_sono = horas_totais / 8
    st.markdown(f'<div class="result-card">'
                f'<span class="time-unit"> Noites de sono (8 hr/noite):</span><br>'
                f'<span style="font-size: 1.5rem; font-weight: bold;">{noites_sono:,.0f} noite(s)</span>'
                f'</div>', unsafe_allow_html=True)


    qtd_livros = horas_totais / tempo_leitura_horas
    st.markdown(f'<div class="result-card">'
                f'<span class="time-unit"> Quantidade de livros lidos:</span><br>'
                f'<span style="font-size: 1.5rem; font-weight: bold;">{qtd_livros:,.0f} livro(s)</span>'
                f'</div>', unsafe_allow_html=True)
    
    tempo_aprender_idioma = horas_totais / tempo_idioma_horas
    st.markdown(f'<div class="result-card">'
                f'<span class="time-unit"> Total de idiomas (média 600 hr até dominar):</span><br>'
                f'<span style="font-size: 1.5rem; font-weight: bold;">{tempo_aprender_idioma:,.0f} idioma(s)</span>'
                f'</div>', unsafe_allow_html=True)


    qtd_cursos = horas_totais / tempo_curso_horas
    st.markdown(f'<div class="result-card">'
                f'<span class="time-unit"> Quantidade de cursos online de 150 horas:</span><br>'
                f'<span style="font-size: 1.5rem; font-weight: bold;">{qtd_cursos:,.0f} curso(s)</span>'
                f'</div>', unsafe_allow_html=True)
    
    qtd_exercicios = horas_totais / tempo_exercicio_horas
    st.markdown(f'<div class="result-card">'
                f'<span class="time-unit"> Total de maratonas treinadas (média 1000 hr):</span><br>'
                f'<span style="font-size: 1.5rem; font-weight: bold;">{qtd_exercicios:,.0f} maratona(s)</span>'
                f'</div>', unsafe_allow_html=True)
    
