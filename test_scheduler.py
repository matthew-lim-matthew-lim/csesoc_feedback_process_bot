import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

async def my_task():
    print(f"Task executed at {datetime.now()}")

def main():
    scheduler = AsyncIOScheduler()
    # Schedule the task to run every day at a specific time (e.g., 14:30)
    scheduler.add_job(my_task, 'cron', hour=1, minute=14)
    scheduler.start()

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == "__main__":
    main()
