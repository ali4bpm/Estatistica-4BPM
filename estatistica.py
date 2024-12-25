import streamlit as st
import pandas as pd
import gspread 
from oauth2client.service_account import ServiceAccountCredentials


st.set_page_config(page_title="Estatística 4º BPM", page_icon = "Images/brasao.jpg", layout="wide")

st.title("ESTATÍSTICA BATALHÃO POTENGI")
st.subheader("4º BPM PMRN")
st.caption("Servir e Proteger")
#st.markdown("---")
st.divider()

st.sidebar.image("IMAGES/brasao.jpg", caption="Batalhão Potengi",use_container_width=True)


@st.cache_data
def carregar_dados():
    # Configurações de autenticação 
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope) 
    client = gspread.authorize(creds) 
    #Abre a planilha 
    planilha = client.open_by_key("1NXJwjx48gKRIrTdiq1Bexy_s44ymJ0IjClG5_BZtfnc") 
    aba = planilha.worksheet("Ocorrência_Geral")# ou nome da aba desejada 
    #Lê dados da planilha 
    dados = aba.get_all_values() 
    df = pd.DataFrame(dados)
    #Retirando a primeira linha do df
    dfTratado = pd.DataFrame(dados[1:], columns=dados[0])
    df = dfTratado
    return df 
    #Exibe os dados no Streamlit 
df = carregar_dados()
df
