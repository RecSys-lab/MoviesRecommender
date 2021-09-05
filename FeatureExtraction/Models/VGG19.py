from keras.applications.vgg19 import VGG19

# About VGG-19:
# Running the example will load the VGG16 model and download the model weights
# The model can then be used directly to classify a photograph into one of 1,000 classes


def VGG19Launcher():
    print('\n🔥 Launching VGG-19 architecture ...')
    model = VGG19()
    # Show a summary
    print('\n🚀 VGG-19 is ready! Check the sumamry:')
    model.summary()
