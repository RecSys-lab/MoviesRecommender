import pandas as pd
from utils import logger
from config import moviesListCSV, generatedListCSV, movieLenzRatings


def datasetGenerator():
    logger('Dataset Generator started ...')
    print('Reading dataset files ...')
    movies = pd.read_csv(moviesListCSV)
    logger(f'Dataset loaded with {len(movies)} movies')

    print('Reading ratings files from MovieLenz ...')
    ratings = pd.read_csv(movieLenzRatings)
    logger(f'Ratings loaded with {len(ratings)} instances (user ratings)')

    print('Joining files on the field MovieId ...')
    jointItems = movies.merge(ratings, on='movieId')

    print(f'Exporting to {generatedListCSV} ...')
    open(generatedListCSV, 'w+')  # Create file if doesn't exists
    jointItems.to_csv(generatedListCSV, index=False)

    logger(f'Finished generating dataset in {generatedListCSV}')
