# Fetch the neccesary python modules
import streamlit as st
import pickle
import pandas as pd

# Recommend courses based on the cosine similarity score of the course selected by the user
def recommend(course):
    course_index = courses[courses['Course Name'] == course].index[0]
    distances = similarity[course_index]
    courses_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_courses = []

    for  i in courses_list:
        recommended_courses.append(courses.iloc[i[0]]['Course Name'])

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

# Output recommendations
if st.button('Recommend'):
    recommended_courses = recommend(selected_course_name)
 
    # Display recommended courses as separate lines
    for course in recommended_courses:
        st.write(course)