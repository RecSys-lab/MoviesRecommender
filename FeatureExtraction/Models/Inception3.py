from keras.applications.inception_v3 import InceptionV3

# About Inception-v3 (GoogleNet):
# The model expects color images to have the square shape 299×299
# Running the example will load the Inception-v3 model and download the model weights


def Inception3Launcher():
    print('\n🔥 Launching Inception-v3 architecture ...')
    model = InceptionV3()
    # Show a summary
    print('\n🚀 Inception-v3 is ready! Check the sumamry:')
    model.summary()
