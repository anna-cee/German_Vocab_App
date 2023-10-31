import randomlist
import quiz 
import flashcard
import time
import sys
from colorama import Fore, Back, Style
from prettytable import PrettyTable
outline = PrettyTable()


#Start Welcome
welcome_vert = 'Tag! Wilkommen!'
for x in welcome_vert:
    sys.stdout.flush  
    print(Fore.YELLOW + x )
    time.sleep(0.1)
welcome_hor = 'Tag! Wilkommen! \n \n'
for x in welcome_hor:
    print(Fore.YELLOW + x, end=" ", flush=True)
    time.sleep(0.1)
title = 'RANDOM VOCABULARY LIST \n & QUIZ GENERATOR \n \n'
for x in title: 
    print(Fore.RED, Style.BRIGHT + x, end=" ", flush=True)
type = 'German for Beginners! \n \n'
print(Fore.CYAN + type)
input("Please ENTER \n")
    


features = [ '* Choose a topic \n'
        '* Generate a list of 10 random vocab from the topic. \n'
        '* View the list, translation and context sentences. \n'
        '* Flashcards generate to learn the list \n'
        '* Quiz your memory with a word-match and gap-fill quiz. \n' ]

outline.add_column('App features include:', features)
features_table = outline.get_string(fields=['App features include:'])
print(Style.RESET_ALL + features_table)
input('ENTER for Topic Menu')

class MenuCheckError(Exception):
    pass

def nav_option():
    print(Style.RESET_ALL)
    navoption = input("Press any key for next feature or 'M' to return to Main Menu for a new list.\n")
    if navoption == 'M':
         menu()


def menu():
    try:
        menu_option = input(Fore.CYAN + "\nCHOOSE A TOPIC TO START! \n \n 1. health and body \n 2. time \n 3. food \n 4. getting around \n 5. spending money \n")
    
        if menu_option == '1':
            health_list = randomlist.Randomlist(open('body_and_health.csv','r',encoding='utf-8-sig')) 
            health_vocab = health_list.workinglist
            health_table = randomlist.TableGenerator(health_vocab)
            nav_option()
            health_flashcards = flashcard.FlashcardGenerator(health_table)   
            nav_option()
            health_quiz = quiz.QuizGenerator(health_vocab)
            nav_option()
            health_contextquiz = quiz.ContextQuizGenerator(health_vocab)
            print(Fore.YELLOW + 'Super gemacht! Back to Menu!')
            menu()
 

        elif menu_option == '2':
            time_list = randomlist.Randomlist(open(f'time_vocab.csv','r',encoding='utf-8-sig'))
            time_vocab = time_list.workinglist        
            time_table = randomlist.TableGenerator(time_vocab)
            nav_option()
            time_flashcards = flashcard.FlashcardGenerator(time_table)
            nav_option()
            time_quiz = quiz.QuizGenerator(time_vocab)
            nav_option()
            time_contextquiz = quiz.ContextQuizGenerator(time_vocab)
            print(Fore.YELLOW + 'Super gemacht! Back to Menu!')

            menu()

        elif menu_option == '3':
            food_list = randomlist.Randomlist(open(f'food.csv','r',encoding='utf-8-sig'))
            food_vocab = food_list.workinglist
            food_table = randomlist.TableGenerator(food_vocab)
            nav_option()
            food_flashcards = flashcard.FlashcardGenerator(food_table)
            nav_option()
            food_quiz = quiz.QuizGenerator(food_vocab)
            nav_option()
            food_contextquiz = quiz.ContextQuizGenerator(food_vocab)
            print('Super gemacht! Back to Menu!')
           
            menu()

        elif menu_option == '4':
            travel_list = randomlist.Randomlist(open(f'travel_and_directions.csv','r',encoding='utf-8-sig'))
            travel_vocab = travel_list.workinglist
            travel_table = randomlist.TableGenerator(travel_vocab)
            nav_option()
            travel_flashcards = flashcard.FlashcardGenerator(travel_table)
            nav_option()
            travel_quiz = quiz.QuizGenerator(travel_vocab)
            nav_option()
            travel_contextquiz = quiz.ContextQuizGenerator(travel_vocab)
            print('Super gemacht! Back to Menu!')
           
           
            menu()

        elif menu_option == '5':
            spending_list = randomlist.Randomlist(open(f'money_and_transactions.csv','r',encoding='utf-8-sig'))
            spending_vocab = spending_list.workinglist
            spending_table = randomlist.TableGenerator(spending_vocab)
            nav_option()
            spending_flashcards = flashcard.FlashcardGenerator(spending_table)
            nav_option()
            spending_quiz = quiz.QuizGenerator(spending_vocab)
            nav_option()
            spending_contextquiz = quiz.ContextQuizGenerator(spending_vocab)
            print('Super gemacht! Back to Menu!')
            menu()

        elif menu_option != '1' or menu_option != '2' or menu_option != '3' or menu_option != '4' or menu_option != '5':
            raise MenuCheckError()

    except MenuCheckError:
        print('Choose a number from the topic menu to start.')
        menu()

menu()

   
                



        
   

    
