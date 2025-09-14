from rates.get_rates import get_full_rates, get_top_cryptorates
import rates.static_rates as sr


async def upload_all_rates():
    sr.rates = await get_full_rates()
    sr.top_rates = await get_top_cryptorates()


async def upload_rates():
    sr.rates = await get_full_rates()


async def upload_top_cryptorates():
    sr.top_rates = await get_top_cryptorates()
