import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Dashboard")
st.markdown("Performance evaluation of the trained **Random Forest Classifier**.")
st.markdown("---")

# -----------------------------
# Model Information
# -----------------------------
st.subheader("🤖 Model Information")

col1, col2 = st.columns(2)

with col1:
    st.info("""
**Model Used:** Random Forest Classifier

**Problem Type:** Multi-Class Classification

**Target Variable:** Crime Category (Crime Code Description)
""")

with col2:
    st.info("""
**Dataset:** Los Angeles Crime Dataset

**Training Algorithm:** Ensemble Learning

**Framework:** Scikit-Learn
""")

st.markdown("---")

# -----------------------------
# Performance Metrics
# -----------------------------
accuracy = 92.87
precision = 92.49
recall = 92.87
f1 = 91.65

st.subheader("📊 Performance Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Accuracy", f"{accuracy}%")
c2.metric("Precision", f"{precision}%")
c3.metric("Recall", f"{recall}%")
c4.metric("F1 Score", f"{f1}%")

st.markdown("---")

# -----------------------------
# Performance Comparison Chart
# -----------------------------
st.subheader("📉 Performance Comparison")

metric_df = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Score": [accuracy, precision, recall, f1]
})

fig = px.bar(
    metric_df,
    x="Metric",
    y="Score",
    text="Score",
    color="Score",
    color_continuous_scale="Blues",
    height=450
)

fig.update_traces(
    texttemplate='%{text:.2f}%',
    textposition='outside'
)

fig.update_layout(
    template="simple_white",
    yaxis_title="Percentage (%)",
    xaxis_title="",
    coloraxis_showscale=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -----------------------------
# Model Summary
# -----------------------------
st.subheader("📝 Model Summary")

st.success(f"""
✅ The **Random Forest Classifier** achieved an overall **Accuracy of {accuracy:.2f}%**.

• **Accuracy:** {accuracy:.2f}%

• **Precision:** {precision:.2f}%

• **Recall:** {recall:.2f}%

• **F1 Score:** {f1:.2f}%

The model demonstrates excellent predictive performance and is suitable for
classifying crime categories with high reliability.
""")

st.markdown("---")

# -----------------------------
# Conclusion
# -----------------------------
st.subheader("📌 Conclusion")

st.write("""
The Random Forest Classifier successfully predicts crime categories using historical
crime data. The model achieved an accuracy of **92.87%**, indicating strong overall
performance. The high Precision, Recall, and F1 Score show that the model provides
balanced and reliable predictions, making it suitable for crime prediction and analysis.
""")