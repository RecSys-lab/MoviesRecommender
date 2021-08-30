from PyInquirer import prompt
from Data.datasetGenerator import datasetGenerator
from Data.stats.moviesDataStats import moviesDataStats
from Data.stats.generatedDataStats import generatedDataStats


modules = ['New Dataset Generator', 'Data Analyzer']


def getUserInput():
    questions = [
        {
            'type': 'list',
            'name': 'Action',
            'message': 'Select your action from the list below:',
            'choices': modules
        },
    ]
    userInputs = prompt(questions)
    return userInputs


def dataProcess(moviesList, movieLenzRatings, generatedDataset):
    userInputs = getUserInput()['Action']
    if userInputs == 'New Dataset Generator':
        print('This module merges the the given movies list with metadata of MovieLenz dataset')
        datasetGenerator(moviesList, movieLenzRatings, generatedDataset)
    elif userInputs == 'Data Analyzer':
        print('This module provides some analysis on the dataset')
        moviesDataStats(moviesList)
        generatedDataStats(generatedDataset)
