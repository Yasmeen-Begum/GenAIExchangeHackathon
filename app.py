import streamlit as st
import requests

st.set_page_config(page_title="Career Advisor", layout="wide")

# 🎓 Header
st.title("🎯 Personalized Career & Skills Advisor")
st.markdown("Empowering students with AI-driven guidance for the modern job market.")

# 📋 Student Profile Form
with st.form("student_profile"):
    name = st.text_input("Full Name")
    age = st.slider("Age", 14, 30)
    academic_stream = st.selectbox("Academic Stream", ["Science", "Commerce", "Arts", "Vocational"])
    academic_background = st.text_area("Academic Background (e.g., subjects, grades, projects)")
    interests = st.text_area("Your Interests (comma-separated)")
    location = st.text_input("City / Region")
    language = st.selectbox("Preferred Language", ["English", "Hindi", "Telugu", "Tamil", "Bengali"])
    submitted = st.form_submit_button("Submit Profile")

# 🚀 Trigger Agent Workflow
if submitted:
    st.info("Sending profile to orchestrator agent...")

    payload = {
        "name": name,
        "age": age,
        "stream": academic_stream,
        "background": academic_background,
        "interests": interests,
        "location": location,
        "language": language
    }

    # Replace with your orchestrator agent endpoint
    ORCHESTRATOR_URL = "https://your-cloud-run-url/orchestrator"

    try:
        response = requests.post(ORCHESTRATOR_URL, json=payload)
        result = response.json()

        # 🧭 Career Recommendations
        st.subheader("🧭 Recommended Career Paths")
        for career in result.get("careers", []):
            st.markdown(f"- **{career['title']}**: {career['reasoning']}")

        # 🧠 Skill Mapping
        st.subheader("🧠 Skill Mapping")
        for skill in result.get("skills", []):
            st.markdown(f"- **{skill['name']}** → Required for: {skill['career']}")

        # 🎓 Course & Certificate Suggestions
        st.subheader("🎓 Courses & Certifications")
        for cert in result.get("certifications", []):
            st.markdown(f"- **{cert['title']}** — [{cert['provider']}]({cert['link']})")

        # 📍 Location-Based Insights
        st.subheader("📍 Regional Opportunities")
        for loc in result.get("regional_insights", []):
            st.markdown(f"- **{loc['city']}**: {loc['opportunity']}")

    except Exception as e:
        st.error(f"Failed to connect to orchestrator agent: {e}")