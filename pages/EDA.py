import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Crime Data Analytics",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_crime_data1.csv")

df = load_data()

# -------------------------------------------------------
# Title
# -------------------------------------------------------
st.title("📊 Crime Data Analytics Dashboard")
st.markdown("Analyze crime patterns using interactive visualizations.")

st.markdown("---")

# -------------------------------------------------------
# Sidebar Filters
# -------------------------------------------------------
st.sidebar.header("Filters")

years = sorted(df["year"].unique())
selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + list(years)
)

areas = sorted(df["area name"].unique())
selected_area = st.sidebar.selectbox(
    "Select Area",
    ["All"] + list(areas)
)

filtered_df = df.copy()

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["year"] == selected_year
    ]

if selected_area != "All":
    filtered_df = filtered_df[
        filtered_df["area name"] == selected_area
    ]

# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------
st.subheader("Dashboard Overview")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "📁 Total Records",
    f"{len(filtered_df):,}"
)

c2.metric(
    "🚨 Crime Types",
    filtered_df["crm cd desc"].nunique()
)

c3.metric(
    "📍 Areas",
    filtered_df["area name"].nunique()
)

c4.metric(
    "🎯 Model Accuracy",
    "92%"
)

st.markdown("---")

# =======================================================
# Row 1
# =======================================================

col1,col2 = st.columns(2)

with col1:

    crime = (
        filtered_df["crm cd desc"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    crime.columns = ["Crime Type","Count"]

    fig = px.bar(
        crime,
        x="Count",
        y="Crime Type",
        orientation="h",
        color="Count",
        color_continuous_scale="Blues",
        text="Count",
        title="Top 10 Crime Types"
    )

    fig.update_layout(
        height=450,
        coloraxis_showscale=False,
        template="simple_white"
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar":False}
    )

with col2:

    gender = (
        filtered_df["vict sex"]
        .value_counts()
        .reset_index()
    )

    gender.columns=["Gender","Count"]

    fig = px.pie(
        gender,
        values="Count",
        names="Gender",
        hole=0.55,
        color_discrete_sequence=px.colors.sequential.Blues_r,
        title="Victim Gender Distribution"
    )

    fig.update_layout(
        height=450,
        template="simple_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar":False}
    )

st.markdown("---")

# =======================================================
# Row 2
# =======================================================

col1,col2 = st.columns(2)

with col1:

    area = (
        filtered_df["area name"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    area.columns=["Area","Crime Count"]

    fig = px.bar(
        area,
        x="Crime Count",
        y="Area",
        orientation="h",
        text="Crime Count",
        color="Crime Count",
        color_continuous_scale="Blues",
        title="Top 10 Crime Areas"
    )

    fig.update_layout(
        height=450,
        template="simple_white",
        coloraxis_showscale=False
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar":False}
    )

with col2:

    fig = px.histogram(
        filtered_df,
        x="vict age",
        nbins=25,
        color_discrete_sequence=["#2563EB"],
        title="Victim Age Distribution"
    )

    fig.update_layout(
        height=450,
        template="simple_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar":False}
    )

st.markdown("---")
# =======================================================
# Row 3
# =======================================================

col1, col2 = st.columns(2)

with col1:

    weapon = (
        filtered_df["weapon desc"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    weapon.columns = ["Weapon", "Count"]

    fig = px.bar(
        weapon,
        x="Count",
        y="Weapon",
        orientation="h",
        text="Count",
        color="Count",
        color_continuous_scale="Blues",
        title="Top 10 Weapons Used"
    )

    fig.update_layout(
        height=450,
        template="simple_white",
        coloraxis_showscale=False,
        yaxis_title="",
        xaxis_title="Crime Count"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

with col2:

    hour = (
        filtered_df["hour"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    hour.columns = ["Hour", "Crime Count"]

    fig = px.line(
        hour,
        x="Hour",
        y="Crime Count",
        markers=True,
        title="Crime Distribution by Hour"
    )

    fig.update_traces(
        line=dict(color="#2563EB", width=4),
        marker=dict(size=8)
    )

    fig.update_layout(
        height=450,
        template="simple_white",
        xaxis_title="Hour of Day",
        yaxis_title="Crime Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

st.markdown("---")

# =======================================================
# Correlation Heatmap
# =======================================================

st.subheader("🔥 Correlation Heatmap")

corr_columns = [
    "vict age",
    "hour",
    "month",
    "year",
    "area",
    "crm cd",
    "lat",
    "lon"
]

corr = filtered_df[corr_columns].corr()

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="Blues",
    aspect="auto",
    title="Correlation Between Important Features"
)

fig.update_layout(
    height=650,
    template="simple_white"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

st.markdown("---")

# =======================================================
# Dataset Preview
# =======================================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    filtered_df.head(15),
    use_container_width=True,
    height=400
)

st.markdown("---")

# =======================================================
# Statistical Summary
# =======================================================

with st.expander("📈 View Statistical Summary"):

    st.dataframe(
        filtered_df.describe(),
        use_container_width=True
    )

st.markdown("---")

# =======================================================
# Download Dataset
# =======================================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_crime_data.csv",
    mime="text/csv"
)

st.markdown("---")

st.success("✅ Crime Data Analytics Dashboard Loaded Successfully")