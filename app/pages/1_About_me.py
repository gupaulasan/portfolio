import streamlit as st

st.title("About me")

st.write("## Introduction")

img, text = st.columns([1, 3])

img.image(
    "./assets/me.jpg",
    use_container_width=True,
    caption="That's me!",
    output_format="PNG",
)

text.markdown(
    """ 
    Hi! My name is Gustavo Santos, I'm a Brazilian Data Scientist.
    
    I have a bachelor's degree in Materials Engineering, which helped me develop important skills that I use daily as a data scientist.     
    Due to the activities I participated in during my uni years, I have a large set of soft skills such as: leading, communication and scientific research.
    
    Since 2023, I have focused my efforts in learning and developing my data skills, studying majorly Python, SQL and machine learning.     
    As you can check in my <a href="Projects" target="_self">Projects</a> page, during the time I have been studying, I applied what I studied in practical projects.<br>
    
    I'm seeking an opportunity as Junior Data Scientist in a professional environment that values innovation and technical excellence.
    """,
    unsafe_allow_html=True,
)

st.write(
    """
    ---
    ## Skills
    """
)

hardskills, softskills = st.columns(2)

hardskills.write("##### Hard skills")
hardskills.progress(90, "Python for Data Science")
hardskills.progress(90, "Machine Learning")
hardskills.progress(80, "SQL")
hardskills.progress(80, "Git")
hardskills.progress(80, "Deep Learning")
hardskills.progress(30, "Google Cloud Platform")
hardskills.progress(15, "MLOps")

softskills.write("##### Soft skills")
softskills.progress(90, "Analytical Thinking")
softskills.progress(90, "Problem Solving")
softskills.progress(90, "Learnability")
softskills.progress(80, "Communication")
softskills.progress(80, "Leardership")
softskills.progress(70, "Agile Methodologies")
st.write(
    """
    ---
    ## Professional Experience
    """
)

st.markdown(
    """
    ##### [GAMA - Machine Learning & Applications Research Group](https://gama.ufsc.br/)
    **Intern Data Scientist | January 2024 - December 2024**
    
    - I developed and monitored unsupervised machine learning models (in Scikit-Learn), majorly clustering,
    for identifying operational modes of industrial assets. This action resulted in the correction of 20% of past
    reports.
    
    - I created a statistical model for outlier identification in time series, increasing performance by 3.5%
    compared to the previous model.
    
    - I developed a visualization platform for error analysis using Dash and Plotly.
    
    - I used feature engineering that resulted in a 10% increase on model performance.
    
    - I conducted exploratory data analysis and data wrangling using Pandas, Numpy and Matplotlib.
    
    - I used git to version control my code.
    
    ##### [SCiTec - Materials Testing Laboratory](https://scitec.com.br/en/)
    **Intern | August 2022 - January 2023**
    - I processed and analyzed experimental data using Excel.
    - I prepared technical reports for clients.
    - I consolidated spreadsheets for data treatment based on technical procedures.
    
    ##### EJEM (Materials Engineering Junior Enterprise)
    **Executive Director and Project Manager | January 2021 – July 2022**
    - Improvement of on-time delivery rate from 75% to 100% by applying agile methodologies in project management.
    - I directly led 3 team members and indirectly led 12 members.
    - I collaborated with the sales department to increase first-quarter revenue by 223%
    - I developed automatic project data extraction using Python.

    """,
    unsafe_allow_html=True,
)

st.write(
    """
    ---
    ## Education
    """
)

st.markdown(
    """
    ##### [Federal University of Santa Catarina (UFSC) - Brazil](https://en.ufsc.br/)
    **Bachelor's Degree in Materials Engineering | March 2019 – December/2024**
    
    - Cumulative GPA: 9.3/10
    - Bachelor's thesis title: Implementation and Parameter Estimation of a Sintering Prediction Model in Python
    
    ##### Datacamp Certification
    **Data Science Associate**
    
    - Valid through March 2025
    
    - Access the [link](https://www.datacamp.com/certificate/DSA0013508028257) for more detail
    """,
    unsafe_allow_html=True,
)

st.write(
    """
    ---
    ## Volunteering
    """
)

st.markdown(
    """
    ##### [Omdena](https://www.omdena.com/)
    **Volunteer Data Scientist | January 2025 - current**
    
    - **Project:** AI-Assisted Sign Language Translation for Deaf Patients in Brazilian Healthcare Settings [[link]](https://www.omdena.com/chapter-challenges/ai-assisted-sign-language-translation-for-brazilian-healthcare-settings)
    
    ##### [Children International Summer Village (CISV)](https://cisv.org/)
    **Volunteer | January 2012 - March 2019**
    
    - NGO that works towards education for a more diverse, sustainable, just and peaceful world.
    - During one of my experiences, I worked with 48 children from 12 countries.
    - I acted as a communication link between adults (21+) and children (11).
     
    """
)

st.markdown(
    """
    ---
    ## Contact me
    
    <a href="https://www.linkedin.com/in/gustavopsantos/" target="_blank">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" data-canonical-src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" style="max-width: 100%;">
    </a>

    <a href="mailto:gupaulasan@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" data-canonical-src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" style="max-width: 100%;">
    </a>
    
    <a href="https://github.com/gupaulasan" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
    </a>
    """,
    True,
)
