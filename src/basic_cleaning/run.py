#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    #This is for GIT testing

    import wandb
    import pandas as pd
    import pandas_profiling
    
    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    run = wandb.init(project="nyc_airbnb", group="eda", save_code=True)
    local_path = wandb.use_artifact("sample.csv:latest").file()
    df = pd.read_csv(local_path)

    profile = pandas_profiling.ProfileReport(df)
    profile.to_widgets()

    args.min_price = 10
    args.max_price = 350
    idx = df['price'].between(args.min_price, args.max_price)
    df = df[idx].copy()

    df['last_review'] = pd.to_datetime(df['last_review'])

    df.to_csv("clean_sample.csv", index=False)

    artifact = wandb.Artifact(
         args.output_artifact,
         type=args.output_type,
         description=args.output_description,
    )
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)

    run.finish()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True,
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Fully-qualified name for the output artifact",
        required=True,
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="Dataframe",
        required=True,
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="Cleaned data for the price on NYV apartments",
        required=True,
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="Minimum price we're willing to pay for to rent a place",
        required=True,
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="Maximum price we're willing to pay for to rent a place",
        required=True,
    )


    args = parser.parse_args()

    go(args)
