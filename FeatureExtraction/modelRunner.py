import os
import time
import glob
import numpy as np
import pandas as pd
from utils import logger
from config import packetSize
from keras.preprocessing.image import load_img, img_to_array
from FeatureExtraction.utils import featuresFolderChecker, packetManager


def modelRunner(outputPath: str, foldersList: list, inputSize: int, model, preprocess_input):
    for imageFolder in foldersList:
        movieId = imageFolder.rsplit('/', 1)[1]
        # Check if the folder with the same name of the movie containing features exists
        movieFeaturesExists = featuresFolderChecker(movieId, outputPath)
        if (movieFeaturesExists):
            print(
                f'Features were previously extracted in {outputPath}\\{movieId}')
        else:
            # Extract features
            startTime = time.time()
            fearuesCounter = len(os.listdir(imageFolder))
            # Initially, the whole number of frames
            remainingNumberOfFrames = len(os.listdir(imageFolder))
            # Used to be compared to packetSize, so that all x items saved into one file
            packetCounter = 0
            packetIndex = 1  # Holds the name of the packet, e.g. Packet0001
            dataFrame = pd.DataFrame(columns=['frameId', 'features'])
            for imageFile in glob.glob(f'{imageFolder}/*.jpg'):
                fileName = os.path.basename(imageFile)
                parentDir = os.path.basename(os.path.dirname(imageFile))
                try:
                    # Finding frameId by removing .jpg from the name
                    frameId = ('frame' + imageFile.rsplit('frame', 1)[1])[:-4]
                    # Load a frame and convert it into a numpy array
                    frame = load_img(imageFile, target_size=(
                        inputSize, inputSize))
                    frameData = img_to_array(frame)
                    frameData = np.expand_dims(frameData, axis=0)
                    # Preprocessing
                    frameData = preprocess_input(frameData)
                    # Get extracted features
                    features = model.predict(frameData)
                    # Append rows to dataFrame
                    dataFrame = dataFrame.append(
                        {'frameId': frameId, 'features': features[0]}, ignore_index=True)
                    packetCounter += 1
                    # Reset the counter only if packetCounter reaches the limit (packetSize) and there is no more frames for process
                    remainingNumberOfFrames -= 1
                    resetCounter = (packetCounter == packetSize) or (
                        remainingNumberOfFrames == 0)
                    if (resetCounter):
                        # Save dataFrame as packet in a file
                        packetManager(packetIndex, dataFrame,
                                      movieId, outputPath)
                        # Clear dataFrame rows
                        dataFrame.drop(dataFrame.index, inplace=True)
                        packetCounter = 0
                        packetIndex += 1
                except Exception as error:
                    errorText = str(error)
                    logger(
                        f'Error while extracting features of {fileName} in {parentDir} ({errorText})', logLevel="error")
                    continue
            elapsedTime = '{:.2f}'.format(time.time() - startTime)
            logger(
                f'Extracted {fearuesCounter}x{features.shape} features ({packetIndex-1} packets) from {movieId} in {elapsedTime} seconds!')
