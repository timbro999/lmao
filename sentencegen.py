import random
import time


sentence_list = []
x=0
def noun_gen(lang_ft):
    ran_num = random.randint(0, 9)
    i=ran_num
    lang_ft = open("{}.txt".format(lang_ft))
    list = lang_ft.read().split(";")

    sentence_list.append(list[i])


while x < 11:

    type = random.randint(0, 2)
    if type == 0:
        noun_gen("adjectives")
    if type == 1:
        noun_gen("nouns")
    if type == 2:
        noun_gen("verbs")
    x+=1
    if x == 10:
        final_list = sentence_list
        print(sentence_list)










