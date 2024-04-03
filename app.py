from pathlib import Path

import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Klein Baru"
PAGE_ICON = ":wave:"
NAME = "Klein Baru"
DESCRIPTION = """
B. Sc. Telecommunication and Information Engineering Student @ DeKUT.
"""
EMAIL = "emailKlein@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/watch?v=MFuwKl8CK1A",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com/Klein-Baru",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Resistor-color-code-Decoder": "https://github.com/Klein-Baru/Resistor-color-code-Decoder",
    "🏆 A-Topography-Recognition-and-Prediction-System-for-Hybrid-Vehicles": "https://github.com/Klein-Baru/A-Topography-Recognition-and-Prediction-System-for-Hybrid-Vehicles",
    "🏆 The-Ultimate-MATLAB-Challenge": "https://github.com/Klein-Baru/The-Ultimate-MATLAB-Challenge",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.header("🟡Klein Baru.")
    st.write("📌B. Sc. Telecommunications & Information Engineering.")
    st.write("📫",EMAIL)
    st.write("***⚡Learning and Developing Software!!***")
    st.write("🔥Python, ML, Data Science, Web dev.")
    data = st.button("Download files")
    if data:
        st.write("Downloading...if download fails, kindly call.")
    st.slider(label=" ", value=50, min_value=10, step=5, max_value=100)
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Full stack web developer ranging from front end development to deployment.
- ✔️ Good at extracting actionable insights from data.
- ✔️ Strong hands on experience and knowledge in Python.
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🗄️ Web development: Front-end, Back-end, Google Forms, Streamlit.
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: Streamlit, Matplotlib.
- 📚 Modeling: Logistic regression, linear regression, decision trees.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "Attachee | Data Science and Artificial Intelligence Lab-DeKUT.**")
st.write("02/2030.")
st.write(
    """
- ► Learnt AI/ML deployment using Streamlit.
- ► Worked on an IoT project that involved monitoring of river water-level thus flood control.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Personal Projects | Bedroom.**")
st.write("01/21 - 03/2024.")
st.write(
    """
- ► Build web apps using streamlit to solve local problems and for fun.
- ► Build ML apps to solve local problems
- ► Build an IoT and Embedded systems to recognize topography of the land for use in hybrid vehicles.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
