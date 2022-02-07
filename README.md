# ML Pipeline for Short-term Rental Prices in NYC

- Project **ML Pipeline for Short-term Rental Prices in NYC** of ML DevOps Engineer Nanodegree Udacity

## Project Description

Using the starting code provided, we'll write a program tha uses MLFlow and WandB to predict the short term rental prices for AirBNB rentals in New York City

## Running Files

> git clone https://github.com/TimothyLMoore/nd0821-c2-build-model-workflow-starter.git
> cd nd0821-c2-build-model-workflow-starter
> conda env create -f environment.yml
> conda activate nyc_airbnb_dev

login to your Wandb

>  mlflow run .

This will run the entire pipeline, before you test the regression model you'll have to set tag your best model as "prod" on WandB the run.

> mlflow run . -P steps=test_regression_model

## Submission Details

-Github Repository: https://github.com/TimothyLMoore/nd0821-c2-build-model-workflow-starter

-WandB Project: https://wandb.ai/timothylmoore/nyc_airbnb?workspace=user-timothylmoore
