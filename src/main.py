import randomlist
import quiz 
import flashcard
import time
import sys
from colorama import Fore, Back, Style
from prettytable import PrettyTable
outline = PrettyTable()


#Start Welcome
# welcome = 'Tag! Wilkommen!'
# for x in welcome:
#     sys.stdout.flush  
#     print(Fore.YELLOW, Style.BRIGHT + x )
#     time.sleep(0.2)
# for x in welcome:
#     print(Fore. YELLOW + x, end=" ", flush=True)
#     time.sleep(0.2)
# title = '\nRandom Vocabulary List & Quiz Generator \n'
# for x in title:
#     print(Fore. RED + x, end ="", flush=True)
# type = 'German for Beginners!'
# print(Fore.CYAN + type)
# input()
    


features = [ '1. Choose a topic \n'
        '2. Generate a list of 10 random vocab from the topic. \n'
        '3. View the list, translation and context sentences. \n'
        '4. Flashcards generate to learn the list \n'
        '5. Quiz your memory with a word-match and gap-fill quiz. \n' ]

outline.add_column('App features include:', features)
features_table = outline.get_string(fields=['App features include:'])
print(features_table)

class MenuCheckError(Exception):
    pass

def nav_option():
    navoption = input("Press any key for next feature or 'M' to return to Main Menu for a new list.\n")
    if navoption == 'M':
         menu()


def menu():
    try:
        menu_option= input('\nCHOOSE A TOPIC TO START! \n \n 1. health and body \n 2. time \n 3. food \n 4. getting around \n 5. spending money \n')


        if menu_option == '1':
            health_list = randomlist.Randomlist(open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')) 
            #print(healthlist.workinglist)
            health_vocab = health_list.workinglist
            health_table = randomlist.TableGenerator(health_vocab)
            nav_option()
            health_flashcards = flashcard.FlashcardGenerator(health_table)   
            nav_option()
            health_quiz = quiz.QuizGenerator(health_vocab)
            nav_option()
            health_contextquiz = quiz.ContextQuizGenerator(health_vocab)
            print('Super gemacht! Back to Menu!')
            menu()
 

        elif menu_option == '2':
            time_list = randomlist.Randomlist(open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig'))
            time_vocab = time_list.workinglist        
            time_table = randomlist.TableGenerator(time_vocab)
            time_flashcards = flashcard.FlashcardGenerator(time_vocab)
            time_quiz = quiz.QuizGenerator(time_vocab)
            time_contextquiz = quiz.ContextQuizGenerator(time_vocab)

            menu()

        elif menu_option == '3':
            food_list = randomlist.Randomlist(open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig'))
            food_vocab = food_list.workinglist
            food_table = randomlist.TableGenerator(food_vocab)
            food_flashcards = flashcard.FlashcardGenerator(food_table)
            food_quiz = quiz.QuizGenerator(food_vocab)
            food_contextquiz = quiz.ContextQuizGenerator(food_vocab)
           
            menu()

        elif menu_option == '4':
            travel_list = randomlist.Randomlist(open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))
            travel_vocab = travel_list.workinglist
            travel_table = randomlist.TableGenerator(travel_vocab)
            travel_flashcards = flashcard.FlashcardGenerator(travel_table)
            travel_quiz = quiz.QuizGenerator(travel_vocab)
            travel_contextquiz = quiz.ContextQuizGenerator(travel_vocab)
           
            menu()

        elif menu_option == '5':
            spending_list = randomlist.Randomlist(open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig'))
            spending_vocab = spending_list.workinglist
            spending_table = randomlist.TableGenerator(spending_vocab)
            spending_flashcards = flashcard.FlashcardGenerator(spending_table)
            spending_quiz = quiz.QuizGenerator(spending_vocab)
            spending_contextquiz = quiz.ContextQuizGenerator(spending_vocab)

            menu()

        elif menu_option != '1' or menu_option != '2' or menu_option != '3' or menu_option != '4' or menu_option != '5':
            raise MenuCheckError()

    except MenuCheckError:
        print('Choose a number from the topic menu to start.')
        menu()

menu()

   
                



        
   

    
