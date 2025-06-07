import streamlit as st
import google.generativeai as genai

api_key = st.secrets["API_KEY"]

genai.configure(api_key="AIzaSyCxGtvCu4zeqqUVzAdgNuldr4zGujszm2U")

model = genai.GenerativeModel("gemini-2.0-flash")

try:
    # Utilizando o modelo especificado
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    st.error(f"Erro ao carregar o modelo Gemini 'gemini-2.0-flash': {e}")
    st.info("Verifique se o nome do modelo está correto e se sua chave API tem acesso a ele.")
    st.stop()

def gerar_resposta_gemini(prompt_completo):
    try:
        response = model.generate_content(prompt_completo)

        if response.parts:
            return response.text
        else:
            if response.prompt_feedback:
                st.warning(f"O prompt foi bloqueado. Razão: {response.prompt_feedback.block_reason}")
                if response.prompt_feedback.safety_ratings:
                    for rating in response.prompt_feedback.safety_ratings:
                        st.caption(f"Categoria: {rating.category}, Probabilidade: {rating.probability}")
            return "A IA não pôde gerar uma resposta para este prompt. Verifique as mensagens acima ou tente reformular seu pedido."
    except Exception as e:
        st.error(f"Erro ao gerar resposta da IA: {str(e)}")
        if hasattr(e, 'message'): # Tenta obter mais detalhes do erro da API do Gemini
            st.error(f"Detalhe da API Gemini: {e.message}")
        return None
    
    ################## EXERCICIO 1 #######################
    
st.title(" Gerador de Início de História com IA")
st.markdown("Preencha os dados abaixo e deixe a IA criar um começo épico para sua história!")


nome_protagonista = st.text_input(" Nome do Protagonista")

genero = st.selectbox(" Gênero Literário", ["Fantasia", "Ficção Científica", "Mistério", "Aventura"])

local = st.radio(" Local Inicial da História", [
    "Uma floresta antiga",
    "Uma cidade futurista",
    "Um castelo assombrado",
    "Uma nave espacial à deriva"
])


frase_desafio = st.text_area(" Frase de Efeito ou Desafio Inicial", placeholder="Ex: E de repente, tudo ficou escuro.")


if st.button(" Gerar Início da História"):
    if not nome_protagonista.strip():
        st.warning("Por favor, digite o nome do protagonista.")
    elif not frase_desafio.strip():
        st.warning("Por favor, escreva uma frase de efeito ou desafio.")
    else:
        
        prompt_usuario = (
            f"Crie o início de uma história de gênero '{genero}', com um ou dois parágrafos. "
            f"O protagonista se chama '{nome_protagonista}'. "
            f"A história deve começar em '{local}' e incluir a seguinte frase: \"{frase_desafio}\". "
            f"Use um tom envolvente, criativo e que capture a atenção do leitor logo no começo."
        )

        st.markdown("---")
        st.markdown(" **Prompt enviado para a IA:**")
        st.text_area("", prompt_usuario, height=200)
        st.markdown("---")

        st.info("A IA está criando o início da história...")
        resposta_ia = gerar_resposta_gemini(prompt_usuario)

        if resposta_ia:
            st.markdown("###  Início da História:")
            st.markdown(resposta_ia)
        else:
            st.error("Não foi possível gerar a história. Tente novamente.")


# ##############################  EXERCICIO 2 ##############################################
# st.title("Gerador de Receitas Culinárias Personalizadas com IA ")
# st.markdown("Este aplicativo ajudará os usuários a gerar ideias de receitas com base em ingredientes disponíveis, tipo de culinária e restrições")



#ingredientes = st.text_area("Ingredientes Principais", placeholder='ex: frango, tomate, cebola, arroz')


# tipo_Culinaria= st.selectbox(
#    "Qual o tipo de culinária desejada?",
#   ["Italiana", "Brasileira", "Asiática", "Mexicana", "Qualquer uma"]
#)

#nivel_dificuldade = st.slider("🎚️ Nível de Dificuldade (1 = Muito Fácil, 5 = Desafiador)", min_value=1, max_value=5, value=3)

#restricao_Alimentar= st.checkbox("Possui Restrição Alimentar?")
#restricao=""
#if restricao_Alimentar:
#    restricao = st.text_input("Digite a restrição:",  placeholder="Ex: sem glúten, vegetariana, sem lactose")




#if st.button("Sugerir Receita"):
#    if not ingredientes:
#        st.warning("Por favor, informe os ingredientes principais.")
#    
#    else:
#       restricao_str = f"Considere também a seguinte restrição alimentar: {restricao}." if restricao_Alimentar and restricao else ""

#        prompt_aluno = (
#            f"Sugira uma receita {tipo_Culinaria} com nível de dificuldade {nivel_dificuldade} "
#            f"(sendo 1 muito fácil e 5 desafiador). Deve usar principalmente os seguintes ingredientes: "
#           f"'{ingredientes}'. {restricao_str} Apresente o nome da receita, uma lista de ingredientes adicionais "
#            f"se necessário, e um breve passo a passo do preparo."
#        )

#        st.markdown("---")
#        st.markdown("⚙️ **Prompt que será enviado para a IA (para fins de aprendizado):**")
#        st.text_area("",prompt_aluno, height=250)
#        st.markdown("---")
#
#        st.info("Aguarde, a IA está montando seu roteiro dos sonhos...")
#        resposta_ia = gerar_resposta_gemini(prompt_aluno)

#        if resposta_ia:
#            st.markdown("### ✨ Receita sugerida pela IA:")
 #           st.markdown(resposta_ia)
#        else:
#            st.error("Não foi possível gerar a receita. Verifique as mensagens acima ou tente novamente mais tarde.")
# Executar com: streamlit run app.py


