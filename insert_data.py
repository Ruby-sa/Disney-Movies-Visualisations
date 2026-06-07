import sqlite3

# Connect to the database
conn = sqlite3.connect("disney_movies.db")

# Create a cursor
cursor = conn.cursor()

# Insert Disney movie data
cursor.executemany("""
INSERT INTO DisneyMovies
(MovieID, MovieTitle, Princess, ReleaseYear, RuntimeMinutes, Rating)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, "Snow White", "Snow White", 1937, 83, 7.6),
    (2, "Cinderella", "Cinderella", 1950, 74, 7.3),
    (3, "The Little Mermaid", "Ariel", 1989, 83, 7.6),
    (4, "Beauty and the Beast", "Belle", 1991, 84, 8.0)
])

# Save changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully.")
