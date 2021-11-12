import os
import cv2
import time
import string
from glob import glob
from utils import logger
from Frames.utils import frameResize
from config import moviesDir, framesDir, networkInputSize

videoTypes = ('mkv', 'avi', 'mp4')


# This module extracts frames from a given list of movies
def frameExtractor():
    logger('Frame Extraction started ...')
    print(f'Fetching the list of items in "{moviesDir}"')
    try:
        # Create a folder for outputs if not existed
        if not os.path.exists(framesDir):
            os.mkdir(framesDir)
        # Get the list of movies in the movies directory
        videoFiles = []
        for type in videoTypes:
            videoFiles.extend(glob(f'{moviesDir}/*.{type}'))
        logger(f'Number of videos to process: {len(videoFiles)}')
        # Iterate on all video files in the given directory
        for file in videoFiles:
            fileName = os.path.basename(file)
            print(f'Processing video "{fileName}" ...')
            # Accessing video and provide a proper name for it
            normalizedVideoName = string.capwords(
                fileName.split('.')[0].replace("_", "")).replace(" ", "")
            # Creating output folder
            generatedPath = framesDir + '/' + normalizedVideoName
            # Do not re-generate frames for movies if there is a folder with their normalized name
            if os.path.exists(generatedPath):
                print(
                    f'Skipping movie {file} as its folder already exists!\n')
            else:
                os.mkdir(generatedPath)
                # Capturing video
                try:
                    capturedVideo = cv2.VideoCapture(file)
                    frameRate = int(capturedVideo.get(cv2.CAP_PROP_FPS))
                    success, image = capturedVideo.read()
                    # Calculating the aspect-ratio
                    print(
                        f'Extracting frames (one frame in every {frameRate} frames) ...')
                    frameCounter = 0
                    fileNameCounter = 0
                    startTime = time.time()
                    while success:
                        if (frameCounter % frameRate == 0):
                            # Resizing the image, while preserving its aspect-ratio
                            # image = squareFrameGenerator(image, networkInputSize) # In case we need a square frame
                            image = frameResize(image, networkInputSize)
                            # Format the frame counter as: frame1 --> frame0000001
                            formattedFrameCounter = '{0:07d}'.format(
                                fileNameCounter)
                            # Save the frame as a file
                            cv2.imwrite(
                                f"{framesDir}/{normalizedVideoName}/frame{formattedFrameCounter}.jpg", image)
                            fileNameCounter += 1
                        success, image = capturedVideo.read()
                        # Showing progress
                        if (frameCounter % 1000 == 0):
                            currentTime = int(frameCounter / frameRate)
                            print(
                                f'Processing frame #{frameCounter} ({currentTime:,} seconds passed) ...')
                        frameCounter += 1
                    # Finished extracting frames
                    elapsedTime = '{:.2f}'.format(time.time() - startTime)
                    print(
                        f'Extracted {frameCounter} frames of {normalizedVideoName} in {elapsedTime} seconds!')
                except cv2.error as openCVError:
                    errorText = str(openCVError)
                    logger(
                        f'Error while processing video: {errorText}', logLevel="error")
                except Exception as otherError:
                    errorText = str(otherError)
                    logger(
                        f'Error while running the app: {errorText}', logLevel="error")
    except FileNotFoundError:
        logger(
            f'The input directory does not exist or contain video files!', logLevel="error")
    except Exception as error:
        errorText = str(error)
        logger(f'Error while running the app ({errorText})', logLevel="error")
