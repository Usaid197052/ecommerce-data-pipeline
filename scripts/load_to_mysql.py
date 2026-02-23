import pandas as pd
import logging
from sqlalchemy import create_engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

USERNAME = "root"
PASSWORD = "usaid123"
HOST = "localhost"
DATABASE = "ecommerce_db"

if __name__ == "__main__":
    try:
        logging.info("Connecting to MySQL...")

        engine = create_engine(
            f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
        )

        logging.info("Connection established.")

        
        logging.info("Reading raw CSV file...")
        raw_df = pd.read_csv("data/raw_ecommerce.csv")

        logging.info("Loading raw data into MySQL...")
        raw_df.to_sql("raw_orders", engine, if_exists="replace", index=False)

        logging.info("Raw data loaded successfully.")

    
        logging.info("Reading cleaned CSV file...")
        clean_df = pd.read_csv("data/cleaned_ecommerce.csv")

        logging.info("Loading cleaned data into MySQL...")
        clean_df.to_sql("cleaned_orders", engine, if_exists="replace", index=False)

        logging.info("Cleaned data loaded successfully.")

    except Exception as e:
        logging.error(f"MySQL load failed: {e}")
