import os
import logging
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Optional API Keys (Production Use)
EIA_API_KEY = os.environ.get("EIA_API_KEY")
FRED_API_KEY = os.environ.get("FRED_API_KEY")


def fetch_eia_crude_imports() -> List[Dict[str, Any]]:
    """
    Returns energy import data.

    For the hackathon demo this function serves realistic mock data.
    In production, replace this with live EIA API integration.
    """

    if not EIA_API_KEY:
        logger.info("Using mock energy import dataset.")

        return [
            {
                "economy": "India",
                "source": "Saudi Arabia",
                "commodity": "Crude",
                "volume": 1850000,
            },
            {
                "economy": "India",
                "source": "Iraq",
                "commodity": "Crude",
                "volume": 1180000,
            },
            {
                "economy": "India",
                "source": "Qatar",
                "commodity": "LNG",
                "volume": 740000,
            },
            {
                "economy": "Japan",
                "source": "Qatar",
                "commodity": "LNG",
                "volume": 1480000,
            },
            {
                "economy": "Japan",
                "source": "UAE",
                "commodity": "Crude",
                "volume": 980000,
            },
            {
                "economy": "China",
                "source": "Russia",
                "commodity": "Crude",
                "volume": 2250000,
            },
            {
                "economy": "Germany",
                "source": "Norway",
                "commodity": "Crude",
                "volume": 920000,
            },
        ]

    logger.info("Production mode: replace with live EIA API integration.")
    return []


def fetch_fred_refinery_capacity() -> List[Dict[str, Any]]:
    """
    Returns refinery capacity data.

    For the hackathon demo this function serves realistic mock data.
    In production, replace this with live FRED API integration.
    """

    if not FRED_API_KEY:
        logger.info("Using mock refinery dataset.")

        return [
            {
                "economy": "India",
                "indicator": "Refinery Capacity",
                "value": 5100000,
            },
            {
                "economy": "Japan",
                "indicator": "Refinery Capacity",
                "value": 3400000,
            },
            {
                "economy": "China",
                "indicator": "Refinery Capacity",
                "value": 17500000,
            },
            {
                "economy": "Germany",
                "indicator": "Refinery Capacity",
                "value": 2100000,
            },
        ]

    logger.info("Production mode: replace with live FRED API integration.")
    return []


def validate_data(import_data: List[Dict[str, Any]],
                  refinery_data: List[Dict[str, Any]]) -> bool:
    """
    Basic validation for demo datasets.
    """

    if not import_data:
        logger.error("Energy import dataset is empty.")
        return False

    if not refinery_data:
        logger.error("Refinery dataset is empty.")
        return False

    logger.info("Dataset validation successful.")
    return True


def ingest_data():
    """
    Mock ingestion pipeline.

    Loads realistic datasets for the IDS calculation and AI agents.
    """

    logger.info("Starting ingestion pipeline...")

    import_data = fetch_eia_crude_imports()
    refinery_data = fetch_fred_refinery_capacity()

    if not validate_data(import_data, refinery_data):
        raise ValueError("Dataset validation failed.")

    logger.info(f"Loaded {len(import_data)} import records.")
    logger.info(f"Loaded {len(refinery_data)} refinery records.")

    return {
        "imports": import_data,
        "refinery": refinery_data,
    }


if __name__ == "__main__":
    data = ingest_data()

    logger.info("Mock ingestion completed successfully.")
    print(data)