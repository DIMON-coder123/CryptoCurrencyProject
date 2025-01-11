from src.config import settings
from src.http_client import CMCHTTPClient

cmc_client = CMCHTTPClient(
    url="https://pro-api.coinmarketcap.com",
    api_key=settings.API_KEY
)