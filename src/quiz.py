
import string
from colorama import Fore, Back, Style
import randomlist

try:

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
            print(Fore.CYAN +"QUIZ ... 2. GAPFILL Recall word from list that could be missing.\n")
            while index < len(workinglist):
                for item in workinglist: 
                    index += 1
                    sentence = item['Context'].split()
                    matchlist = item['German'].split()
                    for match in matchlist:
                        match_clean = match.strip()
                        if len(match_clean) > 3 or len(match_clean)<= 2:
                            target_word = match_clean
                            
                    for word in sentence:
                        word_clean = word.strip()
                        if word_clean == target_word:
                            sentence[(sentence.index(word_clean))] = "__________"
                            separator = " "
                            answer = input(f'Which word is missing?        {(separator.join(sentence))}  ')       
                            if answer == match:
                                print(Fore.CYAN + 'Richtig!')
                                if answer == (f'match'+'.'):
                                        print(Fore.CYAN + 'Richtig!')
                                if answer != match:
                                    print(Fore.GREEN + f"The answer was '{match}''")
                    
            nav_option = input("Wieder mal? Go again? 'A' or any key for next.  ")
            if nav_option == 'A':
                ContextQuizGenerator(workinglist)
except:
    print("Oops, the quiz for this list didn't run.")

