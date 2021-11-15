import os
import time
import pandas as pd
from utils import logger
from pytube import YouTube
from config import trailersDir, moviesListCSV, movieLenzYouTubeDir


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
        print(f'Loaded {len(youtubeLinks)} YouTube links!')
        return youtubeLinks
    except Exception as error:
        errorText = str(error)
        logger(
            f'Error while loading the CSV file: {errorText}', logLevel="error")


def loadCollectedMovies():
    """
    Loads the CSV file containing the list of movies (with their metadata)
    Parameters
    ----------
    None
    """
    logger('Loading the CSV file containing the list of collected movies ...')
    try:
        moviesList = pd.read_csv(moviesListCSV)
        print(f'Loaded the data for {len(moviesList)} movies!')
        return moviesList
    except Exception as error:
        errorText = str(error)
        logger(
            f'Error while loading the CSV file: {errorText}', logLevel="error")


def downloadDataFrameGenerator(moviesList, youtubeLinks):
    """
    Loads the lists of movies and YouTube links to generate the links to download
    Parameters
    ----------
    moviesList: pandas.DataFrame
        The data frame of movies
    youtubeLinks: pandas.DataFrame
        The data frame of YouTube links

    """
    logger('Creating the dataframe containing download links ...')
    try:
        # Merge the two dataframes ==> columns: (movieId, youtubeId, title)
        downloadDataFrame = pd.merge(
            moviesList[['movieId']], youtubeLinks, on='movieId')
        # Add a prefix to the YouTube link
        prefix = 'https://www.youtube.com/watch?v='
        downloadDataFrame['youtubeLink'] = downloadDataFrame['youtubeId'].apply(
            prefix.__add__)
        # Remove the old column containing youtubeId
        downloadDataFrame.drop(columns=['youtubeId'], inplace=True)
        print(f'Created YouTube links for {len(downloadDataFrame)} trailers!')
        # Save the dataframe to a CSV file
        filePath = os.path.abspath('./Data/generated/downloadLinks.csv')
        downloadDataFrame.to_csv(filePath, index=False)
        logger(
            f'Saved the dataframe containing download links into {filePath}!')
        # Return the dataframe
        return downloadDataFrame
    except Exception as error:
        errorText = str(error)
        logger(
            f'Error while creating the download dataframe: {errorText}', logLevel="error")


def youtubeDownloader(movieId: str, link: str):
    """
    Downloads a given YouTube link and saves it to the disk
    Parameters
    ----------
    movieId: str
        The ID of the movie (trailer)
    link: str
        The YouTube link to download
    """
    # Check if the video already exists
    if os.path.exists(f'{trailersDir}/{movieId}.mp4'):
        logger(
            f'Skipping, as the video {movieId}.mp4 already exists!', logLevel="warning")
        return
    fixedLengthMovieId = str(movieId).zfill(10)
    print(f'Downloading the trailer for movie "{fixedLengthMovieId}" ...')
    try:
        startTime = time.time()
        # Create a YouTybe object
        youtubeVideo = YouTube(link)
        # Download the video
        youtubeVideo.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').asc().first().download(output_path=trailersDir, filename=f'{fixedLengthMovieId}.mp4')
        elapsedTime = '{:.2f}'.format(time.time() - startTime)
        logger(
            f'Download finished for the trailer "{fixedLengthMovieId}" in {elapsedTime} seconds!')
    except Exception as error:
        errorText = str(error)
        logger(
            f'Error while downloading the file {fixedLengthMovieId}.mp4 ({errorText})', logLevel="error")
