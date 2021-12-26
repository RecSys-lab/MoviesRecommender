import os
import time
import pandas as pd
from utils import logger
from config import packetSize
from FeatureExtraction.utils import featuresFolderChecker, packetManager
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
    movieBoundaryCountDF = pd.DataFrame(
        columns=['movieId', 'shotBoundaryCount'])
    for featuresFolder in featureFoldersList:
        movieId = featuresFolder.rsplit('/', 1)[1]
        # Check if the folder with the same name of the movie containing features exists
        movieShotsExists = featuresFolderChecker(movieId, shotFolder)
        if (movieShotsExists):
            print(f'Shots were previously detected in {featuresFolder}')
        else:
            startTime = time.time()
            packetCounter = 0
            packetIndex = 1  # Holds the name of the packet, e.g. Packet0001
            dataFrame = pd.DataFrame(columns=['frameId', 'features'])
            # Read packet JSON files
            packetCount = len(os.listdir(featuresFolder))
            print(f'Processing {packetCount} packets of movie "{movieId}" ...')
            # Iterate over the packet files to collect them all in a single dataframe
            featuresDF = packetsDataCollector(featuresFolder)
            # Cosine Similarity Calculation
            similarityDF = cosineSimilarityCalculation(
                movieId, shotFolder, featuresDF)
            # Find shot boundaries and select the middle frame of each shot
            boundaryFrames, avgShotLength = shotBoundaryDetection(similarityDF)
            avgShotLength = round(avgShotLength, 2)
            # Create a dataframe with the middle frames
            keyframesDF = featuresDF[featuresDF.index.isin(boundaryFrames)]
            remainingNumberOfFrames = len(keyframesDF)
            # Save the keyframes
            movieBoundaryCountDF = movieBoundaryCountDF.append(
                {'movieId': movieId, 'framesCount': len(featuresDF), 'avgShotLength': avgShotLength, 'shotBoundaryCount': len(keyframesDF)}, ignore_index=True)
            # Iterate over the keyframes to save them in packets
            for index, row in keyframesDF.iterrows():
                # Append rows to dataFrame
                dataFrame = dataFrame.append(
                    {'frameId': row['frameId'], 'features': row['features']}, ignore_index=True)
                packetCounter += 1
                # Reset the counter only if packetCounter reaches the limit (packetSize) and there is no more frames for process
                remainingNumberOfFrames -= 1
                resetCounter = (packetCounter == packetSize) or (
                    remainingNumberOfFrames == 0)
                if (resetCounter):
                    # Save dataFrame as packet in a file
                    packetManager(packetIndex, dataFrame,
                                  movieId, shotFolder)
                    # Clear dataFrame rows
                    dataFrame.drop(dataFrame.index, inplace=True)
                    packetCounter = 0
                    packetIndex += 1
            # Logging
            elapsedTime = '{:.2f}'.format(time.time() - startTime)
            logger(
                f'Finished detecting shots of movie "{movieId}" in {elapsedTime} seconds.')
        # Save per movie shot boundary count to a file
        movieBoundaryCountDF.to_csv(
            f'{shotFolder}/moviesShotBoundaryCount.csv', index=False)
