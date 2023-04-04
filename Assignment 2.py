
import traceback

def digit_sum(number):
    try:
        sum_digits = 0
        if isinstance(number, int) and number >= 0:
            for digit in str(number):
                sum_digits += int(digit)
            return sum_digits
        else:
            return None
    except:
        return None

def count_vowels(text):
    number_vowels = 0
    if isinstance(text, str):
            for v in text:
                if v in "aeiouAEIOU":
                    number_vowels += 1
            return number_vowels
    else:
        return None

def is_interlock(word_list, word1, word2):
    interlock = ""
    interlock_inverse = ""
    if(len(word1) == len(word2)):
        for i in range(len(word1)):
            interlock += word1[i]
            interlock += word2[i]
            interlock_inverse += word2[i]
            interlock_inverse += word1[i]
        if interlock in word_list or interlock_inverse in word_list:
            return True
        else:
            return False
    else:
        return False

import string
def count_types(a_string):
    string_dict = {'lowercase': 0,'uppercase': 0, 'numeric': 0, 'punctuation': 0, 'whitespace': 0}
    lowercase = 0
    uppercase = 0
    numeric = 0
    punctuation = 0
    whitespace = 0
    if isinstance(a_string, str):
            for v in a_string:
                if v.islower():
                    lowercase += 1
                if v.isupper():
                    uppercase += 1
                if v.isnumeric():
                    numeric += 1
                if v in string.punctuation:
                    punctuation += 1
                if v.isspace():
                    whitespace += 1
            string_dict['lowercase'] = lowercase
            string_dict['uppercase'] = uppercase
            string_dict['numeric'] = numeric
            string_dict['punctuation'] = punctuation
            string_dict['whitespace'] = whitespace
            return string_dict
    else:
        return None

def matmul(X, Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    test = []
    for r in result:
        test.append(r)
    return test

import math
def encode(text):
    norm_text = "".join(filter(str.isalnum, text)).lower()
    size = len(norm_text)
    cols = math.ceil(math.sqrt(size))
    if cols == 0:
        return ""
    chunks = [""  for i in range(cols)]
    for idx, c in enumerate(norm_text):
        idx = idx % cols
        chunks[idx] += c
    
    return " ".join(chunks)

def check_brackets(str_with_brackets):
    brackets_list= ['(','[','{','<',')',']','}','>']
    bracket_dict = {'(':')','[':']','{':'}','<':'>'}
    pair = []
    
    if any(i in str_with_brackets for i in brackets_list):
        for i in str_with_brackets:
            if i in brackets_list:
                if i in bracket_dict.keys():
                    pair.append(i)
                else:
                    if pair == []:
                        return False
                    open_bracket = pair.pop()
                    if i != bracket_dict[open_bracket]:
                        return False         
        if pair == []:
            return True
        else:
            return False
    else:
        return False

def nested_sum(list_of_lists):
    total = 0
    for i in range(len(list_of_lists)): 
        if type(list_of_lists[i]) == list :
            total+= nested_sum(list_of_lists[i])
        else:
            if isinstance(list_of_lists[i], int):
                total += list_of_lists[i]  
    return total

def count_people(log):
    log = log.split('\n')
    IN = 0
    OUT = 0
    for i in log:
        test = i.split('\t')
        if(test[0] == "IN"):
            IN += int(test[1])
        if(test[0] == "OUT"):
            OUT += int(test[1])
    return IN - OUT  

from collections import Counter
def next_word(text, word=None):
    text = text.lower().split(" ")
    most_likely_next_word = {}
    for set_word in set(text):
        container = []
        counter = []
        for i,val in enumerate(text):
            if set_word == val:
                try:
                    container.append(text[i + 1])
                except:
                    pass       
        container = dict(Counter(container))
        counter = [(k,v) for k,v in container.items()]
        counter.sort(key=lambda x: x[0])
        counter.sort(key=lambda x: -x[1])
        most_likely_next_word[set_word] = counter[0][0]
    if word is None:
        final_list = [(key,val) for key,val in most_likely_next_word.items()]
        final_list.sort(key=lambda x: x[0])
        return final_list
    else:
        return (word, most_likely_next_word[word])

