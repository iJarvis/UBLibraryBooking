from apscheduler.schedulers.blocking import BlockingScheduler
import libraryScript
import libScript2
import script
sched = BlockingScheduler(timezone="America/New_York")
sched2 = BlockingScheduler(timezone="America/New_York")

@sched.scheduled_job('cron', hour=00,minute=49)
def scheduled_job():
    libraryScript.bookRooms()
    script.bookRoom()

@sched.scheduled_job('cron', hour=00,minute=50)
def scheduled_job():
    libScript2.bookRooms()
    # script.bookRoom()

sched.start()
