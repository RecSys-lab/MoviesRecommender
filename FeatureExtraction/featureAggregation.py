import os
import time
import glob
import json
import logging
import numpy as np


def featureAggregation(featureFoldersList: list, outputDirectory: str):
    for featuresFolder in featureFoldersList:
        movieId = featuresFolder.rsplit('/', 1)[1]
        # Check if the file with the same name of the movie containing aggregated features exists
        aggregatedFile = f'{outputDirectory}/{movieId}.txt'
        # true means it has been processed before
        isAggregated = os.path.isfile(aggregatedFile)
        if (isAggregated):
            print(
                f'🔥 Features were previously aggregated for {movieId}')
            logging.info(
                f'Features were previously aggregated for {movieId}')
        else:
            startTime = time.time()
            # Read packet JSON files
            numberOfPackets = len(os.listdir(featuresFolder))
            packetCounter = 0
            print(
                f'Processing {numberOfPackets} packets of the movie "{movieId}" ...')
            for packetFile in glob.glob(f'{featuresFolder}/*.json'):
                # Reading each packet's data
                jsonFile = open(packetFile,)
                packetData = json.load(jsonFile)
                packetCounter += 1
                for frameData in packetData:
                    features = frameData['features']
                    features = np.asarray(features)
                print(f'Packet #{packetCounter} has been processed!', features)
            print(
                f'✔️ Finished processing the packets of movie "{movieId}"')
            logging.info(
                f'Finished processing the packets of movie "{movieId}"')
