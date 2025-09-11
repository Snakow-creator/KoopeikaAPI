import os

from dotenv import load_dotenv

load_dotenv()

NBK_API = os.getenv("NBK_API")
CRYPTO_API = os.getenv("CRYPTO_API")
CRYPTO_TOP_API = os.getenv("CRYPTO_TOP_API")
