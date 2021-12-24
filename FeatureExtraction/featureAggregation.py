import os
import time
import glob
import json
import numpy as np
import pandas as pd
from utils import logger
from sklearn.mixture import GaussianMixture


def featureAggregation(featureFoldersList: list, aggFolder: str):
    """
    Aggregates all features in the featureFoldersList into one csv file.

    Parameters
    ----------
    featureFoldersList : list
        List of feature folders.
    aggFolder : str
        Path to the folder where the aggregated features will be saved.

    Returns
    -------
    None.
    """
    for featuresFolder in featureFoldersList:
        movieId = featuresFolder.rsplit('/', 1)[1]
        # Check if the file with the same name of the movie containing aggregated features exists
        aggregatedFile = f'{aggFolder}/{movieId}.json'
        # true means it has been processed before
        isAggregated = os.path.isfile(aggregatedFile)
        if (isAggregated):
            print(
                f'🔥 Features were previously aggregated for {movieId}')
        else:
            startTime = time.time()
            # Read packet JSON files
            numberOfPackets = len(os.listdir(featuresFolder))
            # Arrays to store each movie's columns altogether
            movieAggFeatures = []
            movieAggFeat_Max = []
            movieAggFeat_Mean = []
            packetCounter = 0
            print(
                f'Processing {numberOfPackets} packets of the movie "{movieId}" ...')
            for packetFile in glob.glob(f'{featuresFolder}/*.json'):
                # Reading each packet's data
                jsonFile = open(packetFile,)
                packetData = json.load(jsonFile)
                packetCounter += 1
                # Iterate on each frames of array
                for frameData in packetData:
                    features = frameData['features']
                    features = np.asarray(features)
                    movieAggFeatures.append(features)
                if (packetCounter % 50 == 0):
                    print(f'Packet #{packetCounter} has been processed!')
            # Calculating desired aggregated features
            movieAggFeat_Max = np.mean(movieAggFeatures, axis=0)
            movieAggFeat_Mean = np.max(movieAggFeatures, axis=0)
            movieAggFeat_Max = np.round(movieAggFeat_Max, 6)
            movieAggFeat_Mean = np.round(movieAggFeat_Mean, 6)
            # Calculating Gaussian Mixture Model
            print(f'Calculating Gaussian Mixture Model for {movieId} ...')
            movieGMM = GaussianMixture(
                n_components=2, random_state=0).fit(movieAggFeatures)
            # Save aggregated arrays in files
            dataFrame = pd.DataFrame(columns=['Max', 'Mean'])
            dataFrame = dataFrame.append(
                {'Max': movieAggFeat_Max, 'Mean': movieAggFeat_Mean, 'GMM_Mean': movieGMM.means_}, ignore_index=True)
            dataFrame.to_json(
                f'{aggFolder}/{movieId}.json', orient="records")
            elapsedTime = '{:.2f}'.format(time.time() - startTime)
            logger(
                f'Finished aggregating packets of movie "{movieId}" in {elapsedTime} seconds.')
