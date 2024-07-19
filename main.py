# Importing pandas and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter for movies released in the 1990s
netflix_df = netflix_df[(netflix_df['type'] == 'Movie') &
                        (netflix_df['release_year'] >= 1990) &
                        (netflix_df['release_year'] <= 1999)]

# Plot histogram of movie durations
plt.hist(netflix_df['duration'], bins=20)
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Durations in the 1990s')
plt.show()

# Find the most frequent movie duration
duration = netflix_df['duration'].mode()[0]
print(duration)
netflix_df = netflix_df[netflix_df['genre'] == 'Action']

short_movie_count = 0
for lab, row in netflix_df.iterrows():
    if row['duration'] <= 90:
        short_movie_count += 1
print(short_movie_count)