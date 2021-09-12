import csv
import glob
import string
import numpy as np
from keras import Model
from keras.applications.vgg19 import VGG19, preprocess_input
from keras.preprocessing.image import load_img, img_to_array

# About VGG-19:
# Running the example will load the VGG16 model and download the model weights
# The model can then be used directly to classify a photograph into one of 1,000 classes

# Static variables
vggInputSize = 224


def VGG19Launcher(foldersList: list, outputDirectory: string):
    featuresList = []
    # Load model
    print('\n🚀 Launching VGG-19 network ...')
    model = VGG19()
    # Removing the final output layer, so that the second last fully connected layer with 4,096 nodes will be the new output layer
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    for imageFolder in foldersList:
        for imageFile in glob.glob(f'{imageFolder}/*.jpg'):
            # Load a frame and convert it into a numpy array
            frame = load_img(imageFile, target_size=(
                vggInputSize, vggInputSize))
            frameData = img_to_array(frame)
            frameData = np.expand_dims(frameData, axis=0)
            # Preprocessing
            frameData = preprocess_input(frameData)
            # Reshape the image according to the model's structure
            # frame = frame.reshape((1, frame.shape[0], frame.shape[1], frame.shape[2]))
            # Get extracted features
            features = model.predict(frameData)
            featuresList.append(features)
        print(f'Features extracted for {imageFolder}')

    print(f'🔥 Features are ready! Check the output path! {features.shape}')
    # Save to file
    writer = csv.writer(open(outputDirectory, 'w+'))
    writer.writerow(featuresList)
    # open(outputDirectory, 'w+')  # Create file if doesn't exists
    # featuresList.to_csv(outputDirectory, index=False)
