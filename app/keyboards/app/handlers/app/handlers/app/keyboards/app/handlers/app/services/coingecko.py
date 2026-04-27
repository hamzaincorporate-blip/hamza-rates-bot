import aiohttp

from app.data.assets import ASSETS


async def get_prices(selected_tickers: list[str]):
    ids = [ASSETS[ticker] for ticker in selected_tickers if ticker in ASSETS]
    ids_string = ",".join(ids)

    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={ids_string}"
        "&vs_currencies=usd"
        "&include_24hr_change=true"
        "&include_last_updated_at=true"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as response:
            return await response.json()
