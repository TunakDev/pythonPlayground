from ollama import chat
from ollama import ChatResponse


import speech_recognition as sr
import pyttsx3


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("A moment of silence please!")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    # recognized_text = r.recognize_google(audio)
    recognized_text = r.recognize_google(audio, language="de-DE")

    print("Google Speech Recognition thinks you said " + recognized_text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print("Let's ask the model for an answer... ")
response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': recognized_text,
  },
])
# print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)

print("Sound is played now")
engine = pyttsx3.init()
engine.say(response.message.content)
engine.runAndWait()

