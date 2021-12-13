import os
import time
import pandas as pd
from utils import logger
from FeatureExtraction.utils import featuresFolderChecker
from FeatureExtraction.ShotDetection.packetsDataCollector import packetsDataCollector
from FeatureExtraction.ShotDetection.shotBoundaryDetection import shotBoundaryDetection
from FeatureExtraction.ShotDetection.cosineSimilarityCalculation import cosineSimilarityCalculation


def shotDetection(featureFoldersList: list, shotFolder: str):
    """
    This function detects the shot boundaries in a video.

    Parameters
    ----------
    featureFoldersList : list
        List of feature folders.
    shotFolder : str
        Path to the folder where the shotFolder features will be saved.

    Returns
    -------
    None.
    """
    logger('Starting Feature Extractor ...')
    for featuresFolder in featureFoldersList:
        shotBoundaryCount = 0
        movieId = featuresFolder.rsplit('/', 1)[1]
        movieBoundaryCountDF = pd.DataFrame(
            columns=['movieId', 'shotBoundaryCount'])
        # Check if the folder with the same name of the movie containing features exists
        movieShotsExists = featuresFolderChecker(movieId, shotFolder)
        if (movieShotsExists):
            print(f'Shots were previously detected in {featuresFolder}')
        else:
            startTime = time.time()
            # Read packet JSON files
            packetCount = len(os.listdir(featuresFolder))
            print(f'Processing {packetCount} packets of movie "{movieId}" ...')
            # Iterate over the packet files to collect them all in a single dataframe
            featuresDF = packetsDataCollector(featuresFolder)
            # Cosine Similarity Calculation
            similarityDF = cosineSimilarityCalculation(
                movieId, shotFolder, featuresDF)
            # Find shot boundaries and select the middle frame of each shot
            shotBoundaryDetection(similarityDF)
            movieBoundaryCountDF = movieBoundaryCountDF.append(
                {'movieId': movieId, 'shotBoundaryCount': shotBoundaryCount}, ignore_index=True)
            movieBoundaryCountDF.to_csv(
                f'{shotFolder}/moviesShotBoundaryCount.csv', index=False)
            # Logging
            elapsedTime = '{:.2f}'.format(time.time() - startTime)
            logger(
                f'Finished detecting shots movie "{movieId}" in {elapsedTime} seconds.')
