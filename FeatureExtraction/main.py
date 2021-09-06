from PyInquirer import prompt
from FeatureExtraction.Models.VGG16 import VGG16Launcher
from FeatureExtraction.Models.VGG19 import VGG19Launcher
from FeatureExtraction.Models.AlexNet import AlexNetLauncher
from FeatureExtraction.Models.ResNet50 import ResNet50Launcher
from FeatureExtraction.Models.Inception3 import Inception3Launcher


modules = ['AlexNet', 'InceptionV3', 'ResNet50', 'VGG16', 'VGG19']


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
    userInput = getUserInput()['Action']
    if userInput == 'AlexNet':
        AlexNetLauncher()
    elif userInput == 'VGG16':
        VGG16Launcher()
    elif userInput == 'VGG19':
        VGG19Launcher()
    elif userInput == 'InceptionV3':
        Inception3Launcher()
    elif userInput == 'ResNet50':
        ResNet50Launcher()
