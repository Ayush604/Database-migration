

from apscheduler.schedulers.blocking import BlockingScheduler
from migration import migrator

def job_function():
    migrator(client, host, "friends", clientEngine, hostEngine) ## table name



sched = BlockingScheduler()

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
sched.add_job(job_function, 'cron', month='august',day='monday',hour=' 'second='10')

sched.start()
hostConnectionString.close()
clientConnectionString.close()
