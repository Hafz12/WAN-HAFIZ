import streamlit as st

# ===============================
# 🎨 PAGE CONFIGURATION
# ===============================
st.set_page_config(page_title="My Streamlit Resume", page_icon="💼", layout="wide")

# ===============================
# 💼 RESUME SECTION
# ===============================
st.title("Wan Muhammad Hafiz Bin Wan Ibrahim")

# --- Profile and Contact Info ---
st.header("📞 Contact Information")

col1, col2 = st.columns([1, 3])  # Profile pic smaller, info wider

with col1:
    st.image(
        "WhatsApp_Image_2025-06-12_at_16.57.36_99ca5643-removebg-preview (1).png",
        caption="Profile Picture",
        width=150
    )

with col2:
    # Create a single horizontal row using st.columns()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("📧 **Email**")
        st.write("s22a0055@siswa.umk.edu.my")
    with c2:
        st.write("📞 **Phone**")
        st.write("+60 11-6379 8373")
    with c3:
        st.write("🏠 **Location**")
        st.write("Malaysia")

st.markdown("---")

# --- Education ---
st.header("🎓 Education")
st.write("**Bachelor of Information Technology (Hons)**, Universiti Malaysia Kelantan (2022 - 2026)")

st.write("**Matriculation of Negeri Sembilan**, Matriculation KPM Certificate (2020 - 2022)")
st.write("- CGPA: 3.38")

st.markdown("---")

# --- Skills ---
st.header("🛠 Skills")
st.subheader("Programming Languages")
st.markdown("- Python   \n- Java   \n- Dart (Flutter) ")

st.subheader("AI & Machine Learning")
st.markdown("- Object Detection  \n- Image Classification  \n- TensorFlow  \n- Google Colab")

st.subheader("Development Tools")
st.markdown("- Android Studio  \n- FlutterFlow  \n- Visual Studio Code")

st.subheader("Database & Backend")
st.markdown("- Firebase ")

st.markdown("---")

# --- Projects ---
st.header("🚀 Projects")
st.markdown("""
**Wasteless App** – A food waste reduction platform connecting donors and NGOs.  
- Developed using Flutter and Firebase.    

**Snake Detection System** – Real-time object detection using YOLOv8.  
- Integrated with FlutterFlow for mobile notifications.  
- Designed to enhance safety in rural environments.
""")

st.markdown("---")

# --- Achievements ---
st.header("🏅 Achievements & Competitions")
st.markdown("""
- 🧠 **Big Spark Competition 2024** – Participant 
- 🥇 **International Research and Information Science Expo 2025** – Gold Medal  
- 🦁 **Lion’s Lair Competition 2024** – Participant  
- 🥉 **Malaysia Techlympic 2023** – 3rd Place  
- 🧪 **Matriculation STEM Carnival 2021** – Bronze Medal  
""")

st.markdown("---")

# --- Additional Info ---
st.header("📚 Additional Information")
st.markdown("""
- Languages: English, Malay, Chinese(Beginner)
- Interests: AI Research, Planting and Drawing   
- Dream Career: -   
""")

# --- Footer ---
st.markdown("---")
