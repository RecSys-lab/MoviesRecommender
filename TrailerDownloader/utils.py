import pandas as pd
from utils import logger
from config import movieLenzYouTubeDir


def loadYouTubeLinks():
    """
    Loads the CSV file containing the YouTube links
    Parameters
    ----------
    None
    """
    logger('Loading the CSV file containing the YouTube links ...')
    try:
        youtubeLinks = pd.read_csv(movieLenzYouTubeDir)
        print(f'Loaded {len(youtubeLinks)} YouTube links')
        return youtubeLinks
    except Exception as error:
        errorText = str(error)
        logger(
            f'Error while loading the CSV file: {errorText}', logLevel="error")
