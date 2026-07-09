import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings - wide layout looks more like a real dashboard
st.set_page_config(page_title="Netflix Analytics Dashboard", layout="wide")

# Load the cleaned dataset (same file we created in the Python cleaning notebook)
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_cleaned.csv")
    df["date_added"] = pd.to_datetime(df["date_added"])
    return df

df = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filters")

# Type filter (Movie / TV Show)
type_options = ["All"] + sorted(df["type"].dropna().unique().tolist())
selected_type = st.sidebar.selectbox("Type", type_options)

# Country filter
country_options = ["All"] + sorted(df["primary_country"].dropna().unique().tolist())
selected_country = st.sidebar.selectbox("Country", country_options)

# Rating filter
rating_options = ["All"] + sorted(df["rating"].dropna().unique().tolist())
selected_rating = st.sidebar.selectbox("Rating", rating_options)

# Year range filter
min_year = int(df["year_added"].min())
max_year = int(df["year_added"].max())
year_range = st.sidebar.slider("Year Added Range", min_year, max_year, (min_year, max_year))

# Apply filters to the dataframe
filtered_df = df.copy()

if selected_type != "All":
    filtered_df = filtered_df[filtered_df["type"] == selected_type]

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["primary_country"] == selected_country]

if selected_rating != "All":
    filtered_df = filtered_df[filtered_df["rating"] == selected_rating]

filtered_df = filtered_df[
    (filtered_df["year_added"] >= year_range[0]) &
    (filtered_df["year_added"] <= year_range[1])
]

# If the selected filters don't match any rows at all, stop here with a clear message
# instead of letting every chart below break with confusing blank/empty errors.
if len(filtered_df) == 0:
    st.title("Netflix Titles Analytics Dashboard")
    st.warning("No titles match the selected filters. Try widening your filter selection.")
    st.stop()

# ---------------- Title ----------------
st.title("Netflix Titles Analytics Dashboard")
st.markdown("Explore trends across Netflix's movie and TV show catalog.")

# ---------------- KPI Cards ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", len(filtered_df))
col2.metric("Movies", len(filtered_df[filtered_df["type"] == "Movie"]))
col3.metric("TV Shows", len(filtered_df[filtered_df["type"] == "Tv Show"]))
col4.metric("Countries", filtered_df["primary_country"].nunique())

st.markdown("---")

# ---------------- Row 1: Movies vs TV Shows + Content Growth ----------------
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Movies vs TV Shows")
    type_counts = filtered_df["type"].value_counts().reset_index()
    type_counts.columns = ["type", "count"]
    fig1 = px.pie(type_counts, names="type", values="count", hole=0.4)
    st.plotly_chart(fig1, use_container_width=True)

with row1_col2:
    st.subheader("Content Added Over Time")
    year_counts = filtered_df["year_added"].value_counts().sort_index().reset_index()
    year_counts.columns = ["year", "count"]
    fig2 = px.line(year_counts, x="year", y="count", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- Row 2: Top Countries + Top Genres ----------------
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Top 10 Countries")
    top_countries = (
        filtered_df[filtered_df["primary_country"] != "Not Given"]["primary_country"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    if len(top_countries) == 0:
        st.info("No country data available for the current filter selection.")
    else:
        top_countries.columns = ["country", "count"]
        fig3 = px.bar(top_countries, x="count", y="country", orientation="h")
        fig3.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig3, use_container_width=True)

with row2_col2:
    st.subheader("Top 10 Genres")
    top_genres = filtered_df["primary_genre"].value_counts().head(10).reset_index()
    top_genres.columns = ["genre", "count"]
    fig4 = px.bar(top_genres, x="count", y="genre", orientation="h")
    fig4.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig4, use_container_width=True)

# ---------------- Row 3: Rating Distribution + Duration Histogram ----------------
row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    st.subheader("Rating Distribution")
    rating_counts = filtered_df["rating"].value_counts().reset_index()
    rating_counts.columns = ["rating", "count"]
    fig5 = px.bar(rating_counts, x="rating", y="count")
    st.plotly_chart(fig5, use_container_width=True)

with row3_col2:
    st.subheader("Movie Duration Distribution")
    # This column only has values for Movies (TV Shows have seasons instead),
    # so if the current filter is "Tv Show" only, there's nothing to plot here.
    movie_durations = filtered_df["movie_duration_minutes"].dropna()
    if len(movie_durations) == 0:
        st.info("No movies in the current filter selection, so there's no duration data to show. "
                 "This chart only applies to Movies (TV Shows have seasons instead of a runtime).")
    else:
        fig6 = px.histogram(movie_durations, nbins=30, labels={"value": "Duration (minutes)"})
        st.plotly_chart(fig6, use_container_width=True)

# ---------------- Data Table ----------------
st.markdown("---")
st.subheader("Browse the Data")
st.dataframe(filtered_df[["title", "type", "primary_country", "primary_genre", "rating", "year_added"]])
