import logging
import datetime
import string
from PyInquirer import prompt
from FeatureExtraction.utils import imagesDirectories
from FeatureExtraction.Models.VGG19 import VGG19Launcher
from FeatureExtraction.Models.Inception3 import Inception3Launcher
from FeatureExtraction.featureAggregation import featureAggregation


modules = ['Feature Extraction - InceptionV3',
           'Feature Extraction - VGG19', 'Feature Aggeration']


def getUserInput():
    questions = [
        {
            'type': 'list',
            'name': 'Action',
            'message': 'Select an action from the list below:',
            'choices': modules
        },
    ]
    userInput = prompt(questions)
    return userInput


def featureExtractor(inputDirectory: string, outputDirectory: string, packetSize: int):
    # Create logging structure
    logging.basicConfig(filename='features-logger.log', level=logging.INFO)
    currentMoment = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f'\n[{currentMoment}] Starting Feature Extractor ...')
    # Fetcth the list of movie folder(s) containing frames
    foldersList = imagesDirectories(inputDirectory)
    userInput = getUserInput()['Action']
    if userInput == 'Feature Extraction - VGG19':
        VGG19Launcher(foldersList, outputDirectory, packetSize)
    elif userInput == 'Feature Extraction - InceptionV3':
        Inception3Launcher(foldersList, outputDirectory, packetSize)
    elif userInput == 'Feature Aggeration':
        # Aggregates all features for each movie and produces a CSV file
        featureAggregation(outputDirectory)
