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
    # Finished Downloading
    logger('Downloading process has been finished!')
    # Now, generating the list of movies not listed in the CSV file
    moviesNotListed = moviesList[~moviesList['movieId'].isin(
        downloadDataFrame['movieId'])]
    # Check if there are any movies not listed in the CSV file
    if (len(moviesNotListed) > 0):
        logger(f'{len(moviesNotListed)} movies not listed in the CSV file!')
        # Saving not listed movies
        filePath = os.path.abspath('./Data/generated/moviesWithNoLinks.csv')
        moviesNotListed[['movieId', 'title']].to_csv(filePath, index=False)
        logger(
            f'Saved the dataframe containing not-listed movies into {filePath}!')
    logger('Trailers Downloader Finished!')
