from fastapi import APIRouter

import rates.static_rates as sr

router = APIRouter()


@router.get(
    "/rates",
    tags=["API🛠"],
    summary="Получить курсы валют",
    description="<h1>Получает все курсы валют</h1>",
)
async def get_rates(symbol: str = None):
    if symbol:
        if symbol.endswith("USDT"):
            symbol = symbol[:-1]
        return {symbol: sr.rates[symbol]}
    return sr.rates


@router.get(
    "/rates/top_cryptorates",
    tags=["API🛠"],
    summary="Получить топ курсов валют",
    description="<h1>Получает топ курсов валют</h1>",
)
async def get_top_rates():
    return sr.top_rates
