import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="NAVINFO")

# Função para carregar dados
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    tabela["Data"] = pd.to_datetime(tabela["Data"], format='%d/%m/%Y')
    return tabela

# Título e descrição
st.title("Exemplo de Dashboard")
st.subheader("Navinfo + Streamlit")
st.write("Informações sobre os contratos fechados pela XPTO ao longo de maio")

# Seleção de período e filtragem de dados
st.write("---")
qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
num_dias = int(qtde_dias.replace("D", ""))
dados = carregar_dados()

# Garantir que os dados estejam ordenados por data
dados = dados.sort_values(by="Data")

# Filtrar dados para o período selecionado
data_fim = dados["Data"].max()
data_inicio = data_fim - pd.Timedelta(days=num_dias)
dados_filtrados = dados[dados["Data"] >= data_inicio]

# Exibir gráfico
st.area_chart(dados_filtrados.set_index("Data")["Contratos"])

    
# Informações e links adicionais
st.write("Quer saber mais sobre o Fabiano? Veja os links abaixo:")
st.markdown(
    """
    - [Perfil do LinkedIn](https://www.linkedin.com/in/fabiano-de-navarro)
    - [Perfil na DIO](https://www.dio.me/users/nav_info_suporte)
    - [GitHub](https://github.com/Fabianonavarro)
    """
)
