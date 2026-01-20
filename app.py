from turtle import width
from urllib import response
from certifi import contents
import streamlit as st
from pdfextractor import text_extractor
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# First Lets configure the model 
gemini_api_key = os.getenv('Google_API_KEY1')
model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key = gemini_api_key,
    temperature = 0.9
)

# Lets create the side bar to upload the resume 
st.sidebar.title(':orange[Upload Your Resume (Only PDF)]')
file = st.sidebar.file_uploader('Upload Your Resume',type=['pdf'])
if file:
    file_text = text_extractor(file)
    st.sidebar.success('File Uploaded Successfully')

# Lets create the main page of the application

st.set_page_config(page_title="SkillMatch", page_icon="🧠")

st.title(":blue[SkillMatch] – :orange[AI Assisted Skill Matching Tool]")

st.markdown('##### This Applicaation will watch and analyze your resume and your job description that you have provided.',width=
            'content')

tips = '''
Follow these Steps:

1. Upload your resume(PDF Only) in side bar.
2. Copy and paste the job Description below.
3. Click on submit to run the application.
'''

st.info(tips)

job_desc = st.text_area(':red[Copy and paste the job Description over here.]',max_chars=50000)

if st.button('SUBMIT'):
    prompt = f'''
    <Role> You are and expert in analyzing resume and matching it with job desciption.
    <Goal> Match the resume and the job description provided by the applicant.
    <Context> The following content has been provided by the applicant.
    * Resume : {file_text}
    * Job Description: {job_desc}
    <Format>The report should follow these steps :
    * Give a brief desciption the applicant in 3 to 5 lines.
    * Describe in percentage what are the chances of this resume getting selected.
    * Need not to be the exact percentage , you can give interval of percentage.
    * Give the expected ATS Score along with matching and non matching keywords.
    * Perform a SWAT analysisand explain each parameter that is , strength , weakness, Opportunity and Threat.
    * Give what all sections in the current resume that are required to be changed in order to improve the ATS Score and selection percentage.
    * Show both current version and improved version of the section in the resume.
    * Create two sample resume which can maximize the ATS score and selection percentage.

    <Instruction>
    * Use Bullet points for explanation where ever possible.
    * Create Tables for description where ever required.
    * Strictly do not add any new skill in sample resume.
    * The format of sample resume should be in such a way that they can be copied and pasted directly in word .
    '''

    response= model.invoke(prompt)
    st.write(response.content)