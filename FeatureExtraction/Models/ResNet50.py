from keras.applications.resnet import ResNet50

# About ResNet-50:
# The model expects color images to have the square shape 224×224
# Running the example will load the ResNet50 model and download the model weights


def ResNet50Launcher():
    print('\n🔥 Launching ResNet-50 architecture ...')
    model = ResNet50()
    # Show a summary
    print('\n🚀 ResNet-50 is ready! Check the sumamry:')
    model.summary()
