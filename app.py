import streamlit as st
import pandas as pd

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="AI Learning Platform",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------------
# SIDEBAR
# ----------------------------------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Dashboard",
        "Career Recommendation",
        "Quiz",
        "Progress Tracking"
    ]
)

# ----------------------------------
# HOME PAGE
# ----------------------------------
if menu == "Home":

    st.title("🎓 AI Learning & Career Development Platform")

    st.write(
        """
        This platform helps students and job seekers:

        ✅ Learn industry skills
        ✅ Get AI career recommendations
        ✅ Take quizzes
        ✅ Track progress
        ✅ Access educational resources
        """
    )

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        use_container_width=True
    )

# ----------------------------------
# DASHBOARD
# ----------------------------------
elif menu == "Dashboard":

    st.title("📊 Learning Dashboard")

    st.subheader("Your Progress")

    st.progress(70)
    st.bar_chart(df.set_index("Courses"))
