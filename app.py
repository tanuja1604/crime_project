import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Crime Prediction System",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
    max-width:100%;
}

body{
    background-color:#0d1117;
}

.main-title{
    font-size:60px;
    font-weight:bold;
    color:white;
    text-align:center;
}

.sub-title{
    font-size:22px;
    text-align:center;
    color:white;
}

.banner{
    background:linear-gradient(90deg,#8B0000,#1C1C1C);
    padding:30px;
    border-radius:20px;
    box-shadow:0px 0px 20px rgba(255,0,0,0.4);
}

.card{
    background-color:#1f2937;
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
    font-size:20px;
    box-shadow:0px 0px 10px gray;
}

.footer{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Banner ----------------
st.markdown("""
<div class="banner">
    <div class="main-title">🚔 Crime Prediction System</div>
    <div class="sub-title">
        Predict Crime Types using Machine Learning & Data Analytics
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- Welcome ----------------
st.success("👋 Welcome! Use the sidebar to navigate through the project modules.")

st.write("")

# ---------------- Project Modules ----------------
st.markdown("## 📌 Project Modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        📂 <b>Dataset</b><br><br>
        View the crime dataset used for training.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card">
        📊 <b>EDA</b><br><br>
        Explore trends, charts and crime statistics.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        🤖 <b>Crime Prediction</b><br><br>
        Predict crime type using trained ML model.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card">
        📈 <b>Model Performance</b><br><br>
        View Accuracy, Precision, Recall and F1 Score.
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- About ----------------
st.info("""
### 👨‍💻 About Project

This project uses a **Random Forest Machine Learning model** trained on crime records to predict the probable crime type based on user inputs.

**Algorithm Used:** Random Forest Classifier

**Model Accuracy:** **92%**

Navigate through the sidebar to explore all project sections.
""")

# ---------------- Footer ----------------
st.markdown("""
<div class="footer">
🔍 Crime Prediction System | Final Year Computer Science Mini Project
</div>
""", unsafe_allow_html=True)