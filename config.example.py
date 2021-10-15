import os

# Dataset Generation
moviesList = 'C:/Some/Path/Dataset.csv'
generatedDataset = os.path.abspath('./Data/generated/output.csv')
movieLenzRatings = 'C:/Some/Path/ratings.csv'

# Frames
moviesDirectory = 'C:/Some/Path/'
outputDirectory = 'C:/Some/Path/'
networkInputSize = 420  # The width of the extracted frames

# Feature Extraction
packetSize = 25  # Each 25 frames are considered as a packet
imagesDirectory = 'C:/Some/Path/'
# 1) Where the features should be stored, 2) Where to read feature folders for aggregation
extractedFeaturesDirectory = 'C:/Some/Path/'

# Logging
dataLogPath = os.path.abspath('./Data/data-logger.log')
framesLogPath = os.path.abspath('./Frames/frame-logger.log')
