import pandas as pd
from scipy import spatial


def cosineSimilarityCalculation(movieId: str, shotFolder: str, featuresDF: pd.DataFrame):
    """
    Calculates the cosine similarity between sequential features (frames data).

    Parameters
    ----------
    movieId : str
        The movie id.
    shotFolder : str
        The folder containing shots.
    featuresDF : pd.DataFrame
        The dataframe containing the features.

    Returns
    -------
    similarityDF: pd.DataFrame
        The dataframe containing the cosine similarity between sequential features.
    """
    similarityDF = pd.DataFrame(
        columns=['source', 'destination', 'similarity'])
    print(
        f'Calculating cosine similarity among sequential frames of {movieId}...')
    for index in range(len(featuresDF)-1):
        similarity = 1 - spatial.distance.cosine(
            featuresDF['features'][index],
            featuresDF['features'][index + 1])
        similarity = round(similarity, 2)
        similarityDF = similarityDF.append({
            'source': featuresDF['frameId'][index],
            'destination': featuresDF['frameId'][index + 1],
            'similarity': similarity}, ignore_index=True)
    # Save the similarity dataframe
    similarityDF.to_csv(
        f'{shotFolder}/{movieId}/_FramesSimilarity.csv', index=False)
    # Plotting the histogram of the similarity values
    # similarityDF.plot.bar()
    # plt.savefig(f'{shotFolder}/{movieId}.png')
    return similarityDF
