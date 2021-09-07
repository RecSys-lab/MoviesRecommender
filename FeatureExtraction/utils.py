import os


def imageResizer(image, width, height):
    print('imageResizer')


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
