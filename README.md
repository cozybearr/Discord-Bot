# Personal Discord Music bot

![Status badge](https://img.shields.io/badge/Status-Archived-important)

**Update**(30 Nov. 2021): Try using Selenium to do Youtube scrapping for video link

## Dataset Information

A trivial bot to play music and other trivial stuff 😇

## Requirements

There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.

- `discord`
- `asyncio`
- `pytube`
- `json`

The library requirements specific to some methods are:

- `keras` with `TensorFlow` backend for Logistic Regression, MLP, RNN (LSTM), and CNN.
- `xgboost` for XGBoost.

**Note**: It is recommended to use Replit for deploying bot

## Usage

### Preprocessing

1. Run `preprocess.py <raw-csv-path>` on both train and test data. This will generate a preprocessed version of the dataset.
2. Run `stats.py <preprocessed-csv-path>` where `<preprocessed-csv-path>` is the path of csv generated from `preprocess.py`. This gives general statistical information about the dataset and will two pickle files which are the frequency distribution of unigrams and bigrams in the training dataset.

After the above steps, you should have four files in total: `<preprocessed-train-csv>`, `<preprocessed-test-csv>`, `<freqdist>`, and `<freqdist-bi>` which are preprocessed train dataset, preprocessed test dataset, frequency distribution of unigrams and frequency distribution of bigrams respectively.

For all the methods that follow, change the values of `TRAIN_PROCESSED_FILE`, `TEST_PROCESSED_FILE`, `FREQ_DIST_FILE`, and `BI_FREQ_DIST_FILE` to your own paths in the respective files. Wherever applicable, values of `USE_BIGRAMS` and `FEAT_TYPE` can be changed to obtain results using different types of features as described in report.

## Information about other files

- `scrapping.py`: Youtube scrapping
- `ytvids.py`: Download `.mp3` files
