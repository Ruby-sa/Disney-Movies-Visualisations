import sqlite3

# Connect to the database
conn = sqlite3.connect("disney_movies.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table to store Disney movie information
cursor.execute("""
CREATE TABLE DisneyMovies (
    MovieID INTEGER PRIMARY KEY,
    MovieTitle TEXT,
    Princess TEXT,
    ReleaseYear INTEGER,
    RuntimeMinutes INTEGER,
    Rating REAL
)
""")

# Save the changes
conn.commit()

# Close the connection
conn.close()

print("Database created successfully.")
