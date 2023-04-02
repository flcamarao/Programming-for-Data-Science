
def chop(a_list):
    a_list.pop()
    del a_list[0]
    return None

def sum_multiples(a_list):
    total = 0
    for i in a_list:
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def rotate(numbers, k):
    rotated = numbers
    if k > 0:
        for i in range(0,abs(k)):
            rotated.insert(0,numbers.pop())
    else:
        for i in range(0,abs(k)):
            rotated.append(numbers.pop(0))
    return rotated

def on_all(func, a_list):
    new_list = []
    for i in a_list:
        new_list.append(func(i))
    return new_list

def matrix_times_vector(mat, vec):
    new_mat = []
    new_vec = []
    var1 = 0
    var2 = 0
    product = []
    for i in mat:
        for a in i:
            new_mat.append(a)
        for b in vec:
            new_vec.append(b)
    for x in range(len(new_mat)):
        if x < len(vec):
            var1 += new_mat[x] * new_vec[x]
        else:
            var2 += new_mat[x] * new_vec[x]
    product.append(var1)
    product.append(var2)    
    return product  

def coder(text, to_morse=True):
    """Convert English text to Morse code and vice versa
    Parameters
    ----------
    text : str
        English text or Morse code text
    to_morse : boolean
        Converts text to Morse code if `True`, to English otherwise
        
    Returns
    -------
    coded_text : str
        Text converted to Morse code or English
    """
    if(to_morse == True):
        encrypted = ''
        decrypted = ''
        for i in text:
            if i != ' ':
                i = i.upper()
                encrypted += alpha_to_morse[i] + ' '
            else:
                encrypted += '  '
        return encrypted.strip()
    else:
        decipher = ''
        citext = ''
        text = text + ' '
        for letter in text:
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i % 2 == 0 :
                    decipher += ' '
                    i = 0
                elif(citext != ''):
                    decipher += morse_to_alpha[citext]
                    citext = ''
        return decipher

def custom_key(key_element):
    return key_element[1]

def sort_by_key(items_with_keys, ascending=True):
    """Sort items_with_keys based on the keys then by item for same keys
    
    Parameters
    ----------
    items_with_keys : list of tuples
        list of (item, key) tuples to be sorted
    ascending : bool
        Sort in ascending order if True, in descending order otherwise
    """
    if(ascending == True):
        items_with_keys.sort(key=custom_key)
        return items_with_keys
    else:
        items_with_keys.sort(key=custom_key, reverse = True)
        return items_with_keys

def count_words(text):
    text = text.lower()
    text = text.split()
    wc = {}
    count = 0
    for item in text:
        count = text.count(item)
        wc[item] = count
    return wc

from typing import Dict
def display_tree(content):
    nest1 = ''
    dict1 = {}
    dict2 = {}
    dict3 = {}
    content_sorted = sorted(content)
    for i, val in enumerate(content_sorted):
        count = i
        if(count == 0):
            nest1 += val + ":\n"
        else:
            nest1 += val + ":"
        for i, val in enumerate(content):
            dict1 = content[val]
            if isinstance(dict1, Dict):
                if(count == 0):
                    dict2 = sorted(dict1)
                    for i, val in enumerate(dict2):
                        if isinstance(dict1[val], Dict):
                            dict3 = dict1[val]
                            nest2 = "  " + dict2[i] + ':\n'
                            nest1 += nest2
                            for i, val in enumerate(dict1[val]):
                                nest3 = "    " + str(val) + ': ' + dict3[val] + '\n'
                                nest1 += nest3
                        else:
                            nest2 = val +': '+ dict1[val] + '\n'
                            nest1 += "  " + nest2
            else:
                if(count == 1):
                    nest1 += " " + str(dict1) + '\n'
        count += 1
    return nest1        

def get_nested_key_value(nested_dict, key):   
    nested_value = {}
    new_key = key.split('.')
    number_of_loop = len(new_key)
    counter = 0
    while counter < number_of_loop:        
        for i in new_key[counter]:
            if(counter > 0):
                if new_key[counter] in nested_value:
                    nested_value = nested_value[new_key[counter]]
                else:
                    return None
                break
            else:
                nested_value = nested_dict[new_key[counter]]
                break
        counter += 1
    return nested_value

def get_nested_key_value(nested_dict, key):
    key_list = key.split('.', 1)
    
    if len(key_list) == 1:
        if key_list[0] in nested_dict:
            return nested_dict[key_list[0]]
        else:
            return None

    return get_nested_key_value(nested_dict[key_list[0]], key_list[1])
