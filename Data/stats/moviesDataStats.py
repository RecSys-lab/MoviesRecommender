import numpy as np
import pandas as pd
from utils import logger
import matplotlib.pyplot as plt
from config import moviesListCSV


def genreStats(genres):
    print('Calculating genres data ...')
    genresArray = []
    # Genres are separated with |, now we need to merge them into one array
    for genre in genres:
        splittedGenre = genre.split('|')
        genresArray += splittedGenre
    # And now, counting them
    genresArray = np.array(genresArray)
    unique, counts = np.unique(genresArray, return_counts=True)
    countResults = dict(zip(unique, counts))
    # Plot them in a bar chart
    plt.bar(range(len(countResults)), list(
        countResults.values()), align='center')
    plt.xticks(rotation=45)
    plt.xlabel('Genres')
    plt.ylabel('Frequency')
    plt.title('Distribution of genres in the dataset')
    plt.xticks(range(len(countResults)), list(countResults.keys()))
    plt.show()
    return countResults


def moviesDataStats():
    logger('Movies Dataset Analyzer started ...')
    movies = pd.read_csv(moviesListCSV)
    # Genres
    genres = genreStats(movies['genre'])
    logger(f'Genres: {genres}')
    total = sum(genres.values())
    genrePerMovie = float("{:.2f}".format(total/len(movies)))
    logger(f'Total: {total:,} (genres per movie is {genrePerMovie})')
