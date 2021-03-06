import os

# Dataset Generation
moviesListCSV = os.path.abspath('./Data/moviesList.csv')
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
shotBoundaryThreshold = 0.7  # The threshold for the shot boundary detection
shotsDir = 'C:/Some/Path/'

# Trailers Downloader
movieLenzYouTubeDir = 'C:/Some/Path/'
trailersDir = 'C:/Some/Path/'
