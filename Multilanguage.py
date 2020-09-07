import speech_recognition as sr
import requests as r
from bs4 import BeautifulSoup as bs
from googletrans import Translator
translator = Translator()
recognizer=sr.Recognizer()
microphone = sr.Microphone()
res=r.get("https://cloud.google.com/speech-to-text/docs/languages")
soup=bs(res.content,'html.parser')
LANGUAGES = {'af': 'afrikaans','sq': 'albanian','am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese','pa': 'punjabi','ro': 'romanian','ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho','sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali','es': 'spanish','su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu','th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu','uz': 'uzbek','vi': 'vietnamese','cy': 'welsh','xh': 'xhosa','yi': 'yiddish','yo': 'yoruba','zu': 'zulu','fil': 'Filipino','he': 'Hebrew'
}

LANGCODES = dict(map(reversed, LANGUAGES.items()))

temp=[j for j in range(2,360,3)]
x=0
d=list()
lang=[]
for i in soup.select('div table tbody tr td'):
    if x in temp:
        d=d+list(i)
        lang.append(d)
        d=list()
    else:
        d=d+list(i)
    x+=1
d=dict()
x=0
for i in lang:
    d[i[2]]=[x,i[1]]
    x+=1
#Language for speech_recognition
temp_d=dict()
for i,j in d.items():
    temp_d[i.split()[0].lower()]=j[1].split("-")[0]
print("Please Enter Ist User Name:")
user1=input()
print("Please Enter 2nd User Name: ")
user2=input()
for i,j in d.items():
    print("Language:",i,"Index:",j[0])
print(user1,"select your Perfered Language,Please select the index")
index1=int(input())
final1=None
for i,j in d.items():
    if j[0]==index1:
        final1=j[1]
        lang1=i
print(user2,"select your Perfered Language,Please select the index")
index2=int(input())
final2=None
for i,j in d.items():
    if j[0]==index2:
        final2=j[1]
        lang2=i
temp_l=dict()
for i,j in  LANGCODES.items():
    temp_l[i.split()[0].lower()]=j
i=2
print(user1,"Has select Language:",lang1)#,"and Language code:",final1,"and",final1.split("-")[0],"or",temp_l[lang1.split()[0].lower()])
print(user2,"Has select language:",lang2)#,"and Language code:",final2,'and',final2.split("-")[0],"or",temp_l[lang2.split()[0].lower()])
while 1:
    with microphone as source:
        if i%2==0:
            print(user1,"Please say something:")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    # set up the response object
            response = {
                "success": True,
                "error": None,
                "transcription": None
            }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
            try:
                response["transcription"] = recognizer.recognize_google(audio,language=final1)
            except sr.RequestError:
        # API was unreachable or unresponsive
                print("API was unreachable or unresponsive,Please try again")
                response["success"] = False
                response["error"] = "API unavailable"
                continue
            except sr.UnknownValueError:
        # speech was unintelligible
                response["error"] = "Unable to recognize speech"
                print("Sorry didn't get..Try Again")
                continue
            print(response['transcription'])
            x=translator.translate(response['transcription'],dest=final2.split("-")[0])
            print(user1,"Has said:",x.text)
        else :
            print(user2,"Please say something:")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    # set up the response object
            response = {
                "success": True,
                "error": None,
                "transcription": None
            }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
            try:
                response["transcription"] = recognizer.recognize_google(audio,language=final2)
            except sr.RequestError:
        # API was unreachable or unresponsive
                print("API was unreachable or unresponsive,Please try again")
                response["success"] = False
                response["error"] = "API unavailable"
                continue
            except sr.UnknownValueError:
        # speech was unintelligible
                response["error"] = "Unable to recognize speech"
                print("Sorry didn't get..Try Again")
                continue
            print(response['transcription'])
            x=translator.translate(response['transcription'],dest=final1.split("-")[0])
            print(user2,"Has said:",x.text)
        i+=1
        if i>=6:
            break
