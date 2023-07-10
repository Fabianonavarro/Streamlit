import streamlit as st
import pandas as pd

st.set_page_config(page_title="NAVINFO")

with st.container():
    st.subheader("NAvinfo + Streamlit")
    st.title("Exemplo de Dashboard")

    st.write("Informações sobre os contratos fechados pela XPTO ao longo de maio")

    st.write("Quer Saber mais sobre o Fabiano ? [Clique aqui](https://www.linkedin.com/in/fabiano-de-navarro)")
    st.write("--------------------------------------"

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")

