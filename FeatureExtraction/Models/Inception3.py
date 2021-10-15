import logging
from keras import Model
from FeatureExtraction.modelRunner import modelRunner
from keras.applications.inception_v3 import InceptionV3, preprocess_input

# About Inception-v3 (GoogleNet):
# The model expects color images to have the square shape 299×299
# Running the example will load the Inception-v3 model and download the model weights

# Static variables
vggInputSize = 299


def Inception3Launcher(foldersList: list, outputDirectory: str, packetSize: int):
    logging.basicConfig(filename='features-logger.log')
    # Load model
    print('\n🚀 Launching Inception-v3 network ...')
    logging.info('Launching Inception-v3 network ...')
    model = InceptionV3()
    # Removing the final output layer, so that the second last fully connected layer with 2,048 nodes will be the new output layer
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    modelRunner(foldersList, outputDirectory, packetSize,
                vggInputSize, model, preprocess_input)
