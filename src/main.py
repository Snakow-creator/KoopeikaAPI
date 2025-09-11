from fastapi import FastAPI
from handlers import main, rates

import asyncio
import uvicorn

app = FastAPI()

app.include_router(main.router)
app.include_router(rates.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

