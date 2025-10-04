import streamlit as st

# ===============================
# 🎨 PAGE CONFIGURATION
# ===============================
st.set_page_config(page_title="My Streamlit Resume", page_icon="💼", layout="wide")

# ===============================
# 💼 RESUME SECTION
# ===============================
st.title("💼 Wan Muhammad Hafiz Bin Wan Ibrahim's Resume")

# --- Profile and Contact Info ---
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/150", caption="Profile Picture", width=150)
with col2:
    st.header("Contact Information")
    st.write("📧 Email: hafiz@example.com")
    st.write("📞 Phone: +60 12-345 6789")
    st.write("🔗 LinkedIn: [linkedin.com/in/hafiz](https://linkedin.com/in/hafiz)")
    st.write("🏠 Location: Malaysia")

st.markdown("---")

# --- Education ---
st.header("🎓 Education")
st.write("**Bachelor of Information Technology (Software Engineering)**, Universiti Malaysia Kelantan (UMK)")
st.write("_Expected Graduation: 2025_")

# --- Work Experience ---
st.header("💻 Work Experience")
st.write("**Intern – Software Developer**, VHI Power Sdn. Bhd. (2024)")
st.write("- Assisted in developing a Flutter-based mobile app integrated with Firebase.")
st.write("- Collaborated with team members to improve app performance and UI design.")
st.write("- Conducted testing and bug fixing for internal management systems.")

# --- Skills ---
st.header("🛠 Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("- Python 🐍")
    st.markdown("- Streamlit 💻")
with col2:
    st.markdown("- Flutter 📱")
    st.markdown("- Firebase 🔥")
with col3:
    st.markdown("- Machine Learning 🤖")
    st.markdown("- Project Management 📊")

# --- Projects ---
st.header("🚀 Projects & Achievements")
st.markdown("""
**Wasteless App** – A food waste reduction platform connecting donors and NGOs.
- Developed using Flutter and Firebase.
- Won *Top 5 Innovation Award* at UMK TechFair 2024.

**Snake Detection System** – Real-time object detection using YOLOv8.
- Integrated with FlutterFlow for mobile notifications.
- Designed to enhance safety in rural environments.
""")

# --- Extra Info ---
st.header("📚 Additional Information")
st.markdown("""
- Languages: English, Malay  
- Interests: Teaching, AI Research, and Drawing ✏️  
- Dream Career: University Lecturer 🎓  
""")

# --- Footer ---
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit*")

