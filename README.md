# Alarm

This program simulates an alarm. To use it change the values in config.json.

# How does it work? 

After chaging the values in config.json, you are able to execute this program. <br/>
If the time in your computer is equal to the time seted in the configuration file, then the program will open a txt file.<br/>
PS: You can change process to be executed(e.g. to open image instead of 'gedit' use 'eog', for linux). <br/>
If time seted is greater than your machine time, then the process will be waiting until the condition above is satisfied. <br/>
If time seted is less than your machine time, then the program will be finished. <br/>

# How to compile?

Linux: python3 alarm.py <br/>
Windows: py alarm.py <br/>

# Important

Do not forget to use 24-hour format.
