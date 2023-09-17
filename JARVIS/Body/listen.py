# Hindi or English --> English

# Three Functions
#     - Listen
#     - Translate
#     - Connect

import speech_recognition as sr # pip intsall speechrecogniton / conda install -c conda-forge speechrecognition
from googletrans import Translator  # pip install googletrans


# 1 - Listen :Hindi or English
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(
            source, 0, 4
        )  # Jasrvis gets stuck in listening mode, so the 8 is to specify that if cuts the listening after every 8 seconds

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query).lower()
    return query  # Prints in hindi


# print(Listen())


# 2 - Translate
def TranslateHintoEng(Text):
    line = str(Text)
    translator = Translator()
    result = translator.translate(
        line, dest="en"
    )  # dest is used for result language, default is english only
    data = result.text
    print(f"You : {data}.")
    return data


# TranslateHintoEng("और जावेद भाई क्या हाल")


# 3 - Connect
def MicConnect():
    query = Listen()
    data = TranslateHintoEng(query)
    return data
