import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

sns.set_style("whitegrid")

st.set_page_config(
    page_title="FIFA Player Analysis",
    layout="wide"
)

# Load CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown('<h1 class="main-title">⚽ FIFA Player Analysis Dashboard</h1>', unsafe_allow_html=True)

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\ADMIN\Desktop\DATA SCIENCE NOTES\NOVEMBER MONTH\27TH NOV\25th, 26th- Advanced EDA project\25th, 26th- Advanced EDA project\Seaborn - SPORT\FIFA.csv")     # change path if needed

df = load_data()

# Convert to string to avoid TypeError
df['Position'] = df['Position'].astype(str)
df['Nationality'] = df['Nationality'].astype(str)
df['Club'] = df['Club'].astype(str)

# SIDEBAR FILTERS
st.sidebar.header("🔍 Player Filters")
show_raw = st.sidebar.checkbox("Show Raw Data", True)

position = st.sidebar.selectbox("Position", ["All"] + sorted(df['Position'].unique()))
nationality = st.sidebar.selectbox("Nationality", ["All"] + sorted(df['Nationality'].unique()))
club = st.sidebar.selectbox("Club", ["All"] + sorted(df['Club'].unique()))

age_range = st.sidebar.slider("Age Range", int(df["Age"].min()), int(df["Age"].max()), (int(df["Age"].min()), int(df["Age"].max())))
overall_range = st.sidebar.slider("Overall Rating Range", int(df["Overall"].min()), int(df["Overall"].max()), (int(df["Overall"].min()), int(df["Overall"].max())))

# APPLY FILTERS
filtered = df.copy()
if position != "All": filtered = filtered[filtered["Position"] == position]
if nationality != "All": filtered = filtered[filtered["Nationality"] == nationality]
if club != "All": filtered = filtered[filtered["Club"] == club]
filtered = filtered[
    (filtered["Age"].between(age_range[0], age_range[1])) &
    (filtered["Overall"].between(overall_range[0], overall_range[1]))
]

st.write(f"📌 Showing **{filtered.shape[0]} players** after filters")

# TABS
tab_overview, tab_uni, tab_bi, tab_corr, tab_team, tab_compare, tab_conclusion = st.tabs([
    "Overview", "Univariate", "Bivariate", "Correlation", "Best XI Team", "Compare Players", "Conclusion"
])

# -------------------- OVERVIEW TAB --------------------
with tab_overview:
    col1, col2, col3 = st.columns(3)
    col1.metric("Players", filtered.shape[0])
    col2.metric("Attributes", filtered.shape[1])
    col3.metric("Unique Nationalities", filtered['Nationality'].nunique())

    if show_raw:
        st.dataframe(filtered.head())

# -------------------- UNIVARIATE TAB --------------------
with tab_uni:
    c1, c2 = st.columns(2)

    with c1:
        fig, ax = plt.subplots()
        sns.histplot(filtered['Overall'], kde=True, bins=25, ax=ax)
        ax.set_title("Overall Rating Distribution")
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots()
        sns.histplot(filtered['Age'], kde=True, bins=25, ax=ax)
        ax.set_title("Age Distribution")
        st.pyplot(fig)

# -------------------- BIVARIATE TAB --------------------
with tab_bi:
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered, x="Age", y="Overall", hue="Position", ax=ax)
    ax.set_title("Age vs Overall Rating")
    st.pyplot(fig)

# -------------------- CORRELATION TAB --------------------
with tab_corr:
    numeric = filtered.select_dtypes(include='number')
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(numeric.corr(), cmap="coolwarm", annot=False, ax=ax)
    st.pyplot(fig)

# -------------------- TEAM SELECTION TAB --------------------
with tab_team:
    st.subheader("🏆 Best XI Team Selector (Based on Overall Rating)")
    team = (
        filtered.sort_values(by="Overall", ascending=False)
        .groupby("Position")
        .head(1)
    )  # best player per position
    st.dataframe(team[['Name', 'Age', 'Nationality', 'Club', 'Position', 'Overall']])

# -------------------- PLAYER COMPARISON TAB --------------------
with tab_compare:
    st.subheader("⚔ Compare Two Players")
    players = sorted(filtered['Name'].unique())

    p1 = st.selectbox("Select Player 1", players)
    p2 = st.selectbox("Select Player 2", players)

    if p1 and p2:
        c1, c2 = st.columns(2)
        player1 = filtered[filtered["Name"] == p1].iloc[0]
        player2 = filtered[filtered["Name"] == p2].iloc[0]

        c1.markdown(f"### 🟢 {p1}")
        c1.write(player1[['Age', 'Overall', 'Potential', 'Value', 'Wage']])

        c2.markdown(f"### 🔵 {p2}")
        c2.write(player2[['Age', 'Overall', 'Potential', 'Value', 'Wage']])

# -------------------- CONCLUSION TAB --------------------
with tab_conclusion:
    st.markdown("""
### 📌 FIFA EDA Summary

🔹 Filters for Position, Age, Club & Nationality  
🔹 Distribution of core skills & physical stats  
🔹 Relationship between Age & Performance  
🔹 Correlation Heatmap for performance insights  
🔹 Best XI team based on overall rating  
🔹 Player-vs-Player comparison system  

💡 You can now extend this dashboard to:
- Predict player market value
- Recommend similar players using ML
- Performance forecasting model
""")
