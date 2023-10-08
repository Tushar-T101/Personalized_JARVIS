from Brain.Gpt import ReplyBrain
# from Brain.Bard import MainExecution
print("\n>> Starting Up Speak Function...\n")
from Body.speak import Speak
from Body.listen import Listen
from Features.clap import Tester

print("\n>> Done\n")


def MainExe():
    Speak("Hello Sir. I am JARVIS. Ready to assist you...")

    while True:
        Data = Listen()
        Data = str(Data)
        # print("1. Using ChatGPT\n2. Using Bard")
        # choice = input()
        # if choice == '1':
        reply = ReplyBrain(Data)

        # elif choice == '2':
        # reply = MainExecution(Data)

        # else:
        #     Speak("Invalid option")
        
        Speak(reply)


# def ClapDetect():
#     query = Tester()
#     if "True-Mic" in query:
#         MainExe()
#     else:
#         pass


# ClapDetect()

MainExe()