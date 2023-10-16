import streamlit as st
from cliente import Cliente
from vslz import Visu
import pandas as pd

class IndexUI:
    def main():
       st.header("Cadastro de Clientes")
       lst, ins, att, exc = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

       with lst:    
        st.header("Listar")
        df = pd.DataFrame(Visu.ClienteListar())
        st.dataframe(df, width=1000, hide_index=True)
        Visu.ClienteListar()

       with ins:
        st.header("Inserir")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        fone = st.text_input("Telefone")
        if st.button("Inserir"):
          Visu.ClienteInserir(nome, email, fone)
          st.write("Cliente Inserido")

       with att:
        st.header("Atualizar")
        option_atualizar = st.selectbox('Atualizar cliente', (Visu.ClienteListarN()))
        if option_atualizar != None:
          nome = st.text_input("Informe o novo nome", value=option_atualizar.get_nome())
          email = st.text_input("Informe o novo e-mail", value=option_atualizar.get_email())
          fone = st.text_input("Informe o novo telefone", value=option_atualizar.get_fone())
          if st.button("Atualizar"):
            Visu.ClienteAtualizar(option_atualizar.get_id(), nome, email, fone)
            st.write("Cliente atualizado")

       with exc:
        st.header("Excluir")
        option_excluir = st.selectbox('Excluir cliente', (Visu.ClienteListarN()))
        if option_excluir != None:
          if st.button("Excluir"):
            Visu.ClienteExcluir(option_excluir)
            st.write("Cliente excluído")
