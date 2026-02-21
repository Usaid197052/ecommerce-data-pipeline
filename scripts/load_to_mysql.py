import pandas as pd
import logging
from sqlalchemy import create_engine

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

USERNAME = "root"
PASSWORD = "usaid123"   # Replace this
HOST = "localhost"
DATABASE = "ecommerce_db"

if __name__ == "__main__":
    try:
        logging.info("Connecting to MySQL...")

        engine = create_engine(
            f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
        )

        logging.info("Reading cleaned CSV file...")
        df = pd.read_csv("data/cleaned_ecommerce.csv")

        logging.info("Loading data into MySQL...")
        df.to_sql("orders", engine, if_exists="replace", index=False)

        logging.info("Data successfully loaded into MySQL.")

    except Exception as e:
        logging.error(f"MySQL load failed: {e}")