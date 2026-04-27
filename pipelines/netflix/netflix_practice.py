import pandas as pd
# from DF_basics import df_cleaned

df = pd.read_csv("../../data/netflix/netflix_cleaned.csv")
df["date_added"]=pd.to_datetime(df["date_added"] ,  errors="coerce")


# Task 1 — Beginner
# Find how many Movies vs TV Shows are in the cleaned data:
# print(df["type"].value_counts())
# Task 2 — Beginner
# Find the top 5 countries with the most titles. One line of code. Figure it out using value_counts() on the right column.
# print(df["country"].value_counts().head(5))

# Task 3 — Intermediate
# Add a new column called year_added that extracts just the year from date_added:
df["year_added"] = df["date_added"].dt.year.astype("Int64")

# print(df["year_added"])



# Task 4 — filter recent movies
# Find all Netflix titles where:
# type is "Movie" AND release_year is greater than 2015
recent_movies = df[(df["type"] == "Movie") & (df["release_year"] > 2015)]
# print(recent_movies)
# print(len(recent_movies))

# Now the final challenge — Task 5 💪
# Write a function called summarize(df) that prints:
#
# Total titles
# Number of Movies vs TV Shows
# Top 3 countries
# Earliest and latest date_added
def summarize(df):
    print("=" * 40)
    total_titles = len(df)
    print(f"Total titles: {total_titles}")

    print("\nMovies vs TV Shows:")
    print(df["type"].value_counts())

    print("\nTop 3 countries:")
    print(df["country"].value_counts().head(3))

    print(f"\nEarliest date added: {min(df['date_added'])}")
    print(f"Latest date added: {max(df['date_added'])}")
    print("=" * 40)

summarize(df)