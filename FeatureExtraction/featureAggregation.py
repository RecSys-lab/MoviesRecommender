import logging
from FeatureExtraction.utils import aggregatedFileChecker


def featureAggregation(featureFoldersList: list, outputDirectory: str):
    for featuresFolder in featureFoldersList:
        movieId = featuresFolder.rsplit('/', 1)[1]
        # Check if the file with the same name of the movie containing aggregated features exists
        isAggregated = aggregatedFileChecker(movieId, outputDirectory, 'txt')
        if (isAggregated):
            print(
                f'🔥 Features were previously aggregated for {movieId}')
            logging.info(
                f'Features were previously aggregated for {movieId}')
