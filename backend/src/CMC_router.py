from fastapi import APIRouter
from src.cmc_client import cmc_client

router = APIRouter(
    prefix="/cryptocurrencies"
)


@router.get("", tags=["cryptocurrency"], summary="Get list of cryptocurrencies")
async def get_list():
    return await cmc_client.get_currency_list()



@router.get("/{currency_id}", tags=["cryptocurrency"], summary="Get particular cryptocurrency")
async def get_prtc_currency(currency_id: int):
    return await cmc_client.get_prtc_currency(currency_id = currency_id)