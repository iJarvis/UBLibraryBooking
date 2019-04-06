from apscheduler.schedulers.blocking import BlockingScheduler
import libraryScript
sched = BlockingScheduler(timezone="America/New_York")

@sched.scheduled_job('cron', hour="01:18")
def scheduled_job():
    libraryScript.bookRooms()

sched.start()