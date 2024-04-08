#Import libraries
#-----------------------------
import kaggle 
## If kaggle is not installed run !pip install kaggle
## Also, set up your Kaggle API credentials by downloading your kaggle.json API token from your Kaggle account 
## Place the json file in the correct location (usually ~C:\Users\<Windows-username>\.kaggle\kaggle.json on Windows)
#-----------------------------
import os
import zipfile
#-----------------------------

#Define URL to download data from Kaggle
URL = 'rohanrao/formula-1-world-championship-1950-2020'
#-----------------------------
#Define function to download data if it doesn't exist, stop if it is already there
#Define list of datasets that must exist in the source
dataset_list = [
    'circuits.csv',               
    'constructors.csv',
    'lap_times.csv',
    'races.csv',
    'sprint_results.csv',
    'constructor_results.csv',
    'driver_standings.csv',
    'pit_stops.csv',
    'results.csv',
    'status.csv',
    'constructor_standings.csv',
    'drivers.csv',
    'qualifying.csv',
    'seasons.csv'
]
#Define function to check if data exists, and download if it does not
def get_kaggle_f1_data(url = URL , force_download = False):
    """
    Download the formula 1 data from kaggle
    --------
    Parameters:
    url: string (optional)
        url of the kaggle dataset to download
    force_download: bool (optional)
        if True, force redownload of data
    --------
    Notes:
    url and the filepath in the function are set to a default
        url = formula 1 datasets in kaggle
        filepath = datasets/f1
    the filepath cannot be changed, however if the kaggle url changes, change the URL to the correct web location of the data
    -------
    Returns:
    Nothing, only downloads the data and prints messages for the user to explain the function's behavior
    """
    downloaded_datasets = []
    boolean_list = []
    for i in dataset_list:
        if not os.path.exists('datasets/f1/' + i):
            downloaded_datasets.append(i)
            boolean_list.append(True)
    if force_download or any(boolean_list):
            # Use the Kaggle API to download the dataset
            kaggle.api.dataset_download_files(URL, path='datasets/f1', unzip=True)
    if force_download:
        print('Force download was deemed True, therefore all the datasets have been downloaded')
    if downloaded_datasets:
        print("The following datasets were missing and have been downloaded/updated:")
        for dataset in downloaded_datasets:
            print(f"- {dataset}")
    else:
        print("No missing datasets. The following datasets are available:")
        for dataset in dataset_list:
            if os.path.exists('datasets/f1/' + dataset):
                print(f"- {dataset}")
