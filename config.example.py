import os

# Dataset Generation
moviesList = 'C:/Some/Path/Dataset.csv'
generatedDataset = os.path.abspath('./Data/generated/output.csv')
movieLenzRatings = 'C:/Some/Path/ratings.csv'

# Feature Extraction
networkInputSize = 420  # The width of the extracted frames
moviesDirectory = 'C:/Some/Path/'
outputDirectory = 'C:/Some/Path/'

# Logging
dataLogPath = os.path.abspath('./Data/data-logger.log')
framesLogPath = os.path.abspath('./Frames/frame-logger.log')
