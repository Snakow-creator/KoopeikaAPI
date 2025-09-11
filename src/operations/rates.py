import aiohttp
import asyncio
import xml.etree.ElementTree as ES

from config import NBK_API, CRYPTO_API, CRYPTO_TOP_API


async def get_exchange_fiat_rates():
    rates = {"KZTUSD": 1}
    async with aiohttp.ClientSession() as session:
        url = NBK_API
        async with session.get(url) as res:
            if res.status == 200:
                res = await res.text()
                root = ES.fromstring(res)
                items = root.find("channel").findall("item")
                for item in items:
                    value = item.findtext("title")
                    if value == "USD":
                        rates["USD"] = float(item.findtext("description"))
                        continue
                    rates[value + "USD"] = float(item.findtext("description"))
                return rates
            else:
                return {
                    "ok": False,
                    "status": res.status,
                    "message": "fiatrates is not ended",
                }


async def get_usdt_fiat_rates():
    rates = await get_exchange_fiat_rates()
    for key in rates.keys():
        if key == "USD":
            continue
        from_currency = rates["USD"]
        to_currency = rates[key]
        rates[key] = float((1 / from_currency) * to_currency)
    static_rates = {
        "USD": 1.0,
        "⭐️BUYUSD": 0.15,
        "⭐️SELLUSD": 0.13,
    }
    return rates | static_rates


async def get_cryptorates():
    async with aiohttp.ClientSession() as session:
        url = CRYPTO_API
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                crates = {
                    c["symbol"][:-1]: float(c["price"])
                    for c in data
                    if c["symbol"].endswith("USDT") and float(c['price']) > 0
                }
                return crates
            return {
                "ok": False,
                "status": response.status,
                "message": "cryptorates is not ended",
            }


async def get_top_cryptorates():
    async with aiohttp.ClientSession() as session:
        url = CRYPTO_TOP_API
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                crates = {
                    c["symbol"][:-1]: float(c["lastPrice"])
                    for c in data
                    if c["symbol"].endswith("USDT") and float(c["lastPrice"]) > 0
                }
                return crates
            return {
                "ok": False,
                "status": response.status,
                "message": "cryptorates is not ended",
            }


if __name__ == "__main__":
    loop = asyncio.run(get_cryptorates())
