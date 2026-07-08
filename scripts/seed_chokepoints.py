import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MOCK_CHOKEPOINTS = [
    {
        "name": "Strait of Hormuz",
        "latitude": 26.5667,
        "longitude": 56.2500,
        "risk_level": 8
    },
    {
        "name": "Suez Canal",
        "latitude": 30.5852,
        "longitude": 32.2654,
        "risk_level": 5
    },
    {
        "name": "Strait of Malacca",
        "latitude": 1.4300,
        "longitude": 102.8900,
        "risk_level": 4
    },
    {
        "name": "Panama Canal",
        "latitude": 9.0800,
        "longitude": -79.6800,
        "risk_level": 3
    }
]

def seed_chokepoints():
    """
    Seed known global maritime chokepoints into the database.
    """
    logger.info("Seeding chokepoint data...")
    # In a real scenario, use psycopg2 to connect to Postgres and insert the records
    for cp in MOCK_CHOKEPOINTS:
        logger.info(f"Inserting {cp['name']} (Lat: {cp['latitude']}, Lon: {cp['longitude']}) with risk {cp['risk_level']}")
    
    # TODO: Implement actual DB insert using psycopg2
    logger.info("Seeding complete.")

if __name__ == "__main__":
    seed_chokepoints()
