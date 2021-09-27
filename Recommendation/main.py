import logging
import datetime
from Recommendation.sample import sampleCornac


def recommendation():
    print('\n🚀 Launching Recommender ...')
    # Create logging structure
    logging.basicConfig(filename='recommender-logger.log', level=logging.INFO)
    currentMoment = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f'\n[{currentMoment}] Starting Feature Extractor ...')
    sampleCornac()
