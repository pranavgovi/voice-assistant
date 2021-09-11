# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import pyaudio
import pyttsx3
import speech_recognition as sr
import re

api_key = "tkHtxZ-gcftp"
proj_token = "tuCuCfjDCcw1"
run_token = "tuqLBOoLF0G-"


# response=requests.get(f'https://parsehub.com/api/v2/projects/{proj_token}/last_ready_run/data',params={"api_key":api_key})
# data = json.loads(response.text)
class Data:
    def __init__(self, api_key, proj_token):
        self.api_key = api_key
        self.proj_token = proj_token
        self.params = {
            "api_key": self.api_key
        }
        self.getdata()

    def getdata(self):
        response = requests.get(f'https://parsehub.com/api/v2/projects/{proj_token}/last_ready_run/data',
                                params=self.params)
        self.data = json.loads(response.text)
    def countryyy(self):
        g=[]
        for i in range(len(self.data['wc_winner'])):
            g.append(self.data['wc_winner'][i]['name'])
        return g



    def show_data(self):
        print(self.data)

    def get_winners(self):
        s = []
        k = []
        for i in range(len(self.data['wc_winner'])):
            s.append(self.data['wc_winner'][i]['name'])
            s.append(self.data['wc_winner'][i]['value'])
        return s

    def get_year(self, country):
        l = []
        s=["did not win"]
        for i in range(len(self.data['wc_winner'])):
            if (self.data['wc_winner'][i]['name'].lower() == country.lower()):
                l.append(self.data['wc_winner'][i]['value'])
        if (len(l) == 0):
            return s
        else:
            return l

    def get_team(self, year):
        k = int(year)
        for i in range(len(self.data['wc_winner'])):
            if (int(self.data['wc_winner'][i]['value']) == k):
                return self.data['wc_winner'][i]['name']
        else:
            return "world cup didnt happen"

    def wcyears(self):
        k = []
        for i in range(len(self.data['wc_winner'])):
            k.append(self.data['wc_winner'][i]['value'])
        return k

    def wayofwinning(self, year):
        k = int(year)
        for i in range(len(self.data['wc_winner'])):
            if (int(self.data['wc_winner'][i]['value']) == k):
                return self.data['wc_winner'][i]['winning_margin']
    def sayhello(self,name):
        return ("hello {} what can i do for u".format(name))
    def special(self):
        x="i provide interesting stats about cricket world cup...wanna hear?"
        return x
    def provide_details(self):
        p=["i can list world cup winners","i can provide you  the exact year in which a particular country won the world cup","i can also list the win margins","common ask one question"]
        return p
s = Data(api_key, proj_token)


# s.show_data()
# s.get_winners()
# x=s.get_year('south africa')
# print(x)
# a=s.get_team('1983')
# print(a)
# a=s.wayofwinning(2019)
# print(a)
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# speak("hello brother")
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception:", str(e))
    return said.lower()


# print(get_audio())
def main():
    print("started prog")
    s = Data(api_key, proj_token)
    country_list = s.countryyy()
    main_country_list=[]
    for i in country_list:
        main_country_list.append(i.split(" ",1))
    # print(main_country_list)
    # for j in country_list:
    #     print(j)
    p=s.wcyears()
    # print(p)
    users_list=['pranav','sachin','govind','saraswathy','saraswathi']



    end_pharse = "stop"
    country_pattern = {
        re.compile("[\w\s]+country [\w\s]+world cup [\w\s]+[0-9][0-9][0-9][0-9]"): lambda year: s.get_team(year),
        re.compile("[\w\s]+ year [0-9][0-9[0-9][0-9]+[\w\s]+world cup"): lambda year: s.get_team(year),
        re.compile("who [\w\s]+world cup [\w\s]+year [0-9][0-9][0-9][0-9]"):lambda year: s.get_team(year)

    }

    year_pattern = {
        re.compile("[\w\s] year + [\w\s]+world cup+[\D]"): lambda country: s.get_year(country),
        re.compile("[\w\s]+win [\w\s]+ world cup"): lambda country: s.get_year(country)
    #     re.compile("[\w\s]+year [^\d{4}$] +[\w\s] +country [\w\s]+world cup"): lambda year: Data.get_team(year)
    }
    winner_pattern = {
        re.compile("[\w\s]+countries [\w\s]+world cup"): s.get_winners
        # re.compile("world cup [\w\s]+world cup"):Data.get_team
    }
    user_pattern={
        re.compile("[\w\s]+alexa [\w\s]+"):lambda name:s.sayhello(name)
    }
    speciality={
        re.compile("what [\w\s]+speciality"):s.special,
        re.compile("what do you do"):s.special
    }
    respond_pattern={
        re.compile("yes"):s.provide_details
    }
    while True:
        print("listening")
        x_count=0
        text = get_audio()
        print(text)
        key=None
        for pattern,func in country_pattern.items():
            if pattern.match(text):
                yearsss=text.split()
                for year in p:
                    if year in yearsss:
                        key=func(str(year))
                        print(key)
                        speak(key)
        for pattern,func in speciality.items():
            if pattern.match(text):
                key=func()
                print(key)
                speak(key)
        for pattern, func in year_pattern.items():
            if pattern.match(text):
                words = text.split()
                for count in main_country_list:
                    if(x_count<1):

                        if count[0].lower() in words:
                            key = func(str(" ".join(count)))
                            x_count=1
                            print(key)
                            speak(key)
                            break
                else:
                    if(x_count<1):
                        x_count=1
                        print("didnt win")
                        speak("didnt win")
        for pattern,func in respond_pattern.items():
            if pattern.match(text):
                key=func()
                for i in range(len(key)):
                    print(key[i])
                    speak(key[i])

        for pattern, func in winner_pattern.items():
            if pattern.match(text):
                key = func()
                print(key)
                for i in range(len(key)):
                    print(key[i])
                    speak(key[i])

        for pattern,func in user_pattern.items():
            if pattern.match(text):
                namess=text.split()
                for i in users_list:
                    if i.lower() in namess:
                        key=func(i)
                        print(key)
                        speak(key)


        # if key:
        #     print(key)
        #     speak(key)
        if text.find(end_pharse) != -1:
            break


main()
