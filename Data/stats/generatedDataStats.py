import pandas as pd
from utils import logger
import matplotlib.pyplot as plt
from config import generatedListCSV


def plotHistogram(data, title, xLable, yLabel):
    plt.hist(data)
    plt.title(title)
    plt.xlabel(xLable)
    plt.ylabel(yLabel)
    plt.show()


def generatedDataStats():
    logger('Generated Dataset Analyzer started ...')
    print('Creating report from the generated dataset ...')
    generated = pd.read_csv(generatedListCSV)
    numberOfRows = len(generated)
    # Reporting
    logger(f'Number of ratings: {numberOfRows:,}')
    uniqueMovies = len(generated['movieId'].unique())
    logger(f'Number of movies: {uniqueMovies}')
    uniqueUsers = len(generated['userId'].unique())
    logger(f'Number of users: {uniqueUsers:,}')
    avgRatings = float("{:.4f}".format(generated['rating'].mean()))
    logger(f'Average Ratings: {avgRatings:,}')
    ratingsPerUser = float("{:.4f}".format(numberOfRows/uniqueUsers))
    logger(f'Ratings per User (R/U): {ratingsPerUser:,}')
    ratingsPerMovie = float("{:.4f}".format(numberOfRows/uniqueMovies))
    logger(f'Ratings per Movie (R/I): {ratingsPerMovie:,}')
    ratingsPerUserMovie = float("{:.4f}".format(
        numberOfRows/(uniqueUsers*uniqueMovies)))
    logger(f'Ratings per User*Movie (R/(I*U)): {ratingsPerUserMovie:,}')
    # Visualizing
    plotHistogram(generated['rating'],
                  'Ratings of Movies', 'Rating', 'Frequency')
