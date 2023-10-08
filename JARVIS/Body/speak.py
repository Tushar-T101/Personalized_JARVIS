# Speak Functions - 2
#   - Windows Based - pip install pyttsx3
#   - Chrome Based - pip install selenium==4.1.3


# Windows Based - fast, offline, cannot cut while speaking, less voices.
# import pyttsx3


# def Speak(Text):
#     engine = pyttsx3.init("sapi5")  # sapi5 is windows api to get voices
#     voices = engine.getProperty("voices")
#     engine.setProperty("voices", voices[1].id)
#     engine.setProperty("rate", 170)
#     print("")
#     print(f"You: {Text}.")
#     print("")
#     engine.say(Text)
#     # engine.save_to_file('')  # in order to track the communication, but slows the process
#     engine.runAndWait()


# Speak("Hello Sir")


# Chrome Based - Lots of voices, Can cut while speaking, online only, daily words spoken limit because of link used
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Stop selenium tips from appearing
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless=new')  # chrome will open but won't be visible
service = Service(executable_path=r'Database\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
driver.maximize_window()  # to maximize chrome window


buttonSelection = Select(
    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[2]/form/select")
)
buttonSelection.select_by_visible_text("British English / Brian")


def Speak(Text):
    lengthOfText = len(str(Text))
    if lengthOfText == 0:
        pass
    else:
        print("")
        print(f"Jarvis : {Text}.")
        print("")
        Data = str(Text)
        xpathofsec = "/html/body/div[4]/div[2]/form/textarea"
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(
            By.XPATH, value="/html/body/div[4]/div[2]/form/textarea"
        ).clear()

        if lengthOfText >= 30:
            sleep(4)

        elif lengthOfText >= 40:
            sleep(6)

        elif lengthOfText >= 55:
            sleep(8)

        elif lengthOfText >= 70:
            sleep(10)

        elif lengthOfText >= 100:
            sleep(13)

        elif lengthOfText >= 120:
            sleep(14)

        else:
            sleep(2)


# Speak("Hello Sir")
