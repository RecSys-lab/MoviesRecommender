import os

# Dataset Generation
moviesListCSV = 'C:/Some/Path/Dataset.csv'
generatedListCSV = os.path.abspath('./Data/generated/output.csv')
movieLenzRatings = 'C:/Some/Path/ratings.csv'

# Frames
moviesDir = 'C:/Some/Path/'
framesDir = 'C:/Some/Path/'
networkInputSize = 420  # The width of the extracted frames

# Feature Extraction
packetSize = 25  # Each 25 frames are considered as a packet
# 1) Where the features should be stored, 2) Where to read feature folders for aggregation
featuresDir = 'C:/Some/Path/'
aggFeaturesDir = 'C:/Some/Path/'
shotsDir = 'C:/Some/Path/'

# Trailers Downloader
movieLenzYouTubeDir = 'C:/Some/Path/'
trailersDir = 'C:/Some/Path/'
