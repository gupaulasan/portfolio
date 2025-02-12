import streamlit as st

st.title("Projects")

st.write("Here's a brief description of some projects I've developed along the way.")


def project_container(
    title: str,
    url: str,
    img: dict,
    intro: str,
    description: str,
    skills: str,
    show_gh: bool = True,
):
    """Sets a containered project description up."""
    with st.container(border=True):
        st.header(f"[{title}]({url})")

        st.image(image=img["url"], caption=img["caption"], width=350)

        if show_gh:
            st.markdown(
                f"""
                Check the project on Github
                
                <a href="{url}" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
                </a>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            
            #### Introduction
            {intro}
            """,
            unsafe_allow_html=True,
        )

        with st.expander("Show further description"):
            st.markdown(description, unsafe_allow_html=True)

        st.markdown(
            """
            #### Skills
            
            Here a list of technical skills I used in this project:
            """,
            unsafe_allow_html=True,
        )

        st.markdown(skills, unsafe_allow_html=True)


# PLAYLIST CONTINUATION
playlist_title = "Automatic Playlist Continuation"
playlist_url = "https://github.com/gupaulasan/playlist-continuation/tree/main"

playlist_img = {
    "url": "https://images.unsplash.com/photo-1504509546545-e000b4a62425?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "caption": "📷 Heidi Fin",
}
playlist_intro = """
        This project was developed as part of a graduate course I took in uni.      
        It originated from a [RecSys challenge](https://research.atspotify.com/publications/recsys-challenge-2018-automatic-music-playlist-continuation/) and the solutions were based on best solution from the original challenge.
        
        The idea here was to create a program that acts in a similar way as the Spotify's Playlist Continuation feature.        
        Based on the tracks chosen by an user, the program should choose 5 possible tracks to be added to that same playlist.
        """

playlist_description = """
            #### Solution
            Based on the problem set, I chose, as baseline, an approach that used collaborative filtering for the task.     
            However, due to the lack of performance from the approach above, I decided to try a Denoising Autoencoder approach.
        
            ###### Collaborative filtering
        
            Collaborative filtering is based on learning about one's likes and dislikes based on objects with similar habits.     
            For example, recommending a movie to you because someone that, usually, likes the same movies you do gave it 5 stars.
            
            In the context of playlist continuation a person would be a playlist, the movie would be the tracks and the score would be either 1 (if the track is in the playlist) and 0 (if the track is absent from the playlist).
            
            ###### Denoising autoencoder (DAE)
            
            DAEs work by trying to remove noise from an input.      
            In this context, the noise would be removing random tracks from playlists and showing the complete playlist as expected output.
            
            #### Training and testing
            *You can check the way I loaded and split the data to train both models in the link below.*
            """

playlist_skills = """
- Python
- Pandas
- NumPy
- Scikit-Learn
- Keras
- Recommender Systems
"""

project_container(
    title=playlist_title,
    url=playlist_url,
    img=playlist_img,
    intro=playlist_intro,
    description=playlist_description,
    skills=playlist_skills,
)

# Credit scoring
credit_title = "Credit Scoring"
credit_url = "https://github.com/gupaulasan/credit-score"

credit_img = {
    "url": "https://images.unsplash.com/photo-1628527304948-06157ee3c8a6?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "caption": "📷 Towfiqu barbhuiya",
}
credit_intro = """
        The idea of this project was to train a model that could predict the risk of a credit transaction, based a transactions history.        
        Every transaction should receive a score between 0 and 1, 0 representing a higher chance of financial loss.
        
"""
credit_description = """
            #### Solution
            
            For this project, I trained classifiers and compared their perfomances.     
            I used the outuput probabilities of models as credit score.     
            Due to this approach, all the models were comapred using a 0.5 proba threshold for class definition.
            
            #### Data
            
            The data used in this project consists of multiple tables containing different information about the clients and transactions.      
            In order to develop the solution, some feature engineering was necessary.
            
            #### Repo structure
            
            This project was part of a technical challenge. Because of that, all development and data exploration is located in a single Jupyter Notebook.
            
            """
credit_skills = """
- Python
- Pandas
- Numpy
- Matplotlib
- Scikit-learn
- Risk prediction
"""
project_container(
    title=credit_title,
    url=credit_url,
    img=credit_img,
    intro=credit_intro,
    description=credit_description,
    skills=credit_skills,
)

# Dynamox clustering
dyna_title = "Automatic Operational Mode Identification"
dyna_url = "https://gama.ufsc.br/projetos/#:~:text=Projetos%20Ativos-,Detec%C3%A7%C3%A3o%20e%20diagn%C3%B3stico%20de%20falhas%20em%20ativos%20industriais,-O%20projeto%20tem"
dyna_img = {
    "url": "https://gama.ufsc.br/images/projetos/detect_e_diagnos.png",
    "caption": "",
}
dyna_intro = """
        ***Disclaimer**: This project was developed in a closed source environment, for that reason, only the main idea and results are being described*
        
        The main idea of this project was to automatically identify and group signals using machine learning. Signals should be grouped into 'Operational Mode' groups.     
        After the grouping phase, experts would label some of the samples in each group so that the label could be propagated to all the other samples in the group.
        
"""
dyna_description = """
        #### Solution
        
        Based on the scope of the project, a clustering approach was used.      
        As a way to make the performance of the clustering techniques better, some feature engineering was performed. For legal reasons, the feature extraction part will not be further described
        
        #### Data
        
        The data used in this project were the responses from vibration sensors installed in industrial environments.
        
        #### Results
        
        The final product of the project was a <a href='https://dash.plotly.com/'>Dash</a> app in which experts can analyse and label the data.        
        This clustering method allowed the team to correct 20% of past reports, indirectly allowing the supervised model to perform better. 
"""

dyna_skills = """
    - Python
    - Numpy
    - Pandas
    - Scikit-learn
    - Dash
    - Plotly
    - Unsupervised learning
"""

project_container(
    title=dyna_title,
    url=dyna_url,
    img=dyna_img,
    intro=dyna_intro,
    description=dyna_description,
    skills=dyna_skills,
    show_gh=False,
)
