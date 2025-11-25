import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Calculo de Tela - Tempo é Dinheiro',    
    layout='centered'
)

# CSS personalizado
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

# Container de entrada de dados
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
    
    if tempo_total_diario_horas > 0:
        st.markdown(f"**Tempo diário total:** {tempo_total_diario_horas:.1f} horas ({tempo_total_diario_minutos} minutos)")

# Container de resultados
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
    
    # Header dos resultados
    st.markdown("---")
    if qtd_anos > 1:
        st.markdown(f'### Em {qtd_anos} anos, você gastará:')
    else:
        st.markdown(f'### Em {qtd_anos} ano, você gastará:')
    
    # Exibição dos resultados em cards
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