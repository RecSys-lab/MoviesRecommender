import pandas as pd
from utils import logger
from TrailerDownloader.utils import loadYouTubeLinks


def trailersDownloader():
    logger('Trailers Downloader Started ...')
    # Load CSV file containing the YouTube links
    youtubeLinks = loadYouTubeLinks()
    if (youtubeLinks is None):
        return
