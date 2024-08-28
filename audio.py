"""
Ref: 
https://peaceful0907.medium.com/%E7%B0%A1%E6%98%93%E8%AA%9E%E9%9F%B3%E5%8A%A9%E7%90%86%E5%AF%A6%E5%81%9A-5f6228937116
https://pypi.org/project/pyttsx3/
https://www.codegym.tech/blog/python-text-to-speech
"""

import speech_recognition as sr
from gtts import gTTS
from pygame import mixer 
import tempfile
import time
import pyttsx3


# func: speach2text
def STT():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    return r.recognize_google(audio, language = 'zh-tw')


# func: text2speech, Google version
def TTS_google(texts,lang='zh-tw'):
    mixer.init()

    with tempfile.NamedTemporaryFile(delete=True) as fp:
        filename = "{}.mp3".format(fp.name)

        tts = gTTS(text=texts,lang=lang)
        tts.save(filename)

        mixer.music.load(filename)

        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)


# func: text2speech, Python package
def TTS_py(texts):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  

    engine.say(texts)
    engine.runAndWait()


if __name__ == '__main__':
    print('請說話:')

    s = STT()
    print(s)

    TTS_py(s)