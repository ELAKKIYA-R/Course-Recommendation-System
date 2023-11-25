# Fetch the neccesary python modules
import streamlit as st
import pickle
import pandas as pd

# Recommend movies based on content
def recommend(course):
    course_index = courses[courses['Course Name'] == course].index[0]
    distances = similarity[course_index]
    courses_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_courses = []

    # Fetch the posters for each recommended movie
    for  i in courses_list:
        #course_id = courses.iloc[i[0]].id
        recommended_courses.append(courses.iloc[i[0]].original_title)

    return recommended_courses

# Load the necessary python pickle files
courses_dict = pickle.load(open('course_dict.pkl','rb'))
courses = pd.DataFrame(courses_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Web app's hero section - Display Title, Dropdown
st.title("Course Recommender System")

selected_course_name = st.selectbox(
'Select a course to recommend',
courses['Course Name'].values)

# Output recommendations with posters
if st.button('Recommend'):
    name = recommend(selected_course_name)
 
    col1, col2, col3, col4,  col5 = st.columns(5)
    with col1:
        st.text(name[0])
    with col2:
        st.text(name[1])
    with col3:
        st.text(name[2])
    with col4:
        st.text(name[3])
    with col5:
        st.text(name[4])
