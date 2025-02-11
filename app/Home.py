import streamlit as st

st.set_page_config(
    page_title="Gustavo Santos' Portfolio",
    layout="wide",
)


def home_page():
    """Def home page text"""
    st.title("Gustavo Santos' Portfolio")

    st.markdown(
        """
        ## Welcome to my portfolio!
        
        Here you will find the projects I developed during my journey to become a Data Scientist.
        
        This is a place to find out about the reasoning of each project, the tech I used in them and learn about my carrer path.
        
        ## How to navigate it?
        
        You can use the navigation bar displayed on every page. Here is what you will find in each pages:
        
        [**About me:**](About_me)  Learn about my past experiences, skills and motivation
        
        [**Projects**:](Projects)  Check some projects I developed and see my skills in action
        
        ## Contact me
        
        I will be very happy to receive messages addressing doubts and questions about any project I developed. Including this one.
        
        Feel free to contact me through my socials: 
        
        <a href="https://www.linkedin.com/in/gustavopsantos/" target="_blank">
        <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" data-canonical-src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" style="max-width: 100%;">
        </a>

        <a href="mailto:gupaulasan@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" data-canonical-src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" style="max-width: 100%;">
        </a>
        
        <a href="https://github.com/gupaulasan" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
        </a>
        
        """,
        unsafe_allow_html=True,
    )


pages = [
    st.Page(home_page, title="Home", icon=":material/home:"),
    st.Page("pages/1_About_me.py", title="About me", icon="😁"),
    st.Page("pages/2_Projects.py", title="Projects", icon="📁"),
    st.Page("pages/3_CV.py", title="Check my CV", icon="📄"),
]

current_page = st.navigation(pages=pages, position="hidden")

num_cols = max(len(pages) + 1, 8)

columns = st.columns(num_cols, vertical_alignment="bottom")

columns[0].write("**My portfolio**")

for col, page in zip(columns[1:], pages):
    col.page_link(page, icon=page.icon)

current_page.run()
