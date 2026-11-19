import streamlit as st

st.title("Cadastrar anime")

# Formulário com os dados do anime
with st.form("cadastro_anime"):
    nome = st.text_input("Nome do anime")
    genero = st.text_input("Gênero")
    status = st.selectbox(
        "Status",
        ["Quero assistir", "Assistindo", "Concluído"],
    )
    enviar = st.form_submit_button("Enviar")

# Validação e conferência dos dados enviados
if enviar:
    nome = nome.strip()
    genero = genero.strip()

    if nome and genero:
        st.success("Formulário enviado!")
        st.text(f"{nome} — {genero} — {status}")
    else:
        st.warning("Preencha o nome e o gênero do anime.")
