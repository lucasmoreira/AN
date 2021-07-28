import streamlit as st


st.title('Transcrição de textos - Protótipo Dummy')

st.file_uploader('Enviar documento')

if not st.button('Processar'):
    st.stop()

st.image('./teste.png')

st.text('''Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy 
eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo 
dolores et ea rebum. Stet clita kasd gubergren, no sea takimata
 sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
 consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ''')




with st.beta_expander('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy'):
    texto = st.text_input("insira texto corrigido","Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy")
with st.beta_expander('eirmod tempor invidunt ut labore et dolore magna aliquyam erat, '):
    texto1 = st.text_input("insira texto corrigido","eirmod tempor invidunt ut labore et dolore magna aliquyam erat, ")
with st.beta_expander('sed diam voluptua. At vero eos et accusam et justo duo '):
    texto2 = st.text_input("insira texto corrigido","sed diam voluptua. At vero eos et accusam et justo duo ")
with st.beta_expander('dolor et ea rebum. Stet clita kasd gubergren, no sea takimata'):
    texto3 = st.text_input("insira texto corrigido","dolores et ea rebum. Stet clita kasd gubergren, no sea takimata")
with st.beta_expander('sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, '):
    texto4 = st.text_input("insira texto corrigido","sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet")
with st.beta_expander('consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt '):
    texto5 = st.text_input("insira texto corrigido","consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ")

st.button('Enviar')
