import streamlit as st

st.set_page_config(page_title="About Project", page_icon="📖", layout="wide")

st.title("📖 About the Project")

st.markdown("---")

st.markdown("""
## 🚔 Crime Prediction System

The **Crime Prediction System** is a Machine Learning-based web application that predicts the **crime category** based on various crime-related attributes such as location, victim details, weapon information, crime status, and time of occurrence.

The objective of this project is to demonstrate how Machine Learning can assist law enforcement agencies and researchers in analyzing crime patterns and predicting possible crime types using historical crime data.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.success("""
### 💻 Technologies Used

- 🐍 Python
- 📊 Pandas
- 🔢 NumPy
- 🤖 Scikit-Learn
- 📈 Matplotlib
- 🎨 Seaborn
- 🌐 Streamlit
    """)

with col2:
    st.info("""
### 🤖 Machine Learning Model

- Random Forest Classifier

### 📊 Model Performance

- ✅ Accuracy : **92%**
- 📌 Classification Problem
- 📂 Trained on Historical Crime Dataset
    """)

st.markdown("---")

st.markdown("""
## ✨ Key Features

✅ Crime Category Prediction

✅ Interactive Dashboard

✅ Exploratory Data Analysis (EDA)

✅ Dataset Visualization

✅ Model Performance Evaluation

✅ User-Friendly Web Interface
""")

st.markdown("---")

st.markdown("""
## 🎯 Project Objective

The main objective of this project is to analyze historical crime data and predict the most likely crime category using Machine Learning techniques. This system helps in understanding crime trends and demonstrates the practical application of Artificial Intelligence in crime analytics.
""")

st.markdown("---")

st.markdown("""
## 👩‍💻 Developed By

**Tanuja Patil**

🎓 B.Tech Computer Science Engineering

📚 **Machine Learning • Python • Data Analysis • Power BI • Streamlit**

""")

st.markdown("---")

st.caption("© 2026 Crime Prediction System | Developed using Python & Streamlit")