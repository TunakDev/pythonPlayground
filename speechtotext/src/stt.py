#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import os

import speech_recognition as sr
import pyttsx3
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("A moment of silence please!")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recognized_text = r.recognize_google(audio, language="de-DE")

    print("Google Speech Recognition thinks you said " + recognized_text)

    engine = pyttsx3.init()
    engine.say(recognized_text)
    engine.runAndWait()


except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))