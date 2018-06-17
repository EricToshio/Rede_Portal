from django_cron import CronJobBase, Schedule
import ipgetter

class ServerStatus(CronJobBase):
    RUN_EVERY_MINS = 1 # every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):# do your thing here
        ip = ipgetter.myip()
        print("My Cron is working!")
        print("your ip is: ", ip)
        