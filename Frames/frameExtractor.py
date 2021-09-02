import os
import cv2
import string
import logging
from Frames.resizeTools.frameResize import frameResize


# This module extracts frames from a given list of movies
def frameExtractor(moviesDirectory, outputDirectory, networkInputSize):
    print(f'Fetching the list of items in "{moviesDirectory}"')
    try:
        videoFiles = os.listdir(moviesDirectory)
        # Create logging structure
        logging.basicConfig(filename='frame-logger.log', level=logging.INFO)
        # Filter only video files
        for file in videoFiles:
            if not file.lower().endswith(('.mkv', '.avi', '.mp4')):
                videoFiles.remove(file)
        print(f'Number of videos: {len(videoFiles)}\n')
        logging.info(f'Number of videos: {len(videoFiles)}\n')
        # Iterate on all video files in the given directory
        for file in videoFiles:
            print(f'Processing video {file} ...')
            # Accessing video and provide a proper name for it
            currentVideoPath = f'{moviesDirectory}/{file}'
            normalizedVideoName = file.split('.')
            normalizedVideoName = string.capwords(
                normalizedVideoName[0].replace("_", "")).replace(" ", "")
            # Creating output folder
            generatedPath = outputDirectory + '/' + normalizedVideoName
            # Do not re-generate frames for movies if there is a folder with their normalized name
            if os.path.exists(generatedPath):
                # os.mkdir(generatedPath)
                print(
                    f'Skipping movie {file} as its folder already exists!\n')
                logging.info(
                    f'Skipping movie {file} as its folder already exists!')
            else:
                os.mkdir(generatedPath)
                # Capturing video
                try:
                    capturedVideo = cv2.VideoCapture(currentVideoPath)
                    frameRate = int(capturedVideo.get(cv2.CAP_PROP_FPS))
                    success, image = capturedVideo.read()
                    # Calculating the aspect-ratio
                    print(
                        f'Extracting frames (one frame in every {frameRate} frames) ...')
                    frameCounter = 0
                    fileNameCounter = 0
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
                                f"{outputDirectory}/{normalizedVideoName}/frame{formattedFrameCounter}.jpg", image)
                            fileNameCounter += 1
                        success, image = capturedVideo.read()
                        # Showing progress
                        if (frameCounter % 1000 == 0):
                            currentTime = int(frameCounter / frameRate)
                            print(
                                f'Processing frame #{frameCounter} ({currentTime:,} seconds passed) ...')
                        frameCounter += 1
                    print(
                        f'Frames generated for {normalizedVideoName} in {generatedPath}')
                    logging.info(
                        f'Frames generated for {normalizedVideoName} in {generatedPath}')
                except cv2.error as openCVError:
                    print('🚨 Error while processing video:', str(openCVError))
                    logging.error(
                        f'Error while processing video {openCVError}')
                except Exception as otherError:
                    print('🚨 Error while running the app:', str(otherError))
                    logging.error(f'Error while running the app: {otherError}')
    except FileNotFoundError:
        print(
            "🚨 [FileNotFoundError] The input directory does not exist or contain video files!")
        logging.error(
            f'The input directory does not exist or contain video files!')
    except Exception as e:
        print('🚨 Error while running the app:', str(e))
        logging.error(f'Error while running the app: {e}')
