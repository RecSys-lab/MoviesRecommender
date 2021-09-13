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
csvHeader = ['movieId', 'visualFeatures']


def VGG19Launcher(foldersList: list, outputDirectory: string):
    logging.basicConfig(filename='features-logger.log')
    startTime = time.time()
    # Load model
    print('\n🚀 Launching VGG-19 network ...')
    logging.info('Launching VGG-19 network ...')
    model = VGG19()
    # Removing the final output layer, so that the second last fully connected layer with 4,096 nodes will be the new output layer
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    # Preparing CSV file
    outputFile = open(outputDirectory, 'w+', newline='')

    with outputFile:
        writer = csv.DictWriter(outputFile, fieldnames=csvHeader)
        writer.writeheader()

        for imageFolder in foldersList:
            movieId = imageFolder.rsplit('/', 1)[1]
            for imageFile in glob.glob(f'{imageFolder}/*.jpg'):
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
                                 'visualFeatures': features})
            print(f'Features extracted for {imageFolder}')

        elapsedTime = int(time.time() - startTime)
        print(
            f'🔥 Features are ready! Check the output path! {features.shape} (it took {elapsedTime} seconds)')
        logging.info(
            f'Features got ready in {features.shape} (took {elapsedTime} seconds)')
