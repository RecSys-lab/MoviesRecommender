import os
import time
import glob
import string
import logging
import numpy as np
from keras import Model
from keras.applications.vgg19 import VGG19, preprocess_input
from keras.preprocessing.image import load_img, img_to_array
from FeatureExtraction.utils import featuresFileCreator, featuresFolderChecker

# About VGG-19:
# Running the example will load the VGG16 model and download the model weights
# The model can then be used directly to classify a photograph into one of 1,000 classes

# Static variables
vggInputSize = 224


def VGG19Launcher(foldersList: list, outputDirectory: string):
    logging.basicConfig(filename='features-logger.log')
    # Load model
    print('\n🚀 Launching VGG-19 network ...')
    logging.info('Launching VGG-19 network ...')
    model = VGG19()
    # Removing the final output layer, so that the second last fully connected layer with 4,096 nodes will be the new output layer
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    for imageFolder in foldersList:
        movieId = imageFolder.rsplit('/', 1)[1]
        # Check if the folder with the same name of the movie containing features exists
        movieFeaturesExists = featuresFolderChecker(movieId, outputDirectory)
        if (movieFeaturesExists):
            print(
                f'🔥 Features were previously extracted in {outputDirectory}\\{movieId}')
            logging.info(
                f'Features were previously extracted in {outputDirectory}\\{movieId}')
        else:
            # Extract features
            startTime = time.time()
            for imageFile in glob.glob(f'{imageFolder}/*.jpg'):
                # Finding frameId by removing .jpg from the name
                frameId = ('frame' + imageFile.rsplit('frame', 1)[1])[:-4]
                # Load a frame and convert it into a numpy array
                frame = load_img(imageFile, target_size=(
                    vggInputSize, vggInputSize))
                frameData = img_to_array(frame)
                frameData = np.expand_dims(frameData, axis=0)
                # Preprocessing
                frameData = preprocess_input(frameData)
                # Get extracted features
                features = model.predict(frameData)
                # Exporting
                featuresfilePath = featuresFileCreator(
                    movieId, outputDirectory, frameId)
                np.savetxt(featuresfilePath, features[0], delimiter=', ')
            elapsedTime = int(time.time() - startTime)
            print(
                f'🔥 Features saved in {outputDirectory} with overall shape {features.shape} (it took {elapsedTime} seconds)')
            logging.info(
                f'Features saved in {outputDirectory} with overall shape {features.shape} (took {elapsedTime} seconds)')
