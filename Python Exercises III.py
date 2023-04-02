import csv
def value_counts(a_list, out_path):
    a = []
    b = []
    for i in a_list:
        a += str(i)
        b.append(a_list.count(i))
    c = sorted(dict(zip(a,b)).items(), key=lambda x: (-x[1], x[0])) 
    with open(out_path, 'w') as f:
        writer = csv.writer(f)
        for d in c:
            writer.writerow(d)
    return writer

def is_subset(sublist, superlist, strict=True):
    loop_counter = 0
    index_counter = 0
    list_checker = 0
    result = 0
    if strict:
        if(set(sublist).issubset(set(superlist))):
            while loop_counter < len(superlist):
                for i in range(len(superlist)):
                    if(sublist[i] == superlist[i-index_counter]):
                        list_checker += 1
                        if(list_checker == len(sublist)):
                            result = 1
                            break
                    else:
                        index_counter += 1
                        break
                loop_counter += 1
            if(result > 0):
                return True
            else:
                return False
    else:
        return set(sublist).issubset(set(superlist))

def has_duplicates(a_list):
    checker = 0
    for i in a_list:
        if(a_list.count(i) > 1):
            checker = 1
    if(checker > 0):
        return True
    else:
        return False

import pickle
def count_words(input_file, output_file):
    file = open(input_file, "r")
    file = file.read().lower().split()
    wc = {}
    count = 0
    for item in file:
        count = file.count(item)
        wc[item] = count
    with open(output_file, 'wb') as f:
        pickle.dump(wc, f)

class Person:
    infected = False
    def __init__(self, xy = (0,0)):
        self.x = xy[0]
        self.y = xy[1]
        self.position = (self.x, self.y)
        
    def get_position(self):
        return self.position
    
    def move(self, x = 0, y = 0):
        self.position = (self.position[0] + x, self.position[1] + y)
        return self.position

    def is_infected(self):
        return self.infected
    
    def set_infected(self):
        self.infected = True
        return self.infected
    
    def get_infected(self, person, threshold):
        ed = 1/2*((person.x - self.x)**2 + (person.x - self.y)**2)
        if person.is_infected() == True and ed < threshold: 
            self.infected = True

class Person:
    infected = False
    def __init__(self, xy = (0,0)):
        self.x = xy[0]
        self.y = xy[1]
        self.position = (self.x, self.y)
        
    def is_infected(self):
        return self.infected
    
    def set_infected(self):
        self.infected = True
        return self.infected
    
    def get_infected(self, person, threshold):
        ed = 1/2*((person.x - self.x)**2 + (person.x - self.y)**2)
        if person.is_infected() == True and ed < threshold: 
            self.infected = True

class QuarantinedPerson:
    def __init__(self, xy = (0,0)):
        self.x = xy[0]
        self.y = xy[1]
        self.position = (self.x, self.y)
      
    def move(self, x = 0, y = 0):
        self.position = (self.position[0] + x, self.position[1] + y)
        return self.position
    
    def set_infected(self):
        self.infected = True
        return self.infected
    
    def is_infected(self):
        return self.infected   

import os.path
from os import path
def file_lines(**filepaths):
    result = {}
    for k, v in filepaths.items():
        if(path.exists(v)):
            with open(v, 'r') as fp:
                x = len(fp.readlines())
                x = {k:x}
                result.update(x)
    return result

class TenDivError(Exception):
    def __init__(self, exception):
        super().__init__(exception)
    
def ten_div(numerator, denominator):
    message = "Error encountered: "
    try:
        if(numerator >= 0) and  (numerator <= 10):
            return numerator/denominator
        else:
            raise TenDivError(message)
    except Exception as e:
        raise TenDivError(f'{message}{e}')

file = open("wordfreq.py", "w") # opening the module
text = """ 
def most_frequent(filepath):
    file = open(filepath, "r")
    file = file.read().lower().split()
    wc = {}
    count = 0
    for item in file:
        count = file.count(item)
        wc[item] = count
    c = sorted(wc.items(), key=lambda x: (-x[1], x[0])) #sorting descending and then ascending order
    d = []
    i = 0
    while i < 9: # limiting the values upto 9 most frequent words
        d.append(c[i][0])
        i += 1
    return d
if __name__ == '_main_':
    most_frequent(filepath)
"""
with open('wordfreq.py', 'w') as f: #creating the module
        f.write(text)
        f.close()


