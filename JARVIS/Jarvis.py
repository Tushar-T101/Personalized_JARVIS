from Brain.AIBrain import ReplyBrain

print("\n>> Starting Up Speak Function...\n")
from Body.speak import Speak
from Body.listen import MicConnect
from Features.clap import Tester

print("\n>> Done\n")
from Brain.QnA import QuestionsReplier


def MainExe():
    Speak("Hello Sir.\nI am JARVIS. Ready for you...")

    while True:
        Data = MicConnect()
        Data = str(Data)
        if (
            "what is" in Data
            or "where is" in Data
            or "question" in Data
            or "answer" in Data
        ):
            reply = QuestionsReplier(Data)

        else:
            reply = ReplyBrain(Data)
        Speak(reply)


def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        MainExe()
    else:
        pass


ClapDetect()
