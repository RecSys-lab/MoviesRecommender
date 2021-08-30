import cv2


# This module receives a frame and generates aresized one while keeping the aspect ratio
def frameResize(image, networkInputSize):
    # Calculating frame dimensions
    frameHeight, frameWidth = image.shape[:2]
    aspectRatio = frameWidth / frameHeight
    # Resize frame's width, while keeping its aspect ratio
    generatedImageW = networkInputSize
    generatedImageH = int(generatedImageW / aspectRatio)
    # Scale the frame
    scaledImage = cv2.resize(
        image, (generatedImageW, generatedImageH), interpolation=cv2.INTER_AREA)
    return scaledImage
