test_word_list = ["z","a","b","b","b","b","c","."]
# document1 = ['"They had 16 rolls of duct tape, 2 bags of clothes pins,', 
#             '130 hampsters from the cancer labs down the hall, and',
#              'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
#              'said the source on a recent Geraldo interview.']

#def tokenize(document):
    # new_line = ""
    # for i in document:
        
    #     for j in range(len(i)):
    #         if i[j] == '"':
    #             new_line += ' " '
    #         elif i[j] == '.' or i[j] == ',':
    #             new_line += ' ' + i[j]
    #         elif i[j].isdigit():
                
                
    #             siffra =""
    #             z=1
    #             siffra += i[j]
    #             while i[j+z].isdigit():
                    
    #                 siffra += i[j+z]
    #                 if i[j + z + 1].isalpha() or i[j + z + 1].isspace():
    #                     break
    #                 z+=1
                
    #             j+=z
    #             new_line += (str(siffra) + " ")

    #         else:
    #             new_line += i[j]
            
    # line_split = new_line.split()

    # print(line_split)

# def tokenize(lines):
#     for line in lines:
#         for i in line:
#             print(i)
# #           Mellan rom ingenting
#             if i.isspace():

            #Kolla for ord
#             The next step is to recognize what kind of word you have. As we said in the beginning, there are three kinds of words:

#           those starting with a letter;
#           those starting with a digit;
#           and those which contain only one character which is neither letter nor digit.




        
# tokenize(document1)






def countWords(word_list,stop_words_file):
    stop_words=[]
    with open(stop_words_file) as f:
        for line in f:
            print(line.strip())
            stop_words.append(line.strip())


    word_count = {}
    for word in word_list:
        
        current_word_value = word_count.setdefault(word,0) 
        word_count[word] = current_word_value+1
    
    for word in stop_words:
        if word_count.get(word):
            word_count.pop(word)

    print(word_count)
      

countWords(test_word_list,"eng_stopwords.txt")


def tokenize(lines):
    word_count = 0
    word_count_list = []
    for line in lines:
        for word in line.split():
           while word and not word[0].isalnum():
               print(f"symbol : {word[0]}")
               word_count += 1
               word_count_list += word[0]
               word = word[1:]
           while word and not word[-1].isalnum():
               last = word[-1]
               word = word[:-1]
               if word: 
                  if word.isdigit():
                      print(f"number : {word}")
                      word_count += 1
                      word_count_list += word
                  else:
                      print(f"word : {word}")
                      word_count += 1
                      word_count_list += word
           if word:
               if word.isdigit():
                   print(f"number : {word}")
                   word_count += 1
                   word_count_list += word
               else:   
                   print(f"word : {word}")
                   word_count += 1
                   word_count_list += word
    print("Word count : " + str(word_count))  
    print(word_count_list)
         

tokenize(document1)
