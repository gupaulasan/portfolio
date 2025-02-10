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
):
    """Sets a containered project description up."""
    with st.container(border=True):
        st.header(f"[{title}]({url})")

        st.image(image=img["url"], caption=img["caption"], width=350)

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
            st.write(description)

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
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)       
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
"""

project_container(
    playlist_title,
    playlist_url,
    playlist_img,
    playlist_intro,
    playlist_description,
    playlist_skills,
)


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
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)       
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
"""

project_container(
    credit_title,
    credit_url,
    credit_img,
    credit_intro,
    credit_description,
    credit_skills,
)
