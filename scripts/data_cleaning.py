import pandas as pd
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class DataCleaner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        logging.info("Loading raw data...")
        self.df = pd.read_csv(self.file_path)

    def clean_data(self):
        logging.info("Cleaning data...")
        self.df.drop_duplicates(inplace=True)
        self.df.dropna(inplace=True)
        self.df['total'] = self.df['price'] * self.df['quantity']

    def save_cleaned_data(self, output_path):
        logging.info("Saving cleaned data...")
        self.df.to_csv(output_path, index=False)


if __name__ == "__main__":
    try:
        raw_path = "data/raw_ecommerce.csv"
        clean_path = "data/cleaned_ecommerce.csv"

        cleaner = DataCleaner(raw_path)
        cleaner.load_data()
        cleaner.clean_data()
        cleaner.save_cleaned_data(clean_path)

        logging.info("Data cleaning pipeline completed successfully.")

    except Exception as e:
        logging.error(f"Data cleaning failed: {e}")