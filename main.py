import logging
from utils import logger
from PyInquirer import prompt
from Data.main import dataProcess
from Recommendation.main import recommendation
from Frames.frameExtractor import frameExtractor
from FeatureExtraction.main import featureExtractor

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
        dataProcess()
    elif userInputs == 'Video Frame Extraction':
        frameExtractor()
    elif userInputs == 'Visual Feature Extraction':
        featureExtractor()
    elif userInputs == 'Recommendation':
        recommendation()


__init__()
