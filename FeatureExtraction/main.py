from PyInquirer import prompt
from FeatureExtraction.Models.AlexNet import alexNetLauncher


# Static variables
alexNetInputSize = 227


modules = ['AlexNet', 'VGG19', 'InceptionV3', 'ResNet50']


def getUserInput():
    questions = [
        {
            'type': 'list',
            'name': 'Action',
            'message': 'Select a feature extraction model from the list below:',
            'choices': modules
        },
    ]
    userInputs = prompt(questions)
    return userInputs


def featureExtractor(inputDirectory, outputDirectory):
    userInputs = getUserInput()['Action']
    if userInputs == 'AlexNet':
        alexNetLauncher(alexNetInputSize)
    elif userInputs == 'VGG19':
        print('VGG19')
    elif userInputs == 'InceptionV3':
        print('InceptionV3')
    elif userInputs == 'ResNet50':
        print('ResNet50')
