from gtts import gTTS
import os
import subprocess
import urllib2
from time import sleep
import json

team = '' #IT SERVICE MANAGEMENT GROUP SYS_ID
def text_to_voice(values):
	description = values["result"]["text"]
        if(description!=''):
		audio_file = "alerts.mp3"
        	tts = gTTS(text= description, lang="en")
        	tts.save(audio_file)
        	r = os.system("mpg321 "+audio_file)

def check_new_alerts():
        try:
                response = urllib2.urlopen()
                data = response.read()
                values = json.loads(data)
		return values
        except:
                return 0


def start_program():
        values  = check_new_alerts()
        if (values != 0):
                #print values
                text  = values["result"]["text"]
        	text_to_voice(values)
		#print text
	#text_to_voice(text)
        #else:
                ####log problem

############## START PROGRAM
while True:
        start_program()
        sleep(5)

