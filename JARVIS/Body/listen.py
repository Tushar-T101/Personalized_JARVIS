# # Hindi or English --> English

# # Three Functions
# #     - Listen
# #     - Translate
# #     - Connect

# import speech_recognition as sr # pip intsall speechrecogniton / conda install -c conda-forge speechrecognition
# # from googletrans import Translator  # pip install googletrans

# # 3 - Connect
# # def MicConnect():
#     # query = Listen()
#     # data = TranslateHintoEng(query)
#     # return data


import speech_recognition as sr

def Listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, 0,4) # Jarvis gets stuck in listening mode, so the 8 is to specify that if cuts the listening after every 8 seconds

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        query = str(query).lower()
        print(f'You: {query}')

        # Add an exit command
        if "that's it" in query:
            print("Exiting the program.")
            return None

        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand you.")
    except sr.RequestError as e:
        print(f"Sorry, there was an error connecting to the Google API: {e}")

# while True:
#     query = listen()

