from gtts import gTTS
import os
import subprocess
import urllib2
from time import sleep
import json
import base64
import pygame
import socket
team = 'ce71779413cc76005da23927d144b0df' #ITOC GROUP
sleep_timer = 5
global reboot_count
reboot_count =0
def text_to_voice(values):
        description = values["result"]["text"]
        volume = float(values["result"]["volume"])
        global sleep_timer
        sleep_timer = values["result"]["sleep_timer"]
        if(description!=''):
                audio_file = "alerts.mp3"
                tts = gTTS(text= description, lang="en")
                tts.save(audio_file)
                #r = os.system("mpg321 "+audio_file)
                pygame.mixer.init()
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                        continue

def check_new_alerts():
        try:
                pi_address = os.popen('hostname -I').readlines()[0]
                pi_address = pi_address.replace("\n"," ").replace("\r"," ")
                #print pi_address
                response = urllib2.urlopen("https://spiritairlinesdev.service-now.com/api/sa/light$
                data = response.read()
                values = json.loads(data)
                return values
        except:
                return 0

def internet_on():
        try:
                urllib2.urlopen('https://www.google.com',timeout=1)
                return 1
        except:
                return 0


def start_program():
        internet = internet_on()
        global reboot_count
        if(internet==1):
                reboot_count = 0
                #print reboot_count
                values  = check_new_alerts()
                if (values != 0):
                        #print values
                        text  = values["result"]["text"]
                        text_to_voice(values)
        else:
                reboot_count +=1
                #print reboot_count
        return reboot_count
############## START PROGRAM
while True:
        reboot = start_program()
        reboot = reboot*float(sleep_timer)
        if(reboot>80):
          os.system("reboot")
        sleep(sleep_timer)

