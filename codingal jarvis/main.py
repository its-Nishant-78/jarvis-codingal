
import nltk
from nltk.chat.util import Chat, reflections
reflections= {
    "i am "   : "you are",
    "i was"   : "you where",
    "i"       :"you",
    "i'm"     :"you are",
    "i'd"     :"you would",
    "i've"    :"you have",
    "i'll"    :"you will",
    "my"      :"your",
    "you are" :"i am",
    "you were":"i was",
    "you've"  :"i have",
    "you'll"  :"will",
    "your"    :"my",
    "yours"   :"mine",
    "you"     :"me",
    "me"      :"you"
 }
pairs = [
    [
        "my name is (.*)",
        ["hello %1, How are you today?",]
    ],
    [
        "hi|hello|hey",
        ["Hello","hey there",]
    ],
]
def x():
    print("Hi I am a chatbox")
    chat =Chat(pairs,reflections)
    chat.converse()

if __name__ =="__main__":
    x()