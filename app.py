import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyCxGtvCu4zeqqUVzAdgNuldr4zGujszm2U")
model = genai.GenerativeModel("gemini-2.0-flash")

def gerar_resposta_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

    # Interface para o usuário
    pergunta = st.text_area("Digite sua pergunta:")


# Interface para o usuário
pergunta = st.text_area("Digite sua pergunta:")

if st.button("Gerar Resposta"):
    if pergunta:
        with st.spinner("Gerando resposta..."):
            resposta = gerar_resposta_gemini(pergunta)
            st.write("**Resposta:**")
            st.write(resposta)
    else:
        st.warning("Por favor, digite uma pergunta.")
# Executar com: streamlit run app.py


