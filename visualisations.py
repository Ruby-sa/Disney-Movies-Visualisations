import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("disney_movies.db")

# Read the movie data into a dataframe
df = pd.read_sql_query("SELECT * FROM DisneyMovies", conn)

# Close the connection
conn.close()

# Bar chart: movie ratings
plt.figure()
plt.bar(df["MovieTitle"], df["Rating"])
plt.title("Disney Movie Ratings")
plt.xlabel("Movie")
plt.ylabel("Rating")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("ratings_chart.png")
plt.show()

# Bar chart: movie runtime
plt.figure()
plt.bar(df["MovieTitle"], df["RuntimeMinutes"])
plt.title("Runtime of Disney Movies")
plt.xlabel("Movie")
plt.ylabel("Runtime in Minutes")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("runtime_chart.png")
plt.show()

# Line chart: release years
plt.figure()
plt.plot(df["MovieTitle"], df["ReleaseYear"], marker="o")
plt.title("Release Years of Disney Movies")
plt.xlabel("Movie")
plt.ylabel("Release Year")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("release_years_chart.png")
plt.show()

# Pie chart: share of total runtime
plt.figure()
plt.pie(df["RuntimeMinutes"], labels=df["MovieTitle"], autopct="%1.1f%%")
plt.title("Share of Total Runtime")
plt.tight_layout()
plt.savefig("runtime_pie_chart.png")
plt.show()

print("Visualisations created successfully.")