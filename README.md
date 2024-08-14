# 📊 Dashboard de Análise de Contratos

Bem-vindo ao Dashboard de Análise de Contratos! Este é um aplicativo interativo desenvolvido com [Streamlit](https://streamlit.io) para analisar contratos fechados pela XPTO. Explore os dados de forma intuitiva e visualize tendências ao longo do tempo.

## 🚀 Visão Geral

O dashboard permite ao usuário:
- 📅 Selecionar um período (7, 15, 21 ou 30 dias) para análise.
- 📈 Visualizar gráficos de área mostrando o número de contratos fechados ao longo do período selecionado.

## 🛠️ Requisitos

Para executar este aplicativo, você precisará das seguintes ferramentas:

- [Python 3.6+](https://www.python.org/downloads/) 🐍
- [Streamlit](https://streamlit.io) 📦
- [Pandas](https://pandas.pydata.org) 🧮

Instale as dependências usando o `pip`:

```bash
pip install streamlit pandas

📥 Como Executar
Clone o Repositório

Clone o repositório para seu ambiente local:

bash
Copiar código
git clone https://github.com/usuario/repo.git
cd repo
Prepare os Dados

Certifique-se de que o arquivo resultados.csv esteja no diretório do projeto. O arquivo deve conter as colunas Data e Contratos.

Execute o Aplicativo

No terminal, inicie o aplicativo com o seguinte comando:

bash
Copiar código
streamlit run analise_contratoxpto.py
Acesse o Aplicativo
ou execute o arquivo execute.bat

Abra um navegador e vá para http://localhost:8501 para visualizar o dashboard.

🗂️ Estrutura do Código
analise_contratoxpto.py: Arquivo principal do Streamlit que configura o layout e as funcionalidades do aplicativo.
resultados.csv: Arquivo CSV com os dados dos contratos, contendo as colunas Data e Contratos.
🎯 Funcionalidades
Seleção de Período: Selecione um período (7, 15, 21 ou 30 dias) para ajustar a visualização do gráfico.
Visualização: Gráfico de área mostrando o número de contratos fechados ao longo do período selecionado.
🌐 Links Adicionais
🔗 Perfil do LinkedIn do Desenvolvedor
💼 Perfil na DIO
🖥️ GitHub do Desenvolvedor
🤝 Contribuição
Se você deseja contribuir, faça um fork e envie um pull request. Sugestões e correções são bem-vindas!

📝 Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

🆘 Suporte
Para dúvidas ou problemas, abra uma issue neste repositório ou entre em contato com o desenvolvedor através dos links fornecidos.
