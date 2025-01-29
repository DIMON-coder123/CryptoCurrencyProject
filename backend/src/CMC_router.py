from fastapi import APIRouter, HTTPException
from cmc_client import cmc_client

from logger import logger
router = APIRouter(
    prefix="/cryptocurrencies"
)


@router.get("", tags=["cryptocurrency"], summary="Get all of cryptocurrencies")
async def get_list():
    logger.info("Request to foreign API")
    return await cmc_client.get_all_currency()



@router.get("/{currency_id}", tags=["cryptocurrency"], summary="Get particular cryptocurrency")
async def get_prtc_currency(currency_id: int):
    logger.info("Request to foreign API")
    return await cmc_client.get_prtc_currency(currency_id = currency_id)