from glob import glob
from utils import logger
from config import featuresDir


def shotDetection():
    """
    This function detects the shot boundaries in a video.
    """
    logger('Starting Feature Extractor ...')
