import os
import string


# Creates a list of movie folder(s) containing extracted frame files
def imagesDirectories(foldersDirectory):
    print('Accessing the list of folders containing movie frames ...')
    # Return all folders inside the given directory
    foldersList = os.listdir(f'{foldersDirectory}')
    # Add the absolute path to each folder
    foldersListAbsolute = [foldersDirectory +
                           '/' + folder for folder in foldersList]
    print(f'Found {len(foldersListAbsolute)} item(s)!')
    return foldersListAbsolute


# Checks if a folder with the same name of movieId exists or not, creates one if not
def featuresFolderChecker(movieId: string, targetPath: string):
    featuresfileName = f'{targetPath}/{movieId}'
    # true means it has been processed before
    checker = os.path.exists(featuresfileName)
    if not checker:
        os.mkdir(featuresfileName)
    return checker


# Creates a CSV file containing features
def featuresFileCreator(movieId: string, targetPath: string, fileName: string):
    featuresfilePath = f'{targetPath}/{movieId}/{fileName}.csv'
    if not os.path.exists(featuresfilePath):
        open(featuresfilePath, 'w+')
    return featuresfilePath


# Manages the contents of a packet and sends a signal whether to reset the counter or not
def packetManager(packetCounter: int, packetSize: int, packetIndex: int, movieId: string, targetPath: string) -> bool:
    if (packetCounter < packetSize):
        return False
    else:
        formatedPacketIndex = '{0:04d}'.format(packetIndex)
        packetName = f'packet{formatedPacketIndex}'
        print(f'Saving {packetName} for movie {movieId} ...')
        featuresfilePath = featuresFileCreator(
            movieId, targetPath, packetName)
        return True
