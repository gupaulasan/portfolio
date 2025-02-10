import streamlit as st

st.title("Projects")


def project_container(
    title: str,
    url: str,
    intro: str,
    description: str,
    skills: str,
):
    """Sets a containered project description up."""
    with st.container(border=True):
        st.header(f"[{title}]({url})")

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
            """
        )

        with st.expander("Show further description"):
            st.write(description)

        st.markdown(
            f"""
            #### Skills
            
            Here a list of technical skills I used in this project:
            {skills}
            """,
            True,
        )


# PLAYLIST CONTINUATION
playlist_title = "Automatic Playlist Continuation"
playlist_url = "https://github.com/gupaulasan/playlist-continuation/tree/main"
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

playlist_skills = ""

project_container(
    playlist_title, playlist_url, playlist_intro, playlist_description, playlist_skills
)


credit_title = "Credit Scoring"
credit_url = "https://github.com/gupaulasan/credit-score"
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
            
            As this project was part of a technical challenge, all development and data exploration is located in a single Jupyter Notebook.
            
            """
credit_skills = ""

project_container(
    credit_title, credit_url, credit_intro, credit_description, credit_skills
)
