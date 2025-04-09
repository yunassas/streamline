import streamlit as st

courses = [
    {"name": "Python Basics", "keywords": ["Python", "Programming"]},
    {"name": "Data Science Fundamentals", "keywords": ["Data Science", "Statistics"]},
    {"name": "Intro to Web Development", "keywords": ["Web Development", "JavaScript"]},
    {"name": "AI for beginners", "keywords": ["AI", "Machine Learning"]},
    {"name": "Java", "keywords": ["Programming", "OOP"]}
]

#recommendation system
def recommend_courses(interests):
    recommendations = []
    for course in courses:
        if any(interest.lower() in [k.lower() for k in course["keywords"]] for interest in interests):
            recommendations.append(course["name"])
    return recommendations

#streamlit interface
st.title("Course Recommendation System")

name = st.text_input("enter your name:")
interest_input = st.text_area("enter your interests (comma-separated):")

if st.button("get recommendations"):
    if name and interest_input:
        interests = [i.strip() for i in interest_input.split(",")]
        recommended = recommend_courses(interests)

        if recommended:
            st.success(f"recommended courses for {name}:")
            for course in recommended:
                st.write(f"- {course}")
        else:
            st.warning("no recommendations available")
    else:
        st.error("please enter both your name and interests")
