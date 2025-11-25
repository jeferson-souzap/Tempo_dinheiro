# Calculadora Tempo é Dinheiro

Uma aplicação web interativa desenvolvida em Streamlit que calcula o tempo total gasto no celular ao longo dos anos e mostra o impacto desse tempo em unidades maiores como dias, semanas, meses e anos.

## Sobre o Projeto

Esta ferramenta foi criada para conscientizar sobre o tempo que passamos no celular e ajudar as pessoas a visualizarem como pequenos períodos diários se acumulam significativamente ao longo dos anos.

## Funcionalidades

- **Calculo de Tempo Total**: Converte o uso diário do celular em tempo acumulado ao longo de anos
- **Multiplas Unidades de Tempo**: Mostra resultados em minutos, horas, dias, semanas, meses e anos
- **Interface Interativa**: Seletor deslizante para escolher diferentes períodos de análise (1 a 50 anos)
- **Layout Responsivo**: Design adaptável que funciona em diferentes tamanhos de tela
- **Reflexão Personalizada**: Sugestões do que poderia ser feito com o tempo economizado

## Como Usar

1. **Informe o Tempo Diário**:
   - Digite quantas horas por dia você usa o celular
   - Adicione minutos extras se necessário

2. **Selecione o Período**:
   - Escolha quantos anos deseja analisar (1 a 50 anos)

3. **Veja os Resultados**:
   - Visualize o tempo total acumulado em diferentes unidades
   - Receba insights sobre como aproveitar melhor seu tempo

## Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit** - Framework para aplicações web
- **Pandas** - Manipulação de dados

## Instalação e Execução

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passos para instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/calculadora-tempo-celular.git
cd calculadora-tempo-celular
```

2. Instale as dependências:

```bash
pip install streamlit pandas
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

4. Acesse no navegador:
   - Abra <http://localhost:8501>
   - A aplicação estará rodando localmente

## Estrutura do Projeto

```bash
calculadora-tempo-celular/
│
├── app.py                 # Arquivo principal da aplicação
├── requirements.txt       # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Exemplo de Cálculo

Se você usa o celular **2 horas por dia** durante **10 anos**:

- **Tempo total**: 7.300 horas
- **Equivalente a**: 304 dias completos
- **Ou aproximadamente**: 10 meses do ano

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Melhorar a documentação

## Contato

Se tiver alguma dúvida ou sugestão, entre em contato através das issues do GitHub.

---

**Lembre-se**: Pequenos momentos no celular se transformam em grandes períodos ao longo da vida. Use seu tempo com consciência!
