import pytest

import string
from colorama import Fore, Back, Style
import random




#expected output print correct it items match, end after cycling through list.
# class QuizGenerator:
#     def __init__(self, workinglist):


quizTestData = [
     {'German': 'das Getränk', 'English': 'drink', 'Context': 'Mein Lieblingsgetränk ist Tomatensaft.'}, 
     {'German': 'die Tomate', 'English': 'tomato', 'Context': ' Die Tomate ist noch grün.'}, 
     {'German': 'das Gemüse ', 'English': 'vegetables', 'Context': 'Gemüse brauchen wir auch noch.'}, 
     {'German': 'Guten Appetit!', 'English': 'bon appetit', 'Context': 'Guten Appetit!'}, 
     {'German': 'die Toilette', 'English': 'toilet', 'Context': 'Wo ist die Toilette, bitte?'}, 
     {'German': 'das Ei', 'English': 'egg', 'Context': 'Möchtest du ein Ei zum Frühstück?'}, 
     {'German': 'die Karte (Speisekarte)', 'English': 'menu', 'Context': 'Ich möchte auch etwas essen. Bringen Sie mir die Karte, bitte'}, 
     {'German': 'der Schinken', 'English': 'ham', 'Context': 'Ich möchte gern ein Schinkenbrot.'}, 
     {'German': 'die Lebensmittel', 'English': 'food', 'Context': 'Lebensmittel bekommen Sie im Supermarkt.'}, 
     {'German': 'trinken ', 'English': 'to drink', 'Context': 'Möchtest du etwas trinken?'}]

@pytest.mark.parametrize('quizData',quizTestData)
#match quiz test - determine answer = target
def test_item_match(quizData):
    
    correctcounter = 0
    index = 0
    print(Fore.CYAN +"QUIZ ... 1. WORD MATCH RECALL\n")
    while index < len(quizTestData):
        for item in quizTestData:
            targetvocab = item['German']
            definevocab = item['English']
            cleantarget = targetvocab.rstrip()
            cleandefine = definevocab.rstrip()
            answer = quizData.get('German')
            index += 1
            if answer == cleantarget:
                 correctcounter += 1
                 print(Fore.GREEN + f"Richtig! {cleandefine} is '{cleantarget}'\n")


#context quiz test - determine target vocab blanked out in quiz
@pytest.mark.parametrize('quizData',quizTestData)
def test_item_blank(quizData):
    index = 0
    while index < len(quizTestData):
        for item in quizTestData: 
            answer = quizData.get('German')
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
                        sentence = (f'Which word is missing?        {(separator.join(sentence))}  ')
                        index += 1      
                        
                       
                        #         print(Fore.CYAN + 'Richtig!')
                        # if answer == (f'match'+'.'):
                        #         print(Fore.CYAN + 'Richtig!')
                        # if answer != match:
                        #     print(Fore.GREEN + f"The answer was '{match}''")
                        # index += 1
   


        








