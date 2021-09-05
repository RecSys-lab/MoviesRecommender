from PyInquirer import prompt
from Data.main import dataProcess
from Frames.frameExtractor import frameExtractor
from FeatureExtraction.main import featureExtractor
from config import moviesList, movieLenzRatings, generatedDataset, moviesDirectory, outputDirectory, networkInputSize, imagesDirectory, extractedFeaturesDirectory

modules = ['Dataset Generator', 'Video Frame Extraction',
           'Visual Feature Extraction']


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
    print('Hi! Welcome to the MovieRecommender utilities 🚀')
    userInputs = getUserInput()['Action']
    if userInputs == 'Dataset Generator':
        # arguments: (list of movies in CSV, MovieLenz rating file path, output path)
        dataProcess(moviesList, movieLenzRatings, generatedDataset)
    elif userInputs == 'Video Frame Extraction':
        # arguments: (movies' directory, output directory, network input size)
        frameExtractor(moviesDirectory, outputDirectory, networkInputSize)
    elif userInputs == 'Visual Feature Extraction':
        # arguments: (input directory, output directory)
        featureExtractor(imagesDirectory, extractedFeaturesDirectory)


__init__()
