import streamlit as st
import pandas as pd
import plotly.express as px
import io
import time


##------------------------------------------------------------------------------------------------------------

# LOAD DATA

##------------------------------------------------------------------------------------------------------------


# Pesq_Agr_Mun_2020_2021
diretorio = r'C:\Users\digob\OneDrive\Área de Trabalho\PROJECTS\Pesquisa Agricola IBGE'
caminho_completo = diretorio + '\\Pesq_Agr_Mun_2020_2021.csv'

df = pd.read_csv(caminho_completo, sep=',')



# Importando a base cadastral de municipios
diretorio1 = r'C:\Users\digob\OneDrive\Área de Trabalho\PROJECTS\Pesquisa Agricola IBGE'
caminho_completo1 = diretorio1 + '\\base_cadastral_municipios_completa.xlsx'
df_cities = pd.read_excel(caminho_completo1)

# Renomear a coluna "cod_ibge" para "codigo_ibge"
df = df.rename(columns={'cod_ibge': 'codigo_ibge'})

##------------------------------------------------------------------------------------------------------------

# CLEANING DATA

##------------------------------------------------------------------------------------------------------------

#Extraindo texto da variavel cultura
extrair_codigo_cultura_lambda_simples = lambda cultura_str: cultura_str.split("'")[1]
extrair_nome_cultura_lambda_simples = lambda cultura_str: cultura_str.split("'")[3]

df['codigo_cultura'] = df['cultura'].apply(extrair_codigo_cultura_lambda_simples)
df['nome_cultura'] = df['cultura'].apply(extrair_nome_cultura_lambda_simples)

# 1. Eliminar a coluna "Unnamed: 0"
df = df.drop(columns=['Unnamed: 0','cultura'])

# Criando o DF completo dando MERGE nas bases

df_merge = pd.merge(df,df_cities,on='codigo_ibge',how='left')
df_merge.head(3)


##------------------------------------------------------------------------------------------------------------

# STREAMLIT WEBPAGE FILTERS 

##------------------------------------------------------------------------------------------------------------

df = df_merge

# Title
st.title("Análise de Dados Agrícolas - IBGE")

# # Streamlit Sidebar Filters
# st.sidebar.header("Filter Options")

# Radio Button Filter for Variavel
variavel_options = df[  'variavel'].unique()
selected_variavel = st.radio("Select Variável:", variavel_options)

# Checkbox for Regions
regiao_options = df['Nome_Regiao'].unique()
selected_regioes = st.multiselect("Select Region(s):", regiao_options, default=regiao_options)


# # Multi-select for Nome ESTADOS
# estados_options = df['Sigla_UF'].unique()
# selected_estados= st.multiselect("Select Culture(s):", estados_options,default=estados_options)

# Multi-select for Nome Cultura
cultura_options = df['nome_cultura'].unique()
selected_culturas = st.multiselect("Select Culture(s):", cultura_options, default=cultura_options)

# Filter DataFrame
filtered_data = df[
    (df['variavel'] == selected_variavel) & 
    (df['Nome_Regiao'].isin(selected_regioes)) & 
    # (df['Sigla_UF'].isin(selected_estados)) & 
    (df['nome_cultura'].isin(selected_culturas))
]

# Display the DataFrame in Streamlit
st.write("shape:", filtered_data.shape)

# Display the DataFrame in Streamlit
st.write("Data from CSV:", filtered_data.head(50))


# ##------------------------------------------------------------------------------------------------------------

# # PAYMENT AND DOWNLOAD BUTTON

# ##------------------------------------------------------------------------------------------------------------


st.title("Apoie e Baixe seus Dados")
st.write("Clique no botão abaixo para apoiar e receber seus dados.")

if st.button("Apoiar e Baixar Dados"):
    # Simula o direcionamento para o Stripe e o processo de pagamento
    st.info("Redirecionando para o pagamento...")
    time.sleep(2)  # Simula o tempo de redirecionamento

    # Aqui, você normalmente integraria com a API do Stripe para processar o pagamento
    # Se o pagamento for bem-sucedido, você exibiria o link de download

    # Simula um pagamento bem-sucedido
    pagamento_bem_sucedido = True  # Mude para False para testar o cenário de falha

    if pagamento_bem_sucedido:
        st.success("Pagamento realizado com sucesso! Clique no link abaixo para baixar seus dados.")
        # st.markdown(f'<a href="{DOWNLOAD_URL}" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; border-radius: 5px;">Baixar Dados</a>', unsafe_allow_html=True)



        st.download_button(
            label="Baixar Dados Filtrados como CSV",
            data=filtered_data.to_csv(index=False).encode('utf-8'),
            file_name="dados_filtrados.csv",
            mime="text/csv",
            help="Clique para baixar o DataFrame filtrado em formato CSV."
                )

    else:
        st.error("Ocorreu um erro ao processar o pagamento. Por favor, tente novamente.")

    

