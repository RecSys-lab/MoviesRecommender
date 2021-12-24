import pandas as pd
from config import shotBoundaryThreshold


def shotBoundaryDetection(similarityDF: pd.DataFrame):
    """
    Detects shot boundaries in the similarity matrix.

    Parameters
    ----------
    similarityDF : pd.DataFrame
        The similarity matrix.

    Returns
    -------
    boundaryFrames: list
        List of the middle frames between sequential shot boundaries.
    avgShotLength: float
        The average shot length.
    """
    print("Detecting shot boundaries...")
    shotLengths = []
    boundaryFrames = []
    # Filter similarityDF to only include rows with similarity > threshold
    boundariesDF = similarityDF[similarityDF['similarity']
                                < shotBoundaryThreshold]
    # Get the index of shot boundaries
    boundariesList = boundariesDF.index.tolist()
    boundariesList = [int(x) for x in boundariesList]
    # Get the middle index of the shot boundaries (keyframes)
    for item1, item2 in zip(boundariesList, boundariesList[1:]):
        middleItem = int((item1 + item2)/2)
        boundaryFrames.append(middleItem)
        shotLengths.append(item2 - item1)
    # Average shot length
    avgShotLength = sum(shotLengths)/len(shotLengths)
    # Return the list of keyframes
    print("Keyframes extracted...")
    return boundaryFrames, avgShotLength
