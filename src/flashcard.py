

from colorama import Fore, Back, Style
import randomlist


class FlashcardGenerator:
    def __init__(self, tablename):
        self.tablename = tablename
      
        print(Fore.MAGENTA + "FLASHCARD GENERATOR ...\n")
        direction = input(f" Press E for English > German, or G for German > English  (or any key to skip)   ")
        if direction == 'E':
            self.flash_eng(tablename)
        if direction == 'G':
            self.flash_germ(tablename)


    def flash_eng(self,tablename):
        index = 0
        while index < len(randomlist.englishlist):
            print(Fore.MAGENTA + '\n==================')
            print(Fore.MAGENTA, Style.BRIGHT + randomlist.englishlist[index])
            input()
            input(randomlist.germanlist[index])
            index += 1
        nav = input('Nochmal? Press E for English first, G for German first,or any key for QUIZ. \n')
        if nav == 'E':
                self.flash_eng(tablename)
        if nav == 'G':
                self.flash_germ(tablename)
        

    def flash_germ(self,tablename):
        index = 0
        while index < len(randomlist.englishlist):
            #response = input()
            print('\n==================')
            print(randomlist.germanlist[index])
            input()
            input(randomlist.englishlist[index])
            index += 1
        nav = input('Nochmal? Press E for English first, G for German first,or any key for QUIZ.')
        if nav == 'E':
                self.flash_eng(tablename)
        if nav == 'G':
                self.flash_germ(tablename)
       

           
        
        







            
