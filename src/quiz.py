
import string
from cli_color_py import red, bright_yellow, green, blue, bold, magenta

class QuizGenerator:
    def __init__(self, workinglist):
        self.workinglist = workinglist
        correctcounter = 0
        for item in workinglist:
            targetvocab = item['German']
            definevocab = item['English']
            cleantarget = targetvocab.rstrip()
            cleandefine = definevocab.rstrip()
            answer = input(f'What is the German for {cleandefine}? ')
            if answer == cleantarget:
                    correctcounter += 1
                    print(green(f"Richtig! {cleandefine} is '{cleantarget}'\n"))
            while answer != cleantarget:
                answer = input(f"Nochmal eingeben bitte! (try again or hit 'c' to check answer)  \n ")                   
                if answer == 'c':
                    answer = cleantarget
                    print(blue(f"{cleandefine} is '{cleantarget}'"))
                elif answer == cleantarget:
                    correctcounter += 1
                    print(green(f"Richtig! {cleandefine} is '{cleantarget}' \n"))
        print(magenta(f" Toll! You remembered {correctcounter} items! \n"))

class ContextQuizGenerator:
    def __init__(self, workinglist):
        self.workinglist = workinglist
        #word = str
        
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
                                print(blue('Richtig!'))
                        if answer == (f'match'+'.'):
                                print(blue('Richtig!'))
                        if answer != match:
                            print(green(f"The answer was '{match}''"))




