Classification of vector images
==============================

### Machine learning and Data-science project - OsloMET 2018

#### Group members
| Name | email |
| ------------- | ------------- |
| Sondre Halvorsen | s305349@oslomet.no |
| Andre Fagereng  | s182417@oslomet.no |
| Bendik Mørk Jørgensen | s301100@oslomet.no  |

### Project Background
We have recently at OsloMet gathered a dataset for vector graphical 
images. These images are in the public domain and uploaded by artists 
and designers. The type of data is SVG, AI, and EPS.
Although there are several published datasets for vector graphics, this 
is the first dataset for general vector graphics. The dataset contains 
almost 250 thousand images and is to our knowledge the first and 
largest dataset of its type. The dataset is not yet published.

### Project Aim
In this project we want to explore whether the dataset is suitable for 
standard classification of vector graphics images. Vector graphical 
imagery is different to raster images and we want to investigate the 
performance of standard classification for raster images used with 
vector images.

### Key activities:

 - Use a current framework for machine learning to setup classifiers for raster and vector images

 - Test the performance on the classifiers for our labels (these are noisy labels supplied by uploaders via “tags”)

 - Test the performance across different “categories”, such as abstract imagery, cards, objects etc.

 - If time, explore approaches to deal with the “level of noise” in the labels
 
### Final deliverable 
Case report outlining the method used and the result on classification. 
This is part of a research project and it is expected that the work is 
incorporated into a scientific article.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
