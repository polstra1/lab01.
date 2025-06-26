import streamlit as st
import info
import pandas as pd

# About me
def about_me_section():
    st.header("About me")
    st.image(info.profile_picture, width =200)
    st.write(info.about_me)
    st.write("---")
about_me_section()

# side bar links
def links_sections ():
    st.sidebar.header("Links")
    st.sidebar.text("I don't have linkedin silly me")
    linkedin_link=f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="Linkedin" width = "75" height ="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("I don't have github silly me")
    github_link=f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width = "65" height ="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("I do have an email do not email me")
    email_html=f'<a href="{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width = "75" height ="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_sections()

# edu
def edu_sections(education_data, course_data):
    st.header("Education")
    st.subheader(f"{education_data['Institution']}")
    st.write(f"Degree: {education_data['Degree']}")
    st.write(f"Graduation Date: {education_data['Graduation Date']}")
    st.write(f"GPA: {education_data['GPA']}")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True, # this is how you hide the index
        )
    st.write("---")
        

edu_sections(info.education_data, info.course_data)

# experience
def exper(experience_data):
    st.header("Professional Experience")
    for job_title, (job_discription,image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_discription:
            expander.write(bullet)
    st.write("---")
exper(info.experience_data)

# project
def project(projects_data):
    st.header("Project")
    for project_name, project_description in projects_data.items():
        expander=st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project(info.projects_data)

# skills
def skills(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percet in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill, '')}")
        st.progress(percet)
    st.subheader("spoken Languages")
    for spoken, pro in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken, '')}:{pro}")
    st.write("---")

skills(info.programming_data, info.spoken_data)

# actiavies
def act(leadership_data, act_data):
    st.header("Activities")
    tab1, tab2 =st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details,image)in leadership_data.items():
            expander=st.expander(f"{title}")
            expander.image(image,width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Sevices")
        for title, details in act_data.items():
            expander=st.expander(f"{title}")
            for bullets in details:
                expander.write(bullets)
    st.write("---")

act(info.leadership_data, info.activity_data)





    

