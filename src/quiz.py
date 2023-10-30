
import string
from colorama import Fore, Back, Style
import randomlist

class QuizGenerator:
    def __init__(self, workinglist):
        self.workinglist = workinglist
        correctcounter = 0
        print(Fore.CYAN +"QUIZ ... 1. WORD MATCH RECALL\n")
        for item in workinglist:
            targetvocab = item['German']
            definevocab = item['English']
            cleantarget = targetvocab.rstrip()
            cleandefine = definevocab.rstrip()
            answer = input(f'What is the German for {cleandefine}? ')
            if answer == cleantarget:
                    correctcounter += 1
                    print(Fore.GREEN + f"Richtig! {cleandefine} is '{cleantarget}'\n")
            while answer != cleantarget:
                answer = input(f"Nochmal eingeben bitte! (try again or hit 'c' to check answer)  \n ")                   
                if answer == 'c':
                    answer = cleantarget
                    print(Fore.GREEN + f" {cleandefine} is '{cleantarget}'\n")
                elif answer == cleantarget:
                    correctcounter += 1
                    print(Fore.GREEN + f"Richtig! {cleandefine} is '{cleantarget}'\n")
        print(Fore.MAGENTA + f" Toll! You remembered {correctcounter} items! \n")
        input('Press any key for GAPFILL.')

class ContextQuizGenerator:
    def __init__(self, workinglist):
        self.workinglist = workinglist
        #word = str
        print(Fore.CYAN + 'QUIZ ... 2. GAP FILL\n')
        for item in workinglist: 
            sentence = item['Context'].split()
            matchlist = item['German'].split()
            article = 'der' or 'die' or 'das'
            #print(sentence)
            for word in sentence:
                word_clean = word.strip()
               # print(word_clean)
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








