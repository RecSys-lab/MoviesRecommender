# from keras import Model
from keras.applications.vgg19 import VGG19, preprocess_input
from keras.preprocessing.image import load_img, img_to_array

# About VGG-19:
# Running the example will load the VGG16 model and download the model weights
# The model can then be used directly to classify a photograph into one of 1,000 classes

# Static variables
vggInputSize = 224
tempImage = 'E:\Datasets\For Test\Movie Frames\00000123\frame0000096.jpg'


def VGG19Launcher():
    # Load a frame and convert it into a numpy array
    # frame = load_img(tempImage, target_size=(vggInputSize, vggInputSize))
    # frame = img_to_array(frame)
    # # Reshape the image according to the model's structure
    # frame = frame.reshape((1, frame.shape[0], frame.shape[1], frame.shape[2]))
    # # Preprocessing
    # frame = preprocess_input(frame)
    # # Load model
    print('\n🚀 Launching VGG-19 network ...')
    # model = VGG19()
    # # Removing the final output layer, so that the second last fully connected layer with 4,096 nodes will be the new output layer
    # model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    # # Get extracted features
    # features = model.predict(frame)
    # print('🔥 Features are ready! Check the output path!')
    # print(features.shape)
    # save to file
    # dump(features, open('dog.pkl', 'wb'))
