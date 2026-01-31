import os
from binance.client import Client
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class BinanceClientWrapper:
    def __init__(self):
        # Load API credentials from environment variables
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_SECRET")
        
        if not self.api_key or not self.api_secret:
            logger.error("API credentials missing in .env")
            raise EnvironmentError("Missing API Key or Secret")

        # Initialize Client with Testnet=True for testing purposes
        try:
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            logger.info("Binance Testnet Client Initialized Successfully")
        except Exception as e:
            logger.error(f"Failed to initialize client: {e}")
            raise

    def get_client(self):
        return self.client