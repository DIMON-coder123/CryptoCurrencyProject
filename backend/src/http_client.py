from aiohttp import ClientSession


class HTTPClient:
    def __init__(self, url: str, api_key: str):
        self._session = ClientSession(
            base_url = url,
            headers= {
                "X-CMC_PRO_API_KEY": api_key,
            }

        )


class CMCHTTPClient(HTTPClient):
    async def get_currency_list(self):
        async with self._session.get('/v1/cryptocurrency/listings/latest') as response:
            listening = await response.json()
            return listening["data"]


    async def get_prtc_currency(self, currency_id: int):
        async with self._session.get('/v2/cryptocurrency/quotes/latest',
                                     params = {"id": currency_id,}) as response:
            listening = await response.json()
            return listening["data"][str(currency_id)]