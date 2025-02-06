import streamlit as st

st.title("Projects")

with st.container(border=True):
    st.header(
        "[Automatic Playlist Continuation](https://github.com/gupaulasan/playlist-continuation/tree/main)"
    )

    # TODO Figure a way to add images without sending them to github

    st.markdown(
        """
        Check the project on Github        
        
        <a href="https://github.com/gupaulasan/playlist-continuation/tree/main" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        
        #### Introduction
        This project was developed as part of a graduate course I took in uni.      
        It originated from a [RecSys challenge](https://research.atspotify.com/publications/recsys-challenge-2018-automatic-music-playlist-continuation/) and the solutions were based on best solution from the original challenge.
        
        The idea here was to create a program that acts in a similar way as the Spotify's Playlist Continuation feature.        
        Based on the tracks chosen by an user, the program should choose 5 possible tracks to be added to that same playlist.
        """
    )

    with st.expander("Show further description"):
        st.write(
            """
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
        )

    st.markdown(
        """
        #### Skills
        
        Here a list of skills I used in this project:
        
        """,
        True,
    )

    # TODO Add skills

with st.container(border=True):
    st.header("[Project template](Projects)")

    st.markdown(
        """
        Check the project on Github        
        
        <a href="Projects" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        
        #### Introduction
        *Small description of the project*
        """
    )

    with st.expander("Show further description"):
        st.write(
            """
            #### Solution
            *Describe some of the approaches you used in the solution*
            
            #### Training and testing
            You can check the way I loaded and split the data to train both models in the link below.
            """
        )

    st.markdown(
        """
        #### Skills
        
        Here a list of skills I used in this project:
        
        """,
        True,
    )
