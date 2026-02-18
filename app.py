import streamlit as st
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="AI Smart Semester Planner", layout="wide")

st.title("🎓 AI SMART SEMESTER PLANNER SYSTEM")
st.markdown("Generate a smart study schedule based on subject difficulty.")

# Input Fields
name = st.text_input("Student Name")
semester = st.text_input("Semester")
subjects_text = st.text_input("Subjects (comma separated)")
difficulty_text = st.text_input("Difficulty per Subject (1-5, comma separated)")
free_hours_text = st.text_input("Free hours per day (number)")

if st.button("Generate Smart Plan"):

    if not name or not semester or not subjects_text or not difficulty_text or not free_hours_text:
        st.error("Please fill all fields.")
    else:
        try:
            free_hours = float(free_hours_text)
            subjects = [s.strip() for s in subjects_text.split(",")]
            difficulties = [int(d.strip()) for d in difficulty_text.split(",")]

            if len(subjects) != len(difficulties):
                st.error("Number of subjects and difficulty levels must match!")
            else:
                total_difficulty = sum(difficulties)

                st.success("Study Plan Generated Successfully!")

                st.subheader("📘 Smart Time Distribution")

                start_time = datetime.strptime("08:00", "%H:%M")

                for subject, difficulty in zip(subjects, difficulties):
                    allocated_time = (difficulty / total_difficulty) * free_hours
                    end_time = start_time + timedelta(hours=allocated_time)

                    st.write(f"**Subject:** {subject}")
                    st.write(f"Difficulty: {difficulty}/5")
                    st.write(f"Allocated Time: {round(allocated_time,2)} hrs")
                    st.write(f"Schedule: {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}")
                    st.markdown("---")

                    start_time = end_time

                st.markdown("### 👨‍💻 Developer Profile")
                st.write("Abdullah")
                st.write("Future AI Engineer")
                st.write("BS Student at Bacha Khan University")
                st.write("Specialized in AI-Based Academic Planning Systems")

        except:
            st.error("Please enter valid numbers for difficulty and free hours.")