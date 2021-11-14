import pandas as pd
from utils import logger
from TrailerDownloader.utils import downloadDataFrameGenerator, loadCollectedMovies, loadYouTubeLinks


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
