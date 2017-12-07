from crontab import CronTab
 
my_cron = CronTab(user='root')
job = my_cron.new(command='python /home/pi/ip.py')
job.minute.every(1)
 
my_cron.write()
