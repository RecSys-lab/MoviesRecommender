import os
import pandas as pd
import matplotlib.pyplot as plt


def plotHistogram(data, title, xLable, yLabel):
    plt.hist(data)
    plt.title(title)
    plt.xlabel(xLable)
    plt.ylabel(yLabel)
    plt.show()


def plotPie(sizes, labels, title, xLable, yLabel):
    plt.pie(sizes, explode=None, labels=labels, shadow=True)
    plt.title(title)
    plt.xlabel(xLable)
    plt.ylabel(yLabel)
    plt.show()


def generatedDataStats(generatedFilePath):
    print('Creating report from the generated dataset ...')
    generated = pd.read_csv(generatedFilePath)
    numberOfRows = len(generated)
    # Reporting
    print(f'Number of ratings: {numberOfRows:,}')
    uniqueMovies = len(generated['movieId'].unique())
    print(f'Number of movies: {uniqueMovies}')
    uniqueUsers = len(generated['userId'].unique())
    print(f'Number of users: {uniqueUsers:,}')
    avgRatings = float("{:.4f}".format(generated['rating'].mean()))
    print(f'Average Ratings: {avgRatings:,}')
    ratingsPerUser = float("{:.4f}".format(numberOfRows/uniqueUsers))
    print(f'Ratings per User (R/U): {ratingsPerUser:,}')
    ratingsPerMovie = float("{:.4f}".format(numberOfRows/uniqueMovies))
    print(f'Ratings per Movie (R/I): {ratingsPerMovie:,}')
    ratingsPerUserMovie = float("{:.4f}".format(
        numberOfRows/(uniqueUsers*uniqueMovies)))
    print(f'Ratings per User*Movie (R/(I*U)): {ratingsPerUserMovie:,}')
    # Visualizing
    plotHistogram(generated['rating'],
                  'Ratings of Movies', 'Rating', 'Frequency')
