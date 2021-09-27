import logging
import datetime
from PyInquirer import prompt
from FeatureExtraction.utils import imagesDirectories
from FeatureExtraction.Models.VGG19 import VGG19Launcher
from FeatureExtraction.Models.AlexNet import AlexNetLauncher
from FeatureExtraction.Models.Inception3 import Inception3Launcher


modules = ['AlexNet', 'InceptionV3', 'VGG19']


def getUserInput():
    questions = [
        {
            'type': 'list',
            'name': 'Action',
            'message': 'Select a feature extraction model from the list below:',
            'choices': modules
        },
    ]
    userInput = prompt(questions)
    return userInput


def featureExtractor(inputDirectory, outputDirectory):
    # Create logging structure
    logging.basicConfig(filename='features-logger.log', level=logging.INFO)
    currentMoment = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f'\n[{currentMoment}] Starting Feature Extractor ...')
    # Fetcth the list of movie folder(s) containing frames
    foldersList = imagesDirectories(inputDirectory)
    userInput = getUserInput()['Action']
    if userInput == 'AlexNet':
        AlexNetLauncher()
    elif userInput == 'VGG19':
        VGG19Launcher(foldersList, outputDirectory)
    elif userInput == 'InceptionV3':
        Inception3Launcher()
