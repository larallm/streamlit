import streamlit as st
import google.generativeai as genai


st.title("Criador de Histórias Interativas com IA 📚")



nomeprotagonista = st.text_input("Digite o nome do protagonista:")


generoliterario = st.selectbox("Escolha uma opção para o gênero da história:", ["Fantasia", "Ficção Científica", "Mistério", "Aventura"])

localinicial = st.radio("Escolha o local inicial da história:",  ["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado",  "Uma nave espacial à deriva"])

frasedesafio = st.text_area("Frase de Efeito ou Desafio Inicial (opcional):",   placeholder="Ex: E de repente, tudo ficou escuro.")


if st.button(" Gerar Início da História"):
    if nomeprotagonista and generoliterario and localinicial:


        prompt = f"""
A partir do gênero literário escolhido crie o inicio da história '{generoliterario}' com um protagonista chamado '{nomeprotagonista}'.
A história se passa em '{localinicial}'. Adicione a frase no início: '{frasedesafio}'.
Cria a história a partir dessas informações
"""
        with st.spinner("Gerando história..."):


            genai.configure(api_key="AIzaSyDNAWSkFfjtNWO8UZMbSWxyY1ymdWO-fYs")
            model = genai.GenerativeModel("gemini-2.0-flash")


            try:
                response = model.generate_content(prompt)
                historia = response.text
                st.subheader("Gerador de história:")
                st.write(historia)
            except Exception as e:
                st.error(f"Erro ao gerar a história: {str(e)}")

    else:
        st.warning("ERROR")
