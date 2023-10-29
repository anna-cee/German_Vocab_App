

from cli_color_py import red, bright_yellow, green, blue, bold, magenta
import classlist


class FlashcardGenerator:
    def __init__(self, tablename):
        self.tablename = tablename
      
        print(magenta("FLASHCARD GENERATOR ...\n"))
        direction = input(f" Press E for English > German, or G for German > English  (or any key to skip)   ")
        if direction == 'E':
            self.flash_eng(tablename)
        if direction == 'G':
            self.flash_germ(tablename)


    def flash_eng(self,tablename):
        index = 0
        while index < len(classlist.englishlist):
            print(magenta('\n=================='))
            print(bold(magenta(classlist.englishlist[index])))
            input()
            input(classlist.germanlist[index])
            index += 1
        nav = input('Nochmal? Press E for English first, G for German first,or any key for QUIZ. \n')
        if nav == 'E':
                self.flash_eng(tablename)
        if nav == 'G':
                self.flash_germ(tablename)
        

    def flash_germ(self,tablename):
        index = 0
        while index < len(classlist.englishlist):
            #response = input()
            print(magenta('\n=================='))
            print(bold(magenta(classlist.germanlist[index])))
            input()
            input(classlist.englishlist[index])
            index += 1
        nav = input('Nochmal? Press E for English first, G for German first,or any key for QUIZ.')
        if nav == 'E':
                self.flash_eng(tablename)
        if nav == 'G':
                self.flash_germ(tablename)
        
        







            
