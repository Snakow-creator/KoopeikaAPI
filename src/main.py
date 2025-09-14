from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.__init__ import init_router
from schedulers.__init__ import start_scheduler

import asyncio
import uvicorn

app = FastAPI()


async def main():
    await start_scheduler()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )
    app.include_router(init_router)



if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app, host="0.0.0.0", port=8000)

