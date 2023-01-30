import getch
import sys
import random
import time

def doStuff():
    pet = "Joey please answer the following question"
    st = ""
    i = 0

    #print first character of petition
    print(pet[i], end = "")
    sys.stdout.flush()
    i += 1

    while True:
        character = getch.getch()
        if character == '.':
            print(pet[i], end = "")
            sys.stdout.flush()
            break
        elif character in ('KEY_BACKSPACE', '\b', '\x7f'):
            #backspace entered, remove character at end of string
            l = len(st)
            remove_last = st[:l-1]
            st = remove_last
        print(pet[i], end = "")
        sys.stdout.flush()
        i += 1

        st += character

    return st


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
                "this is pushing the limits of decideable and undecideable questions",
                "i have no clue what you mean, bro",
                "let me know, let me know, let me know, let me know...",
                "there is only one person in the world who could possibly answer that.... me" ]

poem = "Ποιανού τα ξύλα είναι αυτά νομίζω ότι ξέρω.\
Το σπίτι του όμως είναι στο χωριό.\
Δεν θα με δει να σταματάω εδώ\
Για να δει τα δάση του να γεμίζουν με χιόνι.\
\
Το αλογάκι μου πρέπει να το θεωρεί περίεργο\
Να σταματήσει χωρίς αγροικία κοντά\
Ανάμεσα στο δάσος και την παγωμένη λίμνη\
Το πιο σκοτεινό βράδυ του χρόνου.\
\
Κουνάει τις καμπάνες του\
Να ρωτήσω αν υπάρχει κάποιο λάθος.\
Ο μόνος άλλος ήχος είναι το σκούπισμα\
Από εύκολο άνεμο και περονόσπορο.\
\
Τα δάση είναι υπέροχα, σκοτεινά και βαθιά,\
Αλλά έχω υποσχέσεις να τηρήσω,\
Και μίλια απομένουν πριν κοιμηθώ,\
Και μίλια απομένουν πριν κοιμηθώ."

poem1 = "Noli in bonam noctem illam lenire;\
senectus ardeat et extrema luce desipiat;\
Furor, ira morientis luminis.\
\
Sapientes in fine tenebrarum recta cognoscant;\
quia verba eorum non trifida fulmina sunt\
Noli mitis in illam bonam noctem.\
\
Boni viri, ultimam undam prae se ferunt, clamantes quam lucida!\
Mollia sedent viridi facta saltare sinu;\
Furor, ira morientis luminis.\
\
Indomiti, qui ceperunt solem, in fuga cecinerunt;\
Disce et sero : doluerunt in via ;\
Noli mitis in illam bonam noctem.\
\
Graves, morti proximus, caeco Visu qui cernunt\
Oculi caeci sicut meteoris flagrare poterant et hilares esse;\
Furor, ira morientis luminis.\
\
Tuque, pater, illic maesta locaris arce ;\
Maledica, benedic, me nunc tuis saevis lacrymis, precor.\
Noli mitis in illam bonam noctem.\
Furor, ira morientis luminis."

poem2 = "ਵੇਖ ਕੇ! ਦਰਵਾਜ਼ੇ ਵਿੱਚ ਪਾੜਾ. ਇਹ ਇੱਕ ਵੱਖਰੀ ਹਕੀਕਤ ਹੈ। ਕੀ ਸਿਰਫ ਮੈਂ ਹੀ ਅਸਲੀ ਹਾਂ, ਜਾਂ ਕੀ ਤੁਸੀਂ ਅਸਲੀ ਹੋ?"

poem3 = "statiken vet mitt namn"

j = "option"


yn = input("Welcome to JoeyBot, an interactive algorithm!\nDo you wish to configure the JoeyBot at this time? (Y/N) ")
if yn == 'Y' or yn == 'y':
    print("\nHello! Before we begin, we need to ask a few questions to train the program\n")
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
    print("\nTraining the bot, standby...")
    time.sleep(1.5)
    print("\n\nDiagnostics complete, proceed with the program\n\n\n")
    time.sleep(1)
else:
    print("\nProceeding with saved data from last user\n\n\n")
    time.sleep(1)



while True:
    print("*** Write a petition and ask a question for Joey to answer ***\n")

    print("Enter a petition: ", end = "")
    sys.stdout.flush()
    character = 'z'
    while True:
        character = getch.getch()

        if(character == '.'):
            str = doStuff()
            testBit = 1

        elif character == '\n':
            break

        else:
            print(character, end='')
            sys.stdout.flush()

    print("\n\nEnter a question: ", end = "")
    sys.stdout.flush()
    q = input()
    print("")
    #pause for a second
    time.sleep(1.5)
    # print("\n")
    if testBit == 1:
        if(str is "f"): #poem
            print(poem)
        elif str is "d": #poem
            print(poem1)
        elif str is "s": #poem
            print(poem2)
        elif str is "a": #poem
            print(poem3)
        elif str is "j": #option
            print(j)
        else:
            print(str)
    else:
        rand = random.randrange(0, 10, 1)
        print(failedAnswer[rand])

    print("\n", "*"*60)
    print("\n\n\n\n")
    time.sleep(1)
    testBit = 0 # reset the test bit
