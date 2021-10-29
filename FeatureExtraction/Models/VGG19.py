from keras import Model
from utils import logger
from FeatureExtraction.modelRunner import modelRunner
from keras.applications.vgg19 import VGG19, preprocess_input


# About VGG-19:
# Running the example will load the VGG16 model and download the model weights
# The model can then be used directly to classify a photograph into one of 1,000 classes

# Static variables
vggInputSize = 224


def VGG19Launcher(foldersList: list, outputDirectory: str, packetSize: int):
    # Load model
    logger('Launching VGG-19 network ...')
    model = VGG19()
    # Removing the final output layer, so that the second last fully connected layer with 4,096 nodes will be the new output layer
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    modelRunner(foldersList, outputDirectory, packetSize,
                vggInputSize, model, preprocess_input)
