# MoviesRecommender

This repository contains utilities that provide the ability to generate a visual content-based full-length movie dataset.

## ☑️ Prerequisites

In order to run the application, you will need to install the Python libraries listed below:

- Python >= 3.4
- NumPy >= 1.19
- SciPy >= 1.6
- PyInquirer >= 1.0.3
- OpenCV-Python >= 4.1.1
- Tensorflow >= 2.6.0
- Keras >= 2.6.0
- CUDA >= 11.4

For a simple solution, you can simply run the below command in the root directory:

```python
pip install -r requirements.txt
```

Note that you should also install NVIDIA® CUDA® Deep Neural Network library™ (cuDNN) for high-performance GPU acceleration. This is used when training the DNN models in the feature extraction stage.

## 📑 Files and Modules

The application contains two main modules, including **Data Processing** and **Feature Extraction**, both accessible via the **main.py** file. Each of the mentioned modules provide a different set of utilities:

#### I. Data Processing

Contains tools for generating the movies dataset and analyzing its contents. You can find a detailed explanation about each functionalities below:

##### A) New Dataset Generator

This module requires a CSV file containing the movies metadata. The mentioned metadata includes **movieId**, **title**, and **genre**. The most important hint here is that the items of these fields must match MovieLenz-25M dataset instances. Here you can find a simple input file:

| movieId | title               | genre                         |
| ------- | ------------------- | ----------------------------- |
| 1203    | 12 Angry Men (1957) | Crime, Drama                  |
| 79132   | Inception (2010)    | Action, Crime, Drama, Mystery |
| ...     | ...                 | ...                           |

Using the **datasetGenerator.py** file of this module, movieIds will merge with the MovieLenz metadata and generates a more detailed dataset. The mentioned fields include userIds rated for the movie, IMDB rating, and timestamp of rating.

##### B) Data Analyzer

As you can guess, this module provides some statistics from the dataset, including number of movies, distribution of genres in a chart, total number of ratings and interacted users, etc.

## 🚀 Launch the Application

After installing required packages, the first step to run the engine of the application is to provide a proper configuration file. The `main.py` file, which is the start point of the application, needs such file to provide customized configurations for its differernt modules and then run the application:

#### I. Make a Configuration File

You can find a **config.example.py** in the root directory. What you need to do is to make a copy of this file and rename it to **config.py**. There, you can apply your customized settings:

```python
import os

# Dataset Generation
moviesList = 'C:/Some/Path/Dataset.csv'
generatedDataset = os.path.abspath('./Data/generated/output.csv')
movieLenzRatings = 'C:/Some/Path/ratings.csv'

# Feature Extraction
networkInputSize = 420
moviesDirectory = 'C:/Some/Path/'
outputDirectory = 'C:/Some/Path/'
```

As you can see, you need to specify some paths and settings for both **Dataset Generation** and **Feature Extraction** modules:

- **moviesList:** The path to the dataset.csv file that contains data of the collected movies
- **generatedDataset:** The path where the output dataset should be generated
- **movieLenzRatings:** The path to the MovieLenz ratings file
- **moviesDirectory:** The directory that contains a set of movie files
- **outputDirectory:** The folder to hold directories of the extracted frames
- **networkInputSize:** The width of the extracted frames (height will be calculated by the system based on video's aspect-ratio)

Please note that the **config.py** is placed in `.gitignore` file due to the customized settings.

#### II. Run the Application

After providing the configurations, you can easily run the app using the command below in the root directory:

```python
python ./main.py
```

## TODOs

- Feature extractors (AlexNet, VGG, etc)
- Code to find trailers of movies
