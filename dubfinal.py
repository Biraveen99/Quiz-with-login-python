brukernavn_passord = { }

def stuff():
    Hovedmeny()

def Hovedmeny():
    print('trykk L for å logge inn eller R for å registrere deg.' "\n",) #L for login nad R for registration/
    valg = (input()).upper()
    if valg == 'L' :
        innlogging()
    elif valg == 'R':
        login_info ()
    else:
        print('skriv ordentlig') # if you write something else this will come up
        Hovedmeny()


def login_info ():
            print('du skal nå registreres') #giving user feedback for his/hers choice
            brukernavn = input('skriv inn et brukernavn:') #write username
            passord = input('skiv inn et passord:') #write passweord
            brukernavn_passord.update(brukernavn = brukernavn ,passord = passord) #putting them both in the dictionary
            svar = input('vil du lage enda en bruker? svar med J for ja og N for nei.').upper() #if you want to create a new user click J else N
            if svar == 'J':
                login_info ()
            if svar == 'N':
                innlogging()
            else:
                print('Du ga et input som ikke er gydlig, du tas tilbake til hovedmenyen')  # if you write something youll be taken back to the main menu
                Hovedmeny()

def innlogging(): # this is the login sequence if you write
    value1 = input('Brukernavn:')
    value2 = input('Passord:')
    t = 0
    if value1 and value2 in brukernavn_passord.values():
        print('innlogging fullført! Nå til spørsmålene!') #if you have logged inn correctly this message will be displayed
        spørsmål()
    else:
        print('bruker finnes ikke, prøv igjen') # else this will
        innlogging()


def spørsmål(): #these are just the pre-written questions for the quiz.
    score = 0
    liste_score= [ ]
    print('NÅ MÅ DU SVARE VED Å BRUKE SMÅ BOKSTAVER, alt annet av inputs vil gi deg null poeng') #it can be possible to use big letters aswell, we just need to implement an OR function
    poeng = input(' Q1 What is the capital of Norway? \n a. Bergen \n b. Oslo \n c. Stavanger \n d. Trondheim \n')
    if poeng == 'b':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input("Q2 What is the currency of Norway? \n a. Euro \n b. Pound \n c. Krone \n d. Deutsche Mar\n")
    if poeng == 'c':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q3 What is the largest city in Norway?\na. Oslo \nb. Stavanger \nc. Bergen \nd. Trondheim\n')
    if poeng == 'a':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q4 When is constitution day (the national day) of Norway?\n a. 27th May \nb. 17th May \nc. 17th April \nd. 27th April\n')
    if poeng == 'b':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q5 What color is the background of the Norwegian flag? \na. Red\n b. White \nc. Blue \nd. Yellow\n')
    if poeng == 'a':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q6 How many countries does Norway border? \na. 1 \nb. 2 \nc. 3 \n d. 4\n')
    if poeng == 'c':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q7 What is the name of the university in Trondheim? \na. UiS\n b. UiO \nc. NMBU\n d. NTNU\n')
    if poeng == 'd':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q8 How long is the border between Norway and Russia? \na. 96 km \nb. 196 km \nc. 296 km \nd. 396 km\n')
    if poeng == 'b':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q9 Where in Norway is Stavanger? \na. North\n b. South \nc. South-west\nd. South-east\n')
    if poeng == 'c':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    poeng = input('Q10 From which Norwegian city did the world famous composer Edvard Grieg come? \na. Oslo \nb. Bergen \nc. Stavanger\n d. Tromsø\n')
    if poeng == 'b':
        score = score+1
        liste_score.append(1)
    else:
        liste_score.append(0)

    print('du fikk totalt ',score, ' poeng av 10 mulige ')

    print('spørsmålene du har svart riktig på er representert som et 1 og spørsmålene du har svart feil på er representert som 0:')
    print(liste_score)

    if liste_score[0] == 0:
        print('på spm 1 skulle svaret ha vært B')
    
    if liste_score[1] == 0:
        print('på spm 2 skulle svaret ha vært C')
        
    if liste_score[2] == 0:
        print('på spm 3 skulle svaret ha vært A')
    
    if liste_score[3] == 0:
        print('på spm 4 skulle svaret ha vært B')
    
    if liste_score[4] == 0:
        print('på spm 5 skulle svaret ha vært A')
    
    if liste_score[5] == 0:
        print('på spm 6 skulle svaret ha vært C')
    
    if liste_score[6] == 0:
        print('på spm 7 skulle svaret ha vært D')
        
    if liste_score[7] == 0:
        print('på spm 8 skulle svaret ha vært B')
        
    if liste_score[8] == 0:
        print('på spm 9 skulle svaret ha vært C')
    
    if liste_score[9] == 0:
        print('på spm 10 skulle svaret ha vært B')
        
    


stuff()
