"""Shared configuration for the COS802 Ames Housing project."""
from pathlib import Path
SEED=16153970
TARGET="SalePrice"
IDENTIFIERS=["Order","PID"]
PROJECT_DIR=Path("/content/drive/MyDrive/MIT BIG DATA SCIENCE/COS802_PROJECT")
RAW_DIR=PROJECT_DIR/"data"/"raw"; PROCESSED_DIR=PROJECT_DIR/"data"/"processed"
SPLITS_DIR=PROJECT_DIR/"data"/"splits"; FIGURES_DIR=PROJECT_DIR/"figures"
DATA_FILE=RAW_DIR/"AmesHousing.txt"
def ensure_output_dirs():
    for p in (PROCESSED_DIR,SPLITS_DIR,FIGURES_DIR): p.mkdir(parents=True,exist_ok=True)
