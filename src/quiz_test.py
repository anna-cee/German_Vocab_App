

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


#match quiz test - determine answer = target

def test_item_match(data):
    correctcounter = 0
    index = 0
    while index < len(quiz_test_data):
        for item in quiz_test_data:
            targetvocab = item['German']
            definevocab = item['English']
            cleantarget = targetvocab.rstrip()
            cleandefine = definevocab.rstrip()
            answer = cleantarget
            index += 1
            if answer == cleantarget:
                 correctcounter += 1
                 print(f"Richtig! {cleandefine} is '{cleantarget}'\n")

test_item_match(quiz_test_data)
    

           

        








