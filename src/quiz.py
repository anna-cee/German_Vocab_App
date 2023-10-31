
import string
from colorama import Fore, Back, Style
import randomlist

try:

    class QuizGenerator:
        def __init__(self, workinglist):
            self.workinglist = workinglist
            correctcounter = 0
            index = 0
            print(Fore.GREEN, Style.BRIGHT + "QUIZ GENERATOR... \n")
            print(Fore.GREEN, Style.NORMAL + "QUIZ 1. WORD MATCH RECALL: Answer with a word from the list. Points for correct guesses, unlimited guesses, no penalties. \n")

            while index < len(workinglist):
                for item in workinglist:
                    targetvocab = item['German']
                    definevocab = item['English']
                    cleantarget = targetvocab.strip()
                    cleandefine = definevocab.strip()
                    print(Fore.GREEN)
                    answer = input(f'What is the German for {cleandefine}? ')
                    index +=1
                    if answer == cleantarget:
                            correctcounter += 1
                            print(Fore.MAGENTA + f"Richtig! {cleandefine} is '{cleantarget}'\n")
                    while answer != cleantarget:
                        print(Fore.CYAN)
                        answer = input(f"Hopla! Try again or hit 'C' to check answer)  \n ")                   
                        if answer == 'C':
                            answer = cleantarget
                            print(Fore.MAGENTA + f"{cleandefine} is '{cleantarget}'\n")
                        elif answer == cleantarget:
                            correctcounter += 1
                            print(Fore.MAGENTA+ f"Richtig! {cleandefine} is '{cleantarget}'\n")
            print(Fore.YELLOW + f" Toll! You remembered {correctcounter} items! \n")
            print(Fore.CYAN, Style.BRIGHT)
            nav_option = input("Wieder mal? Go again? 'A' or any key for next.  ")
            if nav_option == 'A':
                QuizGenerator(workinglist)
            

    class ContextQuizGenerator:
        def __init__(self, workinglist):
            self.workinglist = workinglist
            print(Fore.GREEN, Style.BRIGHT +"QUIZ ... 2. GAPFILL: Recall the missing word. One try per question, unlimited repeats of quiz, or exit at end.\n")
          
            for item in workinglist: 
                sentence = item['Context'].split()
                matchlist = item['German'].split()

                if len(matchlist) == 2 or len(matchlist) == 3:
                    match = matchlist[1]
                    match_clean = match.strip()
                    
                elif len(matchlist) == 1:
                    match = matchlist[0]
                    match_clean = match.strip()
                    
                for word in sentence:
                    word_clean = word.strip()
                    word_nopunct = word_clean.rstrip(".,?!")  
                    
                    if word_nopunct == match_clean:
                        sentence[(sentence.index(word_clean))] = "__________"
                        separator = " "
                        print(Fore.GREEN, Style.NORMAL + 'Which word is missing?')
                        answer = input(Fore.CYAN + separator.join(sentence))        
                        if answer == match_clean:
                            print(Fore.MAGENTA + 'Richtig!\n')
                        elif answer != match:
                            print(Fore.CYAN + f"Answer check: '{match}'\n")
                      
            nav_option = input(Fore.MAGENTA + "Wieder mal? Go again? Press 'A' or any key for next.  \n")
            if nav_option == 'A':
                ContextQuizGenerator(workinglist)

            
except:
    print("Oops, the quiz for this list didn't run.")

