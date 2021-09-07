# import keras
# import numpy as np
# from keras.models import Sequential
# from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D

# # Static variables
# alexNetInputSize = 227


# def skeletonBuilder(imageShape):
#     print('\n🔥 Building AlexNet architecture ...')
#     # Instantiate a Sequential model
#     alexNet = Sequential()
#     # 1st Convolutional Layer
#     alexNet.add(Conv2D(filters=96, input_shape=imageShape,
#                 kernel_size=(11, 11), strides=(4, 4), padding='valid'))
#     alexNet.add(Activation('relu'))
#     # Max Pooling
#     alexNet.add(MaxPooling2D(pool_size=(3, 3),
#                 strides=(2, 2), padding='valid'))
#     # 2nd Convolutional Layer
#     alexNet.add(Conv2D(filters=256, kernel_size=(
#         5, 5), strides=(1, 1), padding='valid'))
#     alexNet.add(Activation('relu'))
#     # Max Pooling
#     alexNet.add(MaxPooling2D(pool_size=(3, 3),
#                 strides=(2, 2), padding='valid'))
#     # 3rd Convolutional Layer
#     alexNet.add(Conv2D(filters=384, kernel_size=(
#         3, 3), strides=(1, 1), padding='valid'))
#     alexNet.add(Activation('relu'))
#     # 4th Convolutional Layer
#     alexNet.add(Conv2D(filters=384, kernel_size=(
#         3, 3), strides=(1, 1), padding='valid'))
#     alexNet.add(Activation('relu'))
#     # 5th Convolutional Layer
#     alexNet.add(Conv2D(filters=256, kernel_size=(
#         3, 3), strides=(1, 1), padding='valid'))
#     alexNet.add(Activation('relu'))
#     # Max Pooling
#     alexNet.add(MaxPooling2D(pool_size=(3, 3),
#                 strides=(2, 2), padding='valid'))
#     # Fully Connected layer
#     alexNet.add(Flatten())
#     # 1st Fully Connected Layer
#     alexNet.add(Dense(4096, input_shape=(224*224*3,)))
#     alexNet.add(Activation('relu'))
#     # Add Dropout to prevent overfitting
#     alexNet.add(Dropout(0.4))
#     # 2nd Fully Connected Layer
#     alexNet.add(Dense(4096))
#     alexNet.add(Activation('relu'))
#     # Add Dropout
#     alexNet.add(Dropout(0.4))
#     # Output Layer
#     alexNet.add(Dense(1000))
#     alexNet.add(Activation('softmax'))
#     # Show a summary
#     print('\n🚀 AlexNet is ready! Check the sumamry:')
#     alexNet.summary()
#     # Compile the model
#     alexNet.compile(loss=keras.losses.categorical_crossentropy,
#                     optimizer='adam', metrics=['accuracy'])


def AlexNetLauncher():
    print('🚨 Disabled to improve performance (Only VGG-19 is available)')
#     imageShape = (alexNetInputSize, alexNetInputSize, 3)
#     np.random.seed(1000)  # Instantiate an empty model
#     skeletonBuilder(imageShape)
