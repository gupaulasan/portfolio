import streamlit as st

st.title("Check my CV")
pt, en = st.columns(2)
pt.markdown(
    """
    ## Portuguese
    
    Para a versão em português do meu currículo, clique abaixo.
    """
)

pt.link_button(
    label="Acesse meu currículo",
    url="https://drive.google.com/file/d/1e_i0SGpTwDJd_wAIVymFiItSIOHOhZ38/view?usp=sharing",
    type="primary",
    help="Fique à vontade para fazer o download do arquivo",
    use_container_width=False,
)
en.markdown(
    """
    ## English
    
    For the English version click the button below.
    """
)
en.link_button(
    label="Access my CV",
    url="https://drive.google.com/file/d/1Xo1CZjjbWUoiCQyoQ-NGl9Wp212CS7AA/view?usp=drive_link",
    type="primary",
    help="Feel free to download the file",
)
