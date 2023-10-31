import pytest
import string


quiz_test_data = [
     {'German': 'das Getränk', 'English': 'drink', 'Context': 'Mein Lieblingsgetränk ist Tomatensaft.'}, 
     {'German': 'die Tomate', 'English': 'tomato', 'Context': ' Die Tomate ist noch grün.'}, 
     {'German': 'das Gemüse ', 'English': 'vegetables', 'Context': 'Gemüse brauchen wir auch noch.'}, 
     {'German': 'Guten Appetit!', 'English': 'bon appetit', 'Context': 'Guten Appetit!'}, 
     {'German': 'die Toilette', 'English': 'toilet', 'Context': 'Wo ist die Toilette, bitte?'}, 
     {'German': 'das Ei', 'English': 'egg', 'Context': 'Möchtest du ein Ei zum Frühstück?'}, 
     {'German': 'die Karte (Speisekarte)', 'English': 'menu', 'Context': 'Ich möchte auch etwas essen. Bringen Sie mir die Karte, bitte'}, 
     {'German': 'der Schinken', 'English': 'ham', 'Context': 'Ich möchte gern ein Schinkenbrot.'}, 
     {'German': 'die Lebensmittel', 'English': 'food', 'Context': 'Lebensmittel bekommen Sie im Supermarkt.'}, 
     {'German': 'trinken ', 'English': 'to drink', 'Context': 'Möchtest du etwas trinken?'}
     ]


datalist = quiz_test_data
def quiz_test(datalist):
    for item in datalist: 
        sentence = item['Context'].split()
        matchlist = item['German'].split()
        if len(matchlist) == 2 or len(matchlist) == 3:
            match = matchlist[1]
            match_clean = match.strip()
            #print(match_clean) 
        elif len(matchlist) == 1:
            match = matchlist[0]
            match_clean = match.strip()
            #print(match_clean)
        for word in sentence:
            word_clean = word.strip()
            word_nopunct = word_clean.rstrip(".,?!")
            #print(word_nopunct)
            if word_nopunct == match_clean:
                sentence[(sentence.index(word_clean))] = "__________"
                separator = " "
                print(f'Which word is missing?        {(separator.join(sentence))}  ')     
         


  
            
quiz_test(quiz_test_data)
  





            








