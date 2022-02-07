# ML Pipeline for Short-term Rental Prices in NYC

- Project **ML Pipeline for Short-term Rental Prices in NYC** of ML DevOps Engineer Nanodegree Udacity

## Project Description

Using the starting code provided, we'll write a program tha uses MLFlow and WandB to predict the short term rental prices for AirBNB rentals in New York City

## Running Files

> git clone https://github.com/TimothyLMoore/nd0821-c2-build-model-workflow-starter.git
> cd nd0821-c2-build-model-workflow-starter
> conda env create -f environment.yml
> conda activate nyc_airbnb_dev

login to your Wandb (wandb login (API Key))

>  mlflow run .

This will run the entire pipeline, before you test the regression model you'll have to set tag your best model as "prod" on WandB the run.

> mlflow run . -P steps=test_regression_model

## Hyperparameters

test_size: 0.2
val_size: 0.2
random_seed: 42
stratify_by: "neighbourhood_group"
max_tfidf_features: 15
random_forest:
    n_estimators: 100
    max_depth: 15
    min_samples_split: 4
    min_samples_leaf: 3
    n_jobs: -1
    criterion: mae
    max_features: 0.5
    oob_score: true

Scores:
MAE = 33
R-Squared = 0.5594

## Submission Details

-Github Repository: https://github.com/TimothyLMoore/nd0821-c2-build-model-workflow-starter

-WandB Project: https://wandb.ai/timothylmoore/nyc_airbnb?workspace=user-timothylmoore
