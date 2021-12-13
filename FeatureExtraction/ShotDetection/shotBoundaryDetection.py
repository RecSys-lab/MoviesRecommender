import pandas as pd
from config import shotBoundaryThreshold


def shotBoundaryDetection(similarityDF: pd.DataFrame):
    """
    Detects shot boundaries in the similarity matrix.

    Parameters
    ----------
    similarityDF : pd.DataFrame
        The similarity matrix.
    """
    print("Detecting shot boundaries...")
    # Filter similarityDF to only include rows with similarity > threshold
    boundariesDF = similarityDF[similarityDF['similarity']
                                < shotBoundaryThreshold]
    print(boundariesDF)
    # Get the index of shot boundaries
    boundariesList = boundariesDF.index.tolist()
    boundariesList = [int(x) for x in boundariesList]
    print(boundariesList)
    # Get the middle of the shot boundaries
    for item1, item2 in zip(boundariesList, boundariesList[1:]):
        middleItem = int((item1 + item2)/2)
        print(middleItem)
