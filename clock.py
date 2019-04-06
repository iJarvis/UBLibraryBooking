from apscheduler.schedulers.blocking import BlockingScheduler
import libraryScript
sched = BlockingScheduler(timezone="America/New_York")

@sched.scheduled_job('cron', hour=1,minutes=21)
def scheduled_job():
    libraryScript.bookRooms()

sched.start()