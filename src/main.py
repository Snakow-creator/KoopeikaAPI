from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler import AsyncScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from contextlib import asynccontextmanager

from api.__init__ import init_router

from rates.upload_rates import upload_all_rates, upload_rates, upload_top_cryptorates

import uvicorn


@asynccontextmanager
async def main(app: FastAPI):
    async with AsyncScheduler() as scheduler:
        # actions on startup
        await upload_all_rates()

        await scheduler.start_in_background()
        await scheduler.add_schedule(upload_rates, CronTrigger(hour=0, minute=0), id="upload_rates")
        await scheduler.add_schedule(upload_top_cryptorates, IntervalTrigger(minutes=5), id="upload_top_cryptorates")
        yield
        # actions on shutdown
        print("KoopeikaAPI is stopped")


app = FastAPI(lifespan=main)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    )
app.include_router(init_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

