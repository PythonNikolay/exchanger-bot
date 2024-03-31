import aiohttp

async def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    if "error" in data:
        print("Error:", data["error"])
        return None

    return data["rates"][target_currency]
