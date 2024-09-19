import streamlit as st
import pandas as pd
from time import sleep

COLUMN_0 = "Continentes e paises de residencia permanente"

def dashboard_goals() -> None:
    """
    Questão num.1: Explicação do Objetivo e Motivação
    """
    
    st.title("Bem-vindos ao,  :green-background[Rio de Janeiro!] ✈️")

    st.markdown("→ O objetivo do dashboard é mostrar a chegada mensal de turistas pelo Rio de Janeiro, por via Aérea, segundo continentes e países de residência permanente, [2019.](https://www.data.rio/documents/a6c6c3ff7d1947a99648494e0745046d/about)")

    st.markdown("↪ A motivação por trás da escolha dos dados é ver/mostrar os dados de turismo, de estrangeiros, no Rio de Janeiro. Com diferentes funcionalidades que facilitem a compreensão dos dados.")
    ##O objetivo do dashboard é mostrar a chegada mensal de turistas pelo Rio de Janeiro, por via Aérea, segundo continentes e países de residência permanente, entre 2006-2019

    check_box = st.checkbox("Mudar para fundo branco")

    colormap = {
        "white": "#FFFFFF",
        "black": "#31333F"
    }

    if check_box:
        st.markdown(f"""
        <style>
        /*Feito com ajuda de IA*/
        .stApp {{
            background-color: {colormap["white"]};
        }}
        * {{
        color: {colormap["black"]} !important;
        }}
        </style>
    """, unsafe_allow_html=True)

def upload_csv_file() -> bytes:
    """
    Questão num.2: Realizar Upload de Arquivo CSV
    """
    csv_file = st.file_uploader("Carregue um arquivo .csv", type=["csv"])
    return csv_file
    
@st.cache_data ## Não pode ser usado com widgets
def csv_file_to_dataframe(csv_file: bytes) -> pd.DataFrame:
    if csv_file is not None:
        df = pd.read_csv(csv_file)
        return df
    else:
        return None


def expander_show_dataframe(df: pd.DataFrame) -> None:
    with st.expander("Ver dados brutos"):
        if df is None:
            st.write("Carregue o arquivo.")
        else:
            st.dataframe(df)


def selection_box(df: pd.DataFrame) -> None:
    """
    Questão num.3,4 e 5
    """
    if 'selected_column' not in st.session_state: ## Feito com ajuda de IA
        st.session_state.selected_column = None
    
    check_box = st.checkbox("Filtrar, separadamente, pelos meses.")
    # if csv_file:
    #     file = csv_file
    if check_box:
        try:
            data = df
            list_columns = list(data.columns)
            list_columns.remove(COLUMN_0) ## Poderia usar para remover com o índice
            select_box = st.selectbox("", list_columns, index=list_columns.index(st.session_state.selected_column) if st.session_state.selected_column else 0) ## Feito com ajuda de IA
            with st.spinner("Filtrando dados..."):
                sleep(1)
                st.session_state.selected_column = select_box ## Feito com ajuda de IA
                st.dataframe(data[[COLUMN_0, select_box]])
                
                filtered_data_by_month = data[[COLUMN_0, select_box]]
                csv = filtered_data_by_month.to_csv(index=False)
                st.download_button(label="Baixar dados", data=csv, file_name="filtered_monthly_data.csv", mime="text/csv")
        except:
            st.write("Carregue o arquivo.")


def filter_by_continent(df: pd.DataFrame) -> None:
    """
    Questão num.3,4 e 5
    """
    check_box = st.checkbox("Filtrar, separadamente, pelos continentes:")
    if check_box:
        try:
            data = df
            if data is None:
                st.write("Carregue o arquivo.")
            else:
                continents_list = ["África", "América Central", "América do Norte", "América do Sul", "Ásia", "Europa", "Oceania", "Oriente Médio"]
                radio_box = st.radio("", continents_list)
                progress_bar = st.progress(0, text="Filtrando dados...")
                for counter in range(1,101):
                    sleep(0.01)
                    progress_bar.progress(counter)
                progress_bar.empty()
                st.dataframe(data[data[COLUMN_0] == radio_box])
                filtered_data_by_continent = data[data[COLUMN_0] == radio_box]
                csv = filtered_data_by_continent.to_csv(index=False)
                st.download_button(label="Baixar dados", data=csv, file_name="filtered_continent_data.csv", mime="text/csv")
        except:
            st.write("Carregue o arquivo.")