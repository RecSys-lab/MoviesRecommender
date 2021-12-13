import json
import pandas as pd
from glob import glob


def packetsDataCollector(featuresFolder: str):
    """
    Collect all JSON files into a DataFrame

    Parameters
    ----------
    featuresFolder : str
        Path to the folder containing the JSON files

    Returns
    -------
    featuresDF : DataFrame
        DataFrame containing all the visual features in JSON files

    """
    featuresDF = pd.DataFrame(columns=['frameId', 'features'])
    # Iterate over the packet files to collect them all in a single dataframe
    for packetIdx, packetFile in enumerate(glob(f'{featuresFolder}/*.json')):
        if (packetIdx % 50 == 0):
            print(f'Processing packet #{packetIdx}...')
        # Reading each packet's data
        jsonFile = open(packetFile,)
        packetData = json.load(jsonFile)
        # Iterate on each frames of array
        for frameData in packetData:
            featuresDF = featuresDF.append(
                {'frameId': frameData['frameId'], 'features': frameData['features']}, ignore_index=True)
        jsonFile.close()
    return featuresDF
