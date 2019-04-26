from apscheduler.schedulers.blocking import BlockingScheduler
import libraryScript
import script
sched = BlockingScheduler(timezone="America/New_York")
sched2 = BlockingScheduler(timezone="America/New_York")


@sched.scheduled_job('cron', hour=00)
def scheduled_job():
    libraryScript.bookRooms()
    script.bookRoom()

@sched2.scheduled_job('cron', hour=00,minute=10)
def scheduled_job():
    libScript2.bookRooms()
#    script.bookRoom()

sched.start()
sched2.start()
