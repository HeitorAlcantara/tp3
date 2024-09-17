import streamlit as st
import pandas as pd

def dashboard_goals() -> None:
    """
    Questão num.1: Explicação do Objetivo e Motivação:
    """
    st.title("Bem-vindos ao,  :green-background[Rio de Janeiro!] ✈️")

    st.markdown("→ O objetivo do dashboard é mostrar a chegada mensal de turistas pelo Rio de Janeiro, por via Aérea, segundo continentes e países de residência permanente, [2019.](https://www.data.rio/documents/a6c6c3ff7d1947a99648494e0745046d/about)")

    st.markdown("↪ A motivação por trás da escolha dos dados é ver/mostrar os dados de turismo, de estrangeiros, no Rio de Janeiro. Com diferentes funcionalidades que facilitem a compreensão dos dados.")
    ##O objetivo do dashboard é mostrar a chegada mensal de turistas pelo Rio de Janeiro, por via Aérea, segundo continentes e países de residência permanente, entre 2006-2019


def upload_csv_file() -> None:
    """
    Questão num.2: Realizar Upload de Arquivo CSV:
    """
    csv_file = st.file_uploader("Carregue um arquivo .csv", type=["csv"])
    button = st.button("Click")
    try:
        if button:
            details = {
                "File Name": csv_file.name,
                "File Size": csv_file.size
            }
            st.write(details)
            df = pd.read_csv(csv_file)
            st.dataframe(df)
    except AttributeError as e: ## Feito com ajuda da IA.
        st.write(f"Error: {str(e)}")
