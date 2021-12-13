import cv2
import numpy as np


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


def squareFrameGenerator(image, networkInputSize):
    finalImageDimensions = (networkInputSize, networkInputSize)
    # Calculating frame dimensions
    frameHeight, frameWidth = image.shape[:2]
    aspectRatio = frameWidth / frameHeight
    # Choosing proper interpolation
    dimensionH, dimensionW = finalImageDimensions
    interpolation = cv2.INTER_CUBIC  # Stretch the image
    if (frameHeight > dimensionH or frameWidth > dimensionW):
        interpolation = cv2.INTER_AREA  # Shrink the image
    # Add paddings to the image
    paddingColor = [0, 0, 0]
    if aspectRatio > 1:  # Image is horizontal
        generatedImageW = dimensionW
        generatedImageH = np.round(generatedImageW / aspectRatio).astype(int)
        verticalPadding = (dimensionH - generatedImageH) / 2
        paddingTop, paddingBottom = np.floor(verticalPadding).astype(
            int), np.ceil(verticalPadding).astype(int)
        paddingLeft, paddingRight = 0, 0
    elif aspectRatio < 1:  # Image is vertical
        generatedImageH = dimensionH
        generatedImageW = np.round(generatedImageH * aspectRatio).astype(int)
        horizontalPadding = (dimensionW - generatedImageW) / 2
        paddingLeft, paddingRight = np.floor(horizontalPadding).astype(
            int), np.ceil(horizontalPadding).astype(int)
        paddingTop, paddingBottom = 0, 0
    else:  # image is square, so no changes is needed
        generatedImageH, generatedImageW = dimensionH, dimensionW
        paddingLeft, paddingRight, paddingTop, paddingBottom = 0, 0, 0, 0
    # Scale the frame
    scaledImage = cv2.resize(
        image, (generatedImageW, generatedImageH), interpolation=interpolation)
    scaledImage = cv2.copyMakeBorder(scaledImage, paddingTop, paddingBottom,
                                     paddingLeft, paddingRight, borderType=cv2.BORDER_CONSTANT, value=paddingColor)
    return scaledImage
