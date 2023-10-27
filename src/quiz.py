#quiz generator
#get the context sentences from csv
#match keyword in the context sentence with the target vocab
# can I create a checker activity for it?
#can I block out the key word?
#how could I do that? replace it with a '____'?


import csv
import random
import string

# def extract_words_using_find(input_string):
#     words = [input_string[start:space_index] for start, space_index in enumerate(input_string.split(' '))]
#     return words

##vocablist = [r for r in csv.DictReader(open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))]
#randomlist = random.sample(vocablist, 3)
#print(randomlist)

def quizGenerator(listname):
    for item in listname:
        sentence = item['Context'].split()
        matchlist = item['German'].split()
        print(sentence)
        print(matchlist)
        for word in sentence:
            # word = word.translate
            # (str.maketrans('', '', string.punctuation))
            word_nopunct = str.maketrans('', '', string.punctuation)
            print(word.translate(word_nopunct))


            #if word == item['German']:
                #matchlist = item['German'].split()
            for match in matchlist:
                    article = 'der' or 'die' or 'das'
                    if word_nopunct != article and word_nopunct == match:
                    #if word == match:
                        sentence[(sentence.index(word))] = "__________"
                        separator = " "
                        input = input(f'Which word is missing        {(separator.join(sentence))}  ')
                    #print(match)
                        if input == match:
                            print('Richtig!')
                        if input == (f'match'+'.'):
                            print('Richtig!')
                        if input != match:
                            print(f"The answer was '{match}''")






#get the example sentence with the keyword blocked out.
#match the keyword to the sentence and replace it with a block
#turn the sentence into a list of strings that I can interate over and match
#to do this I need to ignore the punctuation or I'll get errors
#get user input for the answer
#return the feedback if answer is correct or not

# import string
 
# test_str = 'Gfg, is best: for ! Geeks ;'
 
# test_str = test_str.translate
#     (str.maketrans('', '', string.punctuation))
# print(test_str)



#    ' '.join(wordlist)
# separator = ', ' 

# result = separator.join(my_list) 

# print(result)
   #print(item['German'])
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


#     #print(wordlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

        
        #for i in item['Context']:
                #print(i)
    #     if word == item['German']:
    #         print(word)


    # sentence = item['Context']
    # result_words = extract_words_using_find(sentence)
    # print(result_words)
    


    




#     matchlist = item['German'].split()
#     print(sentence)
#     print(matchlist)
    #for word in sentence:
    


        #if word == item['German']:
        #     #matchlist = item['German'].split()
        # for match in matchlist:
        #          article = 'der' or 'die' or 'das'
        #         if word_nopunct != article and word_nopunct == match:
        #         #if word == match:
        #             sentence[(sentence.index(word))] = "__________"
        #             separator = " "
        #             input = input(f'Which word is missing        {(separator.join(sentence))}  ')
        #          #print(match)
        #             if input == match:
        #                 print('Richtig!')
        #             if input == (f'match'+'.'):
        #                 print('Richtig!')
        #             if input != match:
        #                 print(f"The answer was '{match}''")

#get the example sentence with the keyword blocked out.
#match the keyword to the sentence and replace it with a block
#turn the sentence into a list of strings that I can interate over and match
#to do this I need to ignore the punctuation or I'll get errors
#get user input for the answer
#return the feedback if answer is correct or not

# import string
 