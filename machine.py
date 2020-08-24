#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
import ex2_getVoice2Text as STT
import requests
import ex4_getText2VoiceStream as TTS
import RPi.GPIO as GPIO
import MicrophoneStream as MS


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.OUT)
btn_status = False

# 
def classify(text):
    key = "a812b8a0-baa9-11ea-8f05-a7dc2583c606a88b2bd5-df7b-45ae-816d-74c558475ae7"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def callback(channel):  
	print("falling edge detected from pin {}".format(channel))
	global btn_status
	btn_status = True
	print(btn_status)


def main():
        global btn_status
        GPIO.add_event_detect(29, GPIO.FALLING, callback=callback, bouncetime=10)
        while True:
            if (btn_status == True):
            # CHANGE THIS to something you want your machine learning model to classify
                data = STT.getVoice2Text()
                demo = classify(data)

                label = demo["class_name"]
                confidence = demo["confidence"]
                print(label)

                if (label == 'google'):
                    MS.play_file("../../Desktop/mp3/google.wav")
                    btn_status = False
                if (label == 'weather'):
                    MS.play_file("../../Desktop/mp3/weather.wav")
                    btn_status = False
                if (label == 'rain'):
                    MS.play_file("../../Desktop/mp3/rain.wav")
                    btn_status = False
                if (label == 'dust'):
                    MS.play_file("../../Desktop/mp3/dust.wav")
                    btn_status = False
                if (label == 'date'):
                    MS.play_file("../../Desktop/mp3/date.wav")
                    btn_status = False
                if (label == 'time'):
                    MS.play_file("../../Desktop/mp3/time.wav")
                    btn_status = False
                if (label == 'music'):
                    MS.play_file("../../Desktop/mp3/music.wav")
                    btn_status = False
                if (label == 'pre'):
                    MS.play_file("../../Desktop/mp3/pre.wav")
                    btn_status = False
                if (label == 'stop'):
                    MS.play_file("../../Desktop/mp3/stop.wav")
                    btn_status = False
                if (label == 'up'):
                    MS.play_file("../../Desktop/mp3/up.wav")
                    btn_status = False
                if (label == 'down'):
                    MS.play_file("../../Desktop/mp3/down.wav")
                    btn_status = False
	

if __name__ == '__main__':
	main()