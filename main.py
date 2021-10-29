import logging
from utils import logger
from PyInquirer import prompt
from Data.main import dataProcess
from Recommendation.main import recommendation
from Frames.frameExtractor import frameExtractor
from FeatureExtraction.main import featureExtractor
from config import moviesList, movieLenzRatings, generatedDataset, moviesDirectory, outputDirectory, networkInputSize, imagesDirectory, extractedFeaturesDirectory, aggregatedFeaturesDirectory, packetSize

modules = ['Dataset Generator', 'Video Frame Extraction',
           'Visual Feature Extraction', 'Recommendation']


def getUserInput():
    questions = [
        {
            'type': 'list',
            'name': 'Action',
            'message': 'Choose your desired module:',
            'choices': modules
        },
    ]
    userInputs = prompt(questions)
    return userInputs


def __init__():
    # Creating log file
    logging.basicConfig(filename='logger.log', level=logging.INFO)
    logger('Framework started!')
    # Getting inputs from users
    userInputs = getUserInput()['Action']
    if userInputs == 'Dataset Generator':
        # arguments: (list of movies in CSV, MovieLenz rating file path, output path)
        dataProcess(moviesList, movieLenzRatings, generatedDataset)
    elif userInputs == 'Video Frame Extraction':
        # arguments: (movies' directory, output directory, network input size)
        frameExtractor(moviesDirectory, outputDirectory, networkInputSize)
    elif userInputs == 'Visual Feature Extraction':
        # arguments: (input directory, output directory)
        featureExtractor(
            imagesDirectory, extractedFeaturesDirectory, aggregatedFeaturesDirectory, packetSize)
    elif userInputs == 'Recommendation':
        # arguments: ()
        recommendation()


__init__()
