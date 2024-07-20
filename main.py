# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt


def filter_90s(dataset):
    # Filter for movies released in the 1990s
    dataset = dataset[(dataset['type'] == 'Movie') &
                            (dataset['release_year'] >= 1990) &
                            (dataset['release_year'] <= 1999)]

    # Plot histogram of movie durations
    plt.figure(figsize=(10, 8))
    plt.hist(dataset['duration'], bins=20, color='green', alpha=0.6)
    plt.grid()
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Number of Movies')
    plt.title('Distribution of Movie Durations in the 1990s')
    plt.show()

    # Find the most frequent movie duration
    duration = dataset['duration'].mode()[0]
    dataset = dataset[dataset['genre'] == 'Action']

    short_movie_count = 0
    for lab, row in dataset.iterrows():
        if row['duration'] <= 90:
            short_movie_count += 1


def filter_genre(dataset):
    filtered_df = dataset['genre'].value_counts().reset_index()
    titles = list(filtered_df.loc[:, 'genre'].values)
    counts = list(filtered_df.loc[:, 'count'])
    plt.figure(figsize=(24, 24))
    plt.grid()
    plt.bar(titles, counts, color='purple', alpha=0.6)
    plt.xlabel('Genre', fontsize=19)
    plt.ylabel('Amount', fontsize=24)
    plt.title('Distribution of Genres', fontsize=24)
    plt.xticks(rotation=70, fontsize=18)
    plt.yticks(fontsize=18)
    plt.show()


if __name__ == '__main__':
    # Read in the Netflix CSV as a DataFrame
    netflix_df = pd.read_csv("netflix_data.csv")
    filter_90s(netflix_df)
    filter_genre(netflix_df)


