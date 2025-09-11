from fastapi import APIRouter

from operations.rates import get_usdt_fiat_rates, get_cryptorates, get_top_cryptorates

router = APIRouter()


@router.get("/rates")
async def get_rates(symbol: str = None):
    try:
        fiat_rates = await get_usdt_fiat_rates()
        crypto_rates = await get_cryptorates()
        rates = fiat_rates | crypto_rates
        if symbol:
            if symbol.endswith("USDT"):
                symbol = symbol[:-1]
            return {symbol: rates[symbol]}
        return rates
    except KeyError:
        return {"ok": False, "message": "value is not found"}


@router.get("/rates/top_cryptorates")
async def get_top_rates():
    return await get_top_cryptorates()


