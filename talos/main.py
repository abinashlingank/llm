class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY


openai.api_key = API_KEY

engine = pyttsx3.init()
engine.setProperty("voice",0.7)
sound = engine.getProperty("voices")
engine.setProperty("voice",sound[1].id)


r= sr.Recognizer()
mic = sr.Microphone(device_index=0)
#print(sr.Microphone.list_microphone_names())
print(style.MAGENTA)
print("Hello there!! i am ruby, talos's personal assistant")
print(style.RESET)
engine.say("Hello there!! i am ruby, talos's personal assistant")
engine.runAndWait()


conversation = """

"""
user_name = "user"
while True:
    with mic as source:
        print(style.CYAN)
        print("\nlistening... speak clearly into mic.")
        print(style.RESET)
        #below code will only consider voice of higher thershold values
        r.adjust_for_ambient_noise(source, duration=0.5)
        #listening format
        audio = r.listen(source)
    # print(audio)
    print(style.CYAN)
    print("no longer listening.\n")
    print(style.RESET)

    try:
        #converting voice into text format
        user_input = r.recognize_google(audio)
        print(style.YELLOW)
        print(user_input)
        print(style.RESET)
    except:
        continue
    if user_input == "exit":
        print(style.GREEN)
        print("Bye sir, have a nice day")
        print(style.RESET)
        engine.say("Bye sir, have a nice day")
        engine.runAndWait()
        break

    prompt = user_name + ": " + user_input + "\n ruby:"
    conversation += prompt

    response = openai.Completion.create(engine='text-davinci-001', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("ruby: ", 1)[0]


    conversation += response_str + "\n"
    print(style.RED)
    print(response_str)
    print(style.RESET)

    engine.say(response_str)
    engine.runAndWait()