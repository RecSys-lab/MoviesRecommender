import os
from glob import glob
from utils import logger
from PyInquirer import prompt
from FeatureExtraction.shotDetection import shotDetection
from FeatureExtraction.Models.VGG19 import VGG19Launcher
from FeatureExtraction.utils import SubdirectoryExtractor
from FeatureExtraction.Models.Inception3 import Inception3Launcher
from FeatureExtraction.featureAggregation import featureAggregation
from config import framesDir, featuresDir, aggFeaturesDir, shotsDir


modules = ['Feature Extraction - InceptionV3',
           'Feature Extraction - VGG19', 'Shot Detection', 'Feature Aggeration']


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


def selectFolder():
    # Show only folders inside the featuresDir (e.g., VGG19, Incp3)
    featuresFolders = glob(f'{featuresDir}/*/')
    choices = [os.path.dirname(folder).split('\\')[-1]
               for folder in featuresFolders]
    possibilities = [
        {
            'type': 'list',
            'name': 'Action',
            'message': 'Select from which model you want to take the extracted features:',
            'choices': choices
        },
    ]
    return prompt(possibilities)


def featureExtractor():
    logger('Starting Feature Extractor ...')
    # Fetcth the list of movie folder(s) containing frames
    framesFoldersList = SubdirectoryExtractor(framesDir)
    # Create a folder for outputs if not existed
    if not os.path.exists(featuresDir):
        os.mkdir(featuresDir)
    # Get action from user
    userInput = getUserInput()['Action']
    if userInput == 'Feature Extraction - VGG19':
        VGG19Launcher(framesFoldersList)
    elif userInput == 'Feature Extraction - InceptionV3':
        Inception3Launcher(framesFoldersList)
    elif userInput == 'Feature Aggeration' or userInput == 'Shot Detection':
        # Get the proper folder in a temporary variable
        tempDir = shotsDir if userInput == 'Shot Detection' else aggFeaturesDir
        # Create a folder for outputs if not existed
        if not os.path.exists(tempDir):
            os.mkdir(tempDir)
        # Prompt the user with folder associated with the models
        selectedFolder = selectFolder()['Action']
        tempFolder = f'{tempDir}/{selectedFolder}'
        # Create a folder for outputs if not existed
        if not os.path.exists(tempFolder):
            os.mkdir(tempFolder)
        # Fetch the list of folder(s) containing packets
        packetsFoldersList = SubdirectoryExtractor(
            f'{featuresDir}/{selectedFolder}')
        # Call proper function
        if userInput == 'Shot Detection':
            shotDetection(packetsFoldersList, tempFolder)
        elif userInput == 'Feature Aggeration':
            featureAggregation(packetsFoldersList, tempFolder)
