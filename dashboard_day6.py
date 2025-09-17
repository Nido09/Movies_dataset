import streamlit as st
import pandas as pd
import plotly.express as px

# ----- Page Config -----
st.set_page_config(page_title="Movie Dashboard", layout="wide")

# ----- Load Data -----
df = pd.read_csv("Day 2 Task.csv.csv")

# ----- Custom CSS -----
st.markdown("""
    <style>
    /* KPI Card Styling */
    .metric-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }
    .metric-card h2 {
        font-size: 28px;
        margin: 0;
    }
    .metric-card p {
        font-size: 14px;
        margin: 0;
        opacity: 0.8;
    }
    </style>
""", unsafe_allow_html=True)

# ----- Title -----
st.title("🎬 Movie Analytics Dashboard")

# ----- Sidebar Filters -----
st.sidebar.header("🔍 Filters")

genre_filter = st.sidebar.multiselect(
    "🎭 Select Genre",
    options=df["genre"].dropna().unique(),
    default=df["genre"].dropna().unique()
)

year_filter = st.sidebar.multiselect(
    "📅 Select Year",
    options=sorted(df["year"].dropna().unique()),
    default=sorted(df["year"].dropna().unique())
)

rating_filter = st.sidebar.slider(
    "⭐ Select Rating Range",
    float(df["rating"].min()), float(df["rating"].max()),
    (float(df["rating"].min()), float(df["rating"].max()))
)

# ----- Apply Filters -----
filtered_df = df[
    (df["genre"].isin(genre_filter)) &
    (df["year"].isin(year_filter)) &
    (df["rating"].between(rating_filter[0], rating_filter[1]))
]

# ----- KPIs -----
st.subheader("📊 Key Insights")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div class='metric-card'><h2>{len(filtered_df)}</h2><p>Movies</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><h2>{round(filtered_df['rating'].mean(),2)}</h2><p>Avg Rating</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-card'><h2>{round(filtered_df['box_office_million'].mean(),2)}</h2><p>Avg Box Office ($M)</p></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='metric-card'><h2>{round(filtered_df['duration_min'].mean(),2)}</h2><p>Avg Duration (min)</p></div>", unsafe_allow_html=True)

# ----- Charts -----
st.subheader("📈 Visual Insights")

col5, col6 = st.columns(2)

# Chart 1: Average Rating by Genre
with col5:
    fig1 = px.bar(
        filtered_df.groupby("genre")["rating"].mean().reset_index(),
        x="genre", y="rating", color="genre",
        title="⭐ Average Rating by Genre",
        text_auto=".2f",
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Box Office by Year
with col6:
    fig2 = px.line(
        filtered_df.groupby("year")["box_office_million"].sum().reset_index(),
        x="year", y="box_office_million",
        title="💰 Total Box Office by Year",
        markers=True,
        color_discrete_sequence=["#ff6f61"]
    )
    st.plotly_chart(fig2, use_container_width=True)

# Chart 3: Top Directors by Average Rating
st.subheader("🎬 Top Directors by Avg Rating")
top_directors = (
    filtered_df.groupby("director")["rating"].mean()
    .reset_index().sort_values(by="rating", ascending=False).head(10)
)
fig3 = px.bar(
    top_directors,
    x="director", y="rating", color="rating",
    title="🎬 Top 10 Directors by Average Rating",
    text_auto=".2f",
    color_continuous_scale="viridis"
)
st.plotly_chart(fig3, use_container_width=True)

# Chart 4: Rating Distribution
st.subheader("⭐ Rating Distribution")
fig4 = px.histogram(
    filtered_df, x="rating", nbins=20,
    title="⭐ Distribution of Movie Ratings",
    marginal="box",
    color_discrete_sequence=["#2a9d8f"]
)
st.plotly_chart(fig4, use_container_width=True)

# ----- Data Table -----
st.subheader("📋 Filtered Movies Dataset")
st.dataframe(filtered_df)
