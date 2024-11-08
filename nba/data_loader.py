import click
import kaggle  # Import Kaggle API library
import os

@click.command()
@click.option('--username', '-u', required=True, help="Your Kaggle username")
@click.option('--api_key', '-k', required=True, help="Your Kaggle API key")
@click.option('--dataset', '-d', required=True, help="Dataset name to download")
def main(username, api_key, dataset):
    # Print the provided arguments to verify
    print(f"Username: {username}")
    print(f"API Key: {api_key}")
    print(f"Dataset: {dataset}")

    # Ensure the 'data' folder exists
    if not os.path.exists('data'):
        os.makedirs('data')

    # Download the dataset to the 'data' folder and unzip
    try:
        kaggle.api.authenticate()  # Authenticate using the .kaggle/kaggle.json file
        kaggle.api.dataset_download_files(dataset, path='data/', unzip=True)
        print("Data downloaded and unzipped into the 'data/' folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
