import os

# Dataset Generation
moviesList = 'C:/Some/Path/Dataset.csv'
generatedDataset = os.path.abspath('./Data/generated/output.csv')
movieLenzRatings = 'C:/Some/Path/ratings.csv'

# Frames
moviesDirectory = 'C:/Some/Path/'
outputDirectory = 'C:/Some/Path/'

# Feature Extraction
networkInputSize = 420  # The width of the extracted frames
imagesDirectory = 'C:/Some/Path/'
extractedFeaturesDirectory = 'C:/Some/Path/'

# Logging
dataLogPath = os.path.abspath('./Data/data-logger.log')
framesLogPath = os.path.abspath('./Frames/frame-logger.log')
