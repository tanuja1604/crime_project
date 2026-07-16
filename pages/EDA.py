
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Crime Data Analytics",
    page_icon="📊",
    layout="wide"
)

sns.set_style("whitegrid")

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

c1, c2, c3, c4 = st.columns(4)

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
    "96.61%"
)

st.markdown("---")

# -------------------------------------------------------
# Plot Style
# -------------------------------------------------------
sns.set_style("darkgrid")

plt.rcParams.update({
    "figure.facecolor": "none",
    "axes.facecolor": "none",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "text.color": "white",
    "axes.titlecolor": "white",
    "grid.color": "gray",
    "font.size": 10
})

# =======================================================
# 1. Top 10 Crime Types
# =======================================================
st.subheader("Top 10 Crime Types")

fig, ax = plt.subplots(figsize=(8,4), facecolor="none")

sns.countplot(
    y="crm cd desc",
    data=filtered_df,
    order=filtered_df["crm cd desc"].value_counts().index[:10],
    color="#4C78A8",
    ax=ax
)

ax.set_title("Top 10 Crime Types", fontsize=14)
ax.set_xlabel("Count")
ax.set_ylabel("Crime Type")

# Remove grid
ax.grid(False)

# Remove white background
ax.set_facecolor("none")
fig.patch.set_alpha(0)

sns.despine(left=True, bottom=True)

st.pyplot(fig)

# -------------------------------------------------------
# Victim Gender Distribution
# -------------------------------------------------------

st.subheader("Victim Gender Distribution")

gender = filtered_df["vict sex"].value_counts()

fig, ax = plt.subplots(figsize=(5,5))

fig.patch.set_alpha(0)
ax.set_facecolor("none")

ax.pie(
    gender,
    labels=gender.index,
    autopct="%1.1f%%",
    startangle=90,
    textprops={"fontsize":10},
    wedgeprops=dict(edgecolor="white", linewidth=2)
)

ax.set_title(
    "Victim Gender Distribution",
    fontsize=14,
    fontweight="bold"
)

left, center, right = st.columns([1,2,1])

with center:
    st.pyplot(fig)

plt.close(fig)
# =======================================================
# 3. Top 10 Crime Areas
# =======================================================

st.subheader("Top 10 Crime Areas")

fig, ax = plt.subplots(figsize=(8,4), facecolor="none")

sns.countplot(
    y="area name",
    data=filtered_df,
    order=filtered_df["area name"].value_counts().index[:10],
    color="#4C78A8",
    ax=ax
)

ax.set_title("Top 10 Crime Areas", fontsize=14)
ax.set_xlabel("Count")
ax.set_ylabel("Area")

ax.grid(False)

ax.set_facecolor("none")
fig.patch.set_alpha(0)

sns.despine(left=True, bottom=True)

st.pyplot(fig)

# =======================================================
# 4. Victim Age Distribution
# =======================================================

st.subheader("Victim Age Distribution")

fig, ax = plt.subplots(figsize=(8,4), facecolor="none")

sns.histplot(
    filtered_df["vict age"],
    bins=25,
    color="#4C78A8",
    ax=ax
)

ax.set_title("Victim Age Distribution", fontsize=14)
ax.set_xlabel("Victim Age")
ax.set_ylabel("Frequency")

ax.grid(False)

ax.set_facecolor("none")
fig.patch.set_alpha(0)

sns.despine(left=True, bottom=True)

st.pyplot(fig)
# =======================================================
# 5. Correlation Heatmap
# =======================================================

st.subheader("Correlation Heatmap")

corr_columns = [
    "dr_no",
    "area",
    "rpt dist no",
    "part 1-2",
    "crm cd",
    "vict age",
    "premis cd",
    "weapon used cd",
    "lat",
    "lon",
    "year",
    "month",
    "weekday",
    "hour",
    "is_weekend",
    "area_crime_count"
]

corr = filtered_df[corr_columns].corr()

fig, ax = plt.subplots(figsize=(9,6), facecolor="none")

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="viridis",
    linewidths=0.3,
    square=True,
    cbar=True,
    annot_kws={"size":8},
    ax=ax
)

ax.set_title("Correlation Heatmap", fontsize=14)

ax.set_facecolor("none")
fig.patch.set_alpha(0)

st.pyplot(fig)

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

st.subheader("📈 Statistical Summary")

st.dataframe(
    filtered_df.describe(),
    use_container_width=True
)

st.markdown("---")

# =======================================================
# Missing Values
# =======================================================

st.subheader("🧹 Missing Values")

missing = filtered_df.isnull().sum()

missing = missing[missing > 0]

if len(missing) == 0:
    st.success("✅ No Missing Values Found")
else:
    st.dataframe(missing)

st.markdown("---")

# =======================================================
# Dataset Information
# =======================================================

st.subheader("📌 Dataset Information")

c1, c2 = st.columns(2)

with c1:
    st.info(f"""
Rows : {filtered_df.shape[0]}

Columns : {filtered_df.shape[1]}

Duplicate Records : {filtered_df.duplicated().sum()}
""")

with c2:
    st.info(f"""
Unique Crime Types : {filtered_df['crm cd desc'].nunique()}

Unique Areas : {filtered_df['area name'].nunique()}

Year Range : {filtered_df['year'].min()} - {filtered_df['year'].max()}
""")

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