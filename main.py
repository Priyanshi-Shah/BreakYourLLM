from dotenv import load_dotenv
import os
import argparse

def main():

    parser = argparse.ArgumentParser(description="Script with configs and CLI args.")
    parser.add_argument("--config", type=str, help="Path to the config file.", default="config/.env", required=False)
    parser.add_argument("--file", type=str, help="Path to CSV file with guidelines.", default="data.csv", required=False)

    args = parser.parse_args()

    # Load the .env file
    load_dotenv(dotenv_path=args.config)

    from sources.generate_tests import run_pipeline
    run_pipeline(args.file)
    # generate_paraphrased_tests


if __name__ == "__main__":
    main()