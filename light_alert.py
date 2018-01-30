
from gtts import gTTS
import os
import subprocess
import urllib2
from time import sleep
import json

blink1_tool = 'blink1-tool'
def text_to_voice():
	audio_file = "alerts.mp3"
	tts = gTTS(text="You have two new alerts in servicenow", lang="en")
	tts.save(audio_file)
	r = os.system("mpg321 "+audio_file)

def change_light_state(color):
	print color
	cmd = blink1_tool + ' --rgb '+ "\'"+color+"\'"
        print "cmd: "+ cmd
        os.popen( cmd)


def check_new_alerts():
	try:
		response = urllib2.urlopen("https://spiritairlinesdev.service-now.com/api/sa/light_alerts?serial_number=2000AD2",timeout=5)
        	data = response.read()
        	values = json.loads(data)
		return values
	except:
		return 0


def start_program():
	internet = check_new_alerts()
	values  = check_new_alerts()
	if (values != 0):
		#print values
		color = values["result"]["color"]
                text  = values["result"]["text"]
		change_light_state(color)
		#text_to_voice(text)
	#else:
		####log problem

############## START PROGRAM
while True:
	start_program()
	sleep(5)
