import random
import json
import nltk
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from nltk.corpus import stopwords

#https://shrib.com/?unlock=now#Mina-xZWrBD
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


with open("database.json", "r") as f:
    data = json.load(f)

greetings_intro = data["greetings_intro"]
greetings_outro = data["greetings_outro"]
negative = data["negative"]
questions = data["questions"]
instiname = data["instiname"]
bot_name = "AdmissionTard : "

def remove_stop_words(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def find_best_match(query, choices):
    filtered_query = remove_stop_words(query)
    filtered_choices = [remove_stop_words(choice["question"]) for choice in choices]

    best_match, score = process.extractOne(filtered_query, filtered_choices, scorer=fuzz.token_sort_ratio)
    return best_match, score

print("\n"+random.choice(instiname))
print("\nHello I am AdmissionTard.")
print(bot_name + "Can I have your name? ")
name = input("You : ").capitalize()
default_name = "Anonymous"

namecount = 0
while name.isspace() or not name:
    print(bot_name, "Please Enter your name. chance : (", namecount + 1, ")")
    name = input("You : ").capitalize()
    namecount += 1
    if namecount == 3:
        name = default_name
        print(bot_name + "Since you haven't provided a name, I'll call you " + default_name + ".")
        print("Write",'"help"',"to explore the list of common queries.")
        break

if name in negative:
    name = default_name
    print(bot_name + "No Problem, Write",'"help"',"to explore the list of common queries.")

elif name not in negative:
    print(bot_name + "Thanks " + name + ", Write",'"help"',"to explore the list of common queries.")
    default_name = name

while True:
    userinp = input(default_name + " : ").lower()
    if userinp in greetings_intro:
        print(bot_name  +  random.choice(greetings_intro).capitalize())
    elif userinp in greetings_outro:
        print(bot_name  + random.choice(greetings_outro).capitalize())
        break
    else:
        best_question, match_score = find_best_match(userinp, questions)
        if match_score > 60:  # Adjust this threshold as needed
            best_question_data = next(item for item in questions if remove_stop_words(item["question"]) == best_question)
            print(bot_name + best_question_data["answer"])
        else:
            print(bot_name + "I'm sorry, I don't understand, please write 'help' to explore the topics i can help you with.")
