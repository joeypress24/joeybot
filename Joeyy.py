import sys
import random
import time
import webbrowser



#MAIN
#initial variable declaration
testBit = 0
str = ""
failedAnswer = [ "only the universe can answer this",
                "as the ancients foretold: yeet",
                "honestly, idk man",
                "AI is powerful, yes, but not that powerful",
                "some questions cannot be answered",
                "google it, silly",
                "this is pushing the limits of decideable and undecideable questions" ]


yn = input("Welcome to JoeyBot, an interactive AI!\nDo you wish to configure the AI? (Y/N) ")
if yn == 'Y' or yn == 'y':
    print("\nHello! Before we begin, we need to ask a few questions to train the AI\n")
    time.sleep(0.5)
    a = input("What is your favorite color? ")
    time.sleep(0.5)
    b = input("\nEnter a valid number between 0 and 255: ")
    time.sleep(0.5)
    b = input("\nEnter three verbs (e.g. running, climbing): ")
    time.sleep(0.5)
    c = input("\nEnter the first word that pops into your mind right now: ")
    print("\nPlease wait while we run diagnostics")
    time.sleep(1)
    print("\nTraining the AI, standby...")
    time.sleep(0.5)
    print("\n\nDiagnostics complete, proceed with the program\n\n\n")
    time.sleep(1)
else:
    print("\nProceeding with saved data from last user\n\n\n")
    time.sleep(1)



print("*** Write a petition and ask a question for Joey to answer ***\n")

input("Enter a petition: ")

#print("\n\nEnter a question: ")
q = input("\nEnter a question: ")
print("prepare to get rekt")

#pause for a second
time.sleep(1)
# print("\n")
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
try:
    webbrowser.open(url)
except:
    print("")

print("\n ****************************************************************\n\n\n\n")
time.sleep(1)
