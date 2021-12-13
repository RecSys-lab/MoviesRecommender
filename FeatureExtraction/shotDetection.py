import os
import time
import json
import pandas as pd
from glob import glob
from utils import logger
from scipy import spatial
from config import shotBoundaryThreshold
from FeatureExtraction.utils import featuresFolderChecker


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
        featuresDF = pd.DataFrame(columns=['frameId', 'features'])
        similarityDF = pd.DataFrame(
            columns=['source', 'destination', 'similarity'])
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
            for packetIdx, packetFile in enumerate(glob(f'{featuresFolder}/*.json')):
                if (packetIdx % 50 == 0):
                    print(f'Processing packet #{packetIdx}...')
                # Reading each packet's data
                jsonFile = open(packetFile,)
                packetData = json.load(jsonFile)
                # Iterate on each frames of array
                for frameData in packetData:
                    featuresDF = featuresDF.append(
                        {'frameId': frameData['frameId'], 'features': frameData['features']}, ignore_index=True)
            # Cosine Similarity Calculation
            print(
                f'Calculating cosine similarity among sequential frames of {movieId}...')
            for index in range(len(featuresDF)-1):
                similarity = 1 - spatial.distance.cosine(
                    featuresDF['features'][index],
                    featuresDF['features'][index + 1])
                similarity = round(similarity, 2)
                similarityDF = similarityDF.append({
                    'source': featuresDF['frameId'][index],
                    'destination': featuresDF['frameId'][index + 1],
                    'similarity': similarity}, ignore_index=True)
            # Save the similarity dataframe
            similarityDF.to_csv(
                f'{shotFolder}/{movieId}/_FramesSimilarity.csv', index=False)
            # Plotting the histogram of the similarity values
            # similarityDF.plot.bar()
            # plt.savefig(f'{shotFolder}/{movieId}.png')

            # Find boundaries
            boundariesDF = similarityDF[similarityDF['similarity']
                                        < shotBoundaryThreshold]
            print(boundariesDF)

            # Find middle frame of boundaries

            # Add shot boundary to the dataframe
            movieBoundaryCountDF = movieBoundaryCountDF.append(
                {'movieId': movieId, 'shotBoundaryCount': shotBoundaryCount}, ignore_index=True)
            movieBoundaryCountDF.to_csv(
                f'{shotFolder}/moviesShotBoundaryCount.csv', index=False)
            # Logging
            elapsedTime = '{:.2f}'.format(time.time() - startTime)
            logger(
                f'Finished detecting shots movie "{movieId}" in {elapsedTime} seconds.')
