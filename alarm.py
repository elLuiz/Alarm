import datetime
import os
import subprocess
import time
import json

hour = 0
minute = 0
seconds = 0
file_path = ""
process_path = ""
alarm_day = ""

time_now = datetime.datetime.now()
day = time_now.today().strftime("%A")
try:
    with open('configuration/config.json', 'r') as config_content:
        config_dict = json.load(config_content)

    file_path = config_dict['file_path']
    hour = config_dict['time_hour']
    minute = config_dict['time_minute']
    seconds = config_dict['time_second']    
    process_path = config_dict['process_path']	
    alarm_day = config_dict['day']	
except IOError as io:
    print("Could not open the configuration file")

try:
    alarm_time = datetime.datetime.combine(time_now.date(), datetime.time(hour, minute, seconds))
    if day in alarm_day:
        time.sleep((alarm_time - time_now).total_seconds())
        subprocess.Popen([process_path, file_path])
    else:
        pass
except ValueError as e:
    pass
except OSError:
    pass

