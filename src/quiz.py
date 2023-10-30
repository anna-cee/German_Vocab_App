
import string
from colorama import Fore, Back, Style
import randomlist

class QuizGenerator:
    def __init__(self, workinglist):
        self.workinglist = workinglist
        correctcounter = 0
        index = 0
        print(Fore.CYAN +"QUIZ ... 1. WORD MATCH RECALL\n")
        while index < len(workinglist):
            for item in workinglist:
                targetvocab = item['German']
                definevocab = item['English']
                cleantarget = targetvocab.rstrip()
                cleandefine = definevocab.rstrip()
                answer = input(f'What is the German for {cleandefine}? ')
                index +=1
                if answer == cleantarget:
                        correctcounter += 1
                        print(Fore.GREEN + f"Richtig! {cleandefine} is '{cleantarget}'\n")
                while answer != cleantarget:
                    answer = input(f"Hopla! Try again or hit 'C' to check answer)  \n ")                   
                    if answer == 'C':
                        answer = cleantarget
                        print(Fore.GREEN + f"{cleandefine} is '{cleantarget}'\n")
                    elif answer == cleantarget:
                        correctcounter += 1
                        print(Fore.GREEN + f"Richtig! {cleandefine} is '{cleantarget}'\n")
        print(Fore.MAGENTA + f" Toll! You remembered {correctcounter} items! \n")
        nav_option = input("Wieder mal? Go again? 'A' or any key for next.  ")
        if nav_option == 'A':
            QuizGenerator(workinglist)
        

class ContextQuizGenerator:
    def __init__(self, workinglist):
        self.workinglist = workinglist
        index = 0
        print(Fore.CYAN + 'QUIZ ... 2. GAP FILL: One try for each word in context. \n')
        while index < len(workinglist):
            for item in workinglist: 
                sentence = item['Context'].split()
                matchlist = item['German'].split()
                article = 'der' or 'die' or 'das'
                for word in sentence:
                    word_clean = word.strip()
                    for match in matchlist:
                        match_clean = match.strip()
                        if match_clean == word_clean and match_clean != article:
                            sentence[(sentence.index(word_clean))] = "__________"
                            separator = " "
                            answer = input(f'Which word is missing?        {(separator.join(sentence))}  ')       
                            if answer == match:
                                    print(Fore.CYAN + 'Richtig!')
                            if answer == (f'match'+'.'):
                                    print(Fore.CYAN + 'Richtig!')
                            if answer != match:
                                print(Fore.GREEN + f"The answer was '{match}''")
                            index += 1
        nav_option = input("Wieder mal? Go again? 'A' or any key for next.  ")
        if nav_option == 'A':
            ContextQuizGenerator(workinglist)


            








