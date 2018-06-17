from django_cron import CronJobBase, Schedule
import ipgetter
import json

class ServerStatus(CronJobBase):
    RUN_EVERY_MINS = 1 # every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):# do your thing here
        #get ip
        ip = ipgetter.myip()
        with open('redecasd_info.json') as f:
            data = json.load(f)

        atual = data['redecasd_status']['origin']

        change = False

        if ip == '161.24.24.1':
            if atual != 'ITA':
                data['redecasd_status']['origin'] = 'ITA'
                change = True 
        elif ip == '191.242.240.146':
            if atual != 'HORIZON':
                data['redecasd_status']['origin'] = 'HORIZON'
                change = True
        else:
            if atual != 'SEM REDE':
                data['redecasd_status']['origin'] = 'SEM REDE'
                change = True

        if change:
            with open('redecasd_info.json', 'w') as outfile:
                json.dump(data, outfile)

