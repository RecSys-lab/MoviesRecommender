import os
import cv2
import string
from Frames.resizeTools.frameResize import frameResize


# This module extracts frames from a given list of movies
def frameExtractor(moviesDirectory, outputDirectory, networkInputSize):
    print(f'Fetching the list of items in "{moviesDirectory}"')
    videoFiles = os.listdir(moviesDirectory)
    print(f'Number of videos: {len(videoFiles)}')
    for file in videoFiles:
        print(f'Processing video {file} ...')
        # Accessing video and provide a proper name for it
        currentVideoPath = f'{moviesDirectory}/{file}'
        normalizedVideoName = file.split('.')
        normalizedVideoName = string.capwords(
            normalizedVideoName[0].replace("_", "")).replace(" ", "")
        # Creating output folder
        generatedPath = outputDirectory + '/' + normalizedVideoName
        if not os.path.exists(generatedPath):
            os.mkdir(generatedPath)
        # Capturing video
        capturedVideo = cv2.VideoCapture(currentVideoPath)
        frameRate = capturedVideo.get(cv2.CAP_PROP_FPS)
        success, image = capturedVideo.read()
        # Calculating the aspect-ratio
        print(f'Extracting frames (one frame in every {frameRate} frames) ...')
        frameCounter = 0
        fileNameCounter = 0
        while success:
            if (frameCounter % int(frameRate) == 0):
                # Resizing the image, while preserving its aspect-ratio
                # image = squareFrameGenerator(image, networkInputSize) # In case we need a square frame
                image = frameResize(image, networkInputSize)
                # Save the frame as a file
                cv2.imwrite(
                    f"{outputDirectory}/{normalizedVideoName}/frame{fileNameCounter}.jpg", image)
                fileNameCounter += 1
            success, image = capturedVideo.read()
            # Showing progress
            if (frameCounter % 1000 == 0):
                currentTime = int(frameCounter / frameRate)
                print(
                    f'Prcessing frame #{frameCounter} ({currentTime:,} seconds passed) ...')
            frameCounter += 1
        print(f'Frames generated for {normalizedVideoName} in {generatedPath}')
