  GNU nano 2.5.3                  File: text_watchdog.py                                 Modified  

import os
from time import sleep

global counter
counter = 0
def start_program():
        process = os.popen("pgrep -af python").readlines()
        found = 0
        for index in range(len(process)):
                result = process[index].replace("\n"," ").replace("\r"," ")
                running = result.find('check_alerts.py')
                if(running>-1):
                        found = 1
        return found
while True:
        found =start_program()
        if(found==0):
                counter +=1
        else:
                counter = 0
        if(counter>12):
                os.system('reboot')
        sleep(5)
