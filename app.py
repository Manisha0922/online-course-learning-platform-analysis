import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Online Learning Analytics", page_icon="📚", layout="wide")
st.title("📚 Online Course & Learning Platform Analysis")
st.markdown("Explore course popularity, ratings, prices, and completion patterns.")
st.caption("Academic demo using a synthetic sample dataset — not official platform statistics.")

DATA_FILE = Path(__file__).parent / "data" / "online_courses.csv"
df = pd.read_csv(DATA_FILE)

with st.sidebar:
    st.header("Dashboard Filters")
    platforms = st.multiselect("Select platforms", sorted(df["Platform"].unique()), default=sorted(df["Platform"].unique()))
    categories = st.multiselect("Select categories", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    levels = st.multiselect("Difficulty level", sorted(df["Difficulty_Level"].unique()), default=sorted(df["Difficulty_Level"].unique()))
    min_rating = st.slider("Minimum rating", 0.0, 5.0, 0.0, 0.1)

view = df[
    df["Platform"].isin(platforms) &
    df["Category"].isin(categories) &
    df["Difficulty_Level"].isin(levels) &
    (df["Rating_Out_of_5"] >= min_rating)
]

if view.empty:
    st.warning("No courses match these filters. Change the filters to see results.")
else:
    a,b,c,d = st.columns(4)
    a.metric("Courses", f"{view['Course_ID'].nunique():,}")
    b.metric("Total enrolments", f"{view['Students_Enrolled'].sum():,}")
    c.metric("Average rating", f"{view['Rating_Out_of_5'].mean():.2f} / 5")
    d.metric("Average completion", f"{view['Completion_Rate_Percent'].mean():.1f}%")

    left, right = st.columns(2)
    with left:
        st.subheader("Most enrolled courses")
        top = view.groupby("Course_Name")["Students_Enrolled"].sum().nlargest(10).sort_values()
        fig, ax = plt.subplots(figsize=(8,5))
        ax.barh(top.index, top.values)
        ax.set_xlabel("Students enrolled")
        st.pyplot(fig)
        plt.close(fig)
    with right:
        st.subheader("Ratings by category")
        ratings = view.groupby("Category")["Rating_Out_of_5"].mean().sort_values()
        fig, ax = plt.subplots(figsize=(8,5))
        ax.barh(ratings.index, ratings.values)
        ax.set_xlim(0,5)
        ax.set_xlabel("Average rating / 5")
        st.pyplot(fig)
        plt.close(fig)

    left, right = st.columns(2)
    with left:
        st.subheader("Completion by difficulty")
        comp = view.groupby("Difficulty_Level")["Completion_Rate_Percent"].mean().reindex(["Beginner","Intermediate","Advanced"]).dropna()
        fig, ax = plt.subplots(figsize=(7,4))
        ax.bar(comp.index, comp.values)
        ax.set_ylim(0,100)
        ax.set_ylabel("Completion rate (%)")
        st.pyplot(fig)
        plt.close(fig)
    with right:
        st.subheader("Price vs rating")
        fig, ax = plt.subplots(figsize=(7,4))
        ax.scatter(view["Price_USD"], view["Rating_Out_of_5"], alpha=0.65)
        ax.set_xlabel("Price (USD)")
        ax.set_ylabel("Rating / 5")
        st.pyplot(fig)
        plt.close(fig)

    st.subheader("Course data")
    st.dataframe(view, use_container_width=True)
    st.download_button("Download filtered data (CSV)", view.to_csv(index=False).encode("utf-8"), "filtered_courses.csv", "text/csv")
