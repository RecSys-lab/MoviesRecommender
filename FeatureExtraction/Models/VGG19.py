import csv
import time
import glob
import string
import logging
import numpy as np
from keras import Model
from keras.applications.vgg19 import VGG19, preprocess_input
from keras.preprocessing.image import load_img, img_to_array

# About VGG-19:
# Running the example will load the VGG16 model and download the model weights
# The model can then be used directly to classify a photograph into one of 1,000 classes

# Static variables
vggInputSize = 224
csvHeader = ['movieId', 'frameId', 'visualFeatures']


def VGG19Launcher(foldersList: list, outputDirectory: string):
    logging.basicConfig(filename='features-logger.log')
    # Load model
    print('\n🚀 Launching VGG-19 network ...')
    logging.info('Launching VGG-19 network ...')
    model = VGG19()
    # Removing the final output layer, so that the second last fully connected layer with 4,096 nodes will be the new output layer
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    for imageFolder in foldersList:
        startTime = time.time()
        movieId = imageFolder.rsplit('/', 1)[1]
        # Preparing CSV file
        outputFile = open(
            f'{outputDirectory}/features_{movieId}.csv', 'w+', newline='')
        with outputFile:
            writer = csv.DictWriter(outputFile, fieldnames=csvHeader)
            writer.writeheader()
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
                # featuresList.append(features)
                writer.writerow({'movieId': movieId,
                                 'frameId': frameId,
                                'visualFeatures': features})
        elapsedTime = int(time.time() - startTime)
        print(
            f'🔥 Features are ready! Check {imageFolder}! {features.shape} (it took {elapsedTime} seconds)')
        logging.info(
            f'Features got ready in {imageFolder} with overall shape {features.shape} (took {elapsedTime} seconds)')
