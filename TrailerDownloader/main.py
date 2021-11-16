import os
from utils import logger
from config import trailersDir
from TrailerDownloader.utils import downloadDataFrameGenerator, loadCollectedMovies, loadYouTubeLinks, youtubeDownloader


def trailersDownloader():
    logger('Trailers Downloader Started ...')
    # Load CSV file containing the YouTube links
    youtubeLinks = loadYouTubeLinks()
    if (youtubeLinks is None):
        return
    # Load CSV file containing the list of movies (with their metadata)
    moviesList = loadCollectedMovies()
    if (moviesList is None):
        return
    # Create the download dataframe
    downloadDataFrame = downloadDataFrameGenerator(moviesList, youtubeLinks)
    if (downloadDataFrame is None):
        return
    # Create a folder for outputs if not existed
    if not os.path.exists(trailersDir):
        os.mkdir(trailersDir)
    # Download the trailers
    [youtubeDownloader(movieId, youtubeLink) for movieId, youtubeLink in zip(
        downloadDataFrame['movieId'], downloadDataFrame['youtubeLink'])]
    # Log finished
    # Save unfound videos
