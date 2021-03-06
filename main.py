import logging
from utils import logger
from PyInquirer import prompt
from Data.main import dataProcess
from Recommendation.main import recommendation
from FeatureExtraction.main import featureExtractor
from TrailerDownloader.main import trailersDownloader
from FramesExtraction.frameExtractor import frameExtractor


modules = ['Dataset Generator', 'Video Frame Extraction',
           'Visual Feature Extraction', 'Trailers Downloader', 'Recommendation']


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
        dataProcess()
    elif userInputs == 'Video Frame Extraction':
        frameExtractor()
    elif userInputs == 'Visual Feature Extraction':
        featureExtractor()
    elif userInputs == 'Trailers Downloader':
        trailersDownloader()
    elif userInputs == 'Recommendation':
        recommendation()


__init__()
