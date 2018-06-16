from django_cron import CronJobBase, Schedule

class ServerStatus(CronJobBase):
    RUN_EVERY_MINS = 1 # every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        print("My Cron is working!")
        pass    # do your thing here