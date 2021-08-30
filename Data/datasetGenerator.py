import pandas as pd


def datasetGenerator(moviesList, movieLenzRatings, generatedDataset):
    print('Reading dataset files ...')
    movies = pd.read_csv(moviesList)
    print(f'Dataset loaded with {len(movies)} instances (movies)')

    print('Reading ratings files from MovieLenz ...')
    ratings = pd.read_csv(movieLenzRatings)
    print(f'Ratings loaded with {len(ratings)} instances (user ratings)')

    print('Joining files on the field MovieId ...')
    jointItems = movies.merge(ratings, on='movieId')

    # --- Note: CSV movieId doesn't keep the 10-digits format, so we should normalize the name ---
    # for index in movies.iterrows():
    #     print(index)
    # userId = '1'
    # print(userId.rjust(10, '0'))

    print(f'Exporting to {generatedDataset} ...')
    open(generatedDataset, 'w+')  # Create file if doesn't exists
    jointItems.to_csv(generatedDataset, index=False)

    print('Finished generating dataset!')
