from apscheduler import AsyncScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from rates.upload_rates import upload_all_rates, upload_rates, upload_top_cryptorates


async def start_scheduler():
    async with AsyncScheduler() as scheduler:
        await upload_all_rates()
        await scheduler.add_schedule(upload_rates, CronTrigger(hour=0, minute=0), id="upload_rates")
        await scheduler.add_schedule(upload_top_cryptorates, IntervalTrigger(minutes=5), id="upload_top_cryptorates")

