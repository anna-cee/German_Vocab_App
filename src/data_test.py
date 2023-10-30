import pytest


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
        for match in matchlist:
            match_clean = match.strip()
            if len(match_clean) > 3 or len(match_clean)<= 2:
                target_word = match_clean
                print(target_word)
        for word in sentence:
            word_clean = word.strip()
            if word_clean == target_word:
                print(word_clean)
    
        #assert word_clean == target_word
            
quiz_test(quiz_test_data)
  





            








