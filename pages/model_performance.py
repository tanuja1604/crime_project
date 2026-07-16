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

# ======================================================
# Model Information
# ======================================================

st.subheader("🤖 Model Information")

col1, col2 = st.columns(2)

with col1:
    st.info("""
**Model Used:** Random Forest Classifier

**Problem Type:** Multi-Class Classification

**Target Variable:** Crime Category (35 Most Frequent Crime Types)

**Number of Classes:** 35
""")

with col2:
    st.info("""
**Dataset:** Los Angeles Crime Dataset

**Algorithm:** Ensemble Learning

**Library:** Scikit-Learn

**Train-Test Split:** 80% Train | 20% Test
""")

st.markdown("---")

# ======================================================
# Performance Metrics
# ======================================================

accuracy = 96.61
precision = 96.65
recall = 96.61
f1 = 96.34

st.subheader("📊 Performance Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Accuracy", f"{accuracy:.2f}%")
c2.metric("Precision", f"{precision:.2f}%")
c3.metric("Recall", f"{recall:.2f}%")
c4.metric("F1 Score", f"{f1:.2f}%")

st.markdown("---")

# ======================================================
# Performance Comparison Chart
# ======================================================

st.subheader("📉 Performance Comparison")

metric_df = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Score": [
        accuracy,
        precision,
        recall,
        f1
    ]
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
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig.update_layout(
    template="simple_white",
    yaxis_title="Percentage (%)",
    xaxis_title="",
    coloraxis_showscale=False,
    yaxis=dict(range=[90, 100])
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ======================================================
# Evaluation Summary Table
# ======================================================

st.subheader("📋 Evaluation Summary")

table = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Value (%)": [
        accuracy,
        precision,
        recall,
        f1
    ]
})

st.dataframe(table, use_container_width=True)

st.markdown("---")

# ======================================================
# Model Summary
# ======================================================

st.subheader("📝 Model Summary")

st.success(f"""
The **Random Forest Classifier** achieved excellent performance on the crime dataset.

### Performance

- **Accuracy:** {accuracy:.2f}%
- **Precision:** {precision:.2f}%
- **Recall:** {recall:.2f}%
- **F1 Score:** {f1:.2f}%

The model predicts the **35 most frequent crime categories** and demonstrates strong predictive performance on unseen test data.
""")

st.markdown("---")

# ======================================================
# Why Random Forest?
# ======================================================

st.subheader("✅ Why Random Forest?")

st.write("""
- High prediction accuracy.
- Handles large datasets efficiently.
- Reduces overfitting by combining multiple Decision Trees.
- Works well with both numerical and categorical features.
- Robust to noisy data.
- Provides stable and reliable predictions.
""")

st.markdown("---")

# ======================================================
# Conclusion
# ======================================================

st.subheader("📌 Conclusion")

st.write(f"""
The Random Forest Classifier was trained using the **Los Angeles Crime Dataset** to predict the **35 most frequent crime categories**.

The model achieved:

- **Accuracy:** {accuracy:.2f}%
- **Precision:** {precision:.2f}%
- **Recall:** {recall:.2f}%
- **F1 Score:** {f1:.2f}%

These results indicate that the model generalizes well to unseen data and is suitable for crime category prediction and crime pattern analysis.
""")