def count_and_print(n):
    x = 1
    while x <= n:
        if(x % 6) == 0: #divisible by 6
            print(str(x) + " foo")
        elif(x % 2) == 0: #divisible by 2
            print(str(x) + " fizz")
        elif(x % 3) == 0: #divisible by 3
            print(str(x) + " fuzz")
        else:
            print(x)
        x += 1

def overlap_interval(start1,end1,start2,end2):
    start = min(start1, start2) + 1 # getting the starting point
    end = max(end1, end2) # the ending of the points
    overlap = []
    if start2 > end1: # if the start of the 2nd endpoints there will be no overlap
        print("No overlap!")
    else:
        for i in range(start, end):
            if i in [start1, start2, end1, end2]: #checking if the the point inside the endpoints
                overlap.append(i)
        print(overlap[0],overlap[1])

import math
def cosine(theta):
    cos_theta = 1 
    n = 1 
    term = 1 
    while abs(term) >= 1e-15:
        term = (-1)**n * theta**(2*n) / math.factorial(2*n) # compute the term
        cos_theta += term # add the value of term
        n += 1 
    return cos_theta

def gcd(a,b):
    while b != 0: # end when the divisor and remainder is equal to zero
        r = a % b  
        (a,b) = (b,r) # gcd(a,b) = gcd(b,r)
    return a
gcd(10,20)

def biased_sum(*args,base = 2): #using args when you have indefinite amount of arguments
    total_sum = 0
    for i in args:
        if i % base == 0: #checking if its a multiple of the base
            total_sum += i * 2 #double the value since its a multiple
        else:
            total_sum += i
    return total_sum

def last_in_sequence(string_digits):
    start = 0
    if("0" in string_digits): #check if the string contains 0 for the sequence
        for i in range(0,len(string_digits)):
            if (int(string_digits[i]) == start):
                last_digit = start
                if (start <= 8): #check if there is another set of sequence after 9
                    start = start + 1
                else:
                    start = 0
        return last_digit
    else:        
        return None

def check_password(password):
    if(len(password) > 7) & (any(i.islower() for i in password)) & (any(i.isupper() for i in password)) & (any(i.isdigit() for i in password)):
        return True
    else:
        return False

def is_palindrome(text):
    if(text == ""):
        return False
    else:
        text = text.replace(" ", "")
        return text == text[::-1]

def create_squares(num_stars):
    squares = ""
    alternate = 2
    for a in range(2):
        for a in range(2):
            squares += "+ "
            for a in range(num_stars):
                squares += "- "
        squares += "+\n"
        for a in range(num_stars):
            for a in range(2):
                squares += "| "
                if(alternate % 2 == 0):
                    for a in range(num_stars):
                        squares += "* "
                    alternate += 1
                else:
                    for a in range(num_stars):
                        squares += "  "
                    alternate += 1
            squares += "|\n"
        alternate += 1
    for a in range(2):
        squares += "+ "
        for a in range(num_stars):
            squares += "- "
    squares += "+\n"    
    return squares

def create_grid(num_squares, num_stars):
    squares = ""
    alternate = 2
    for a in range(num_squares):
        for a in range(num_squares):
            squares += "+ "
            for a in range(num_stars):
                squares += "- "
        squares += "+\n"
        for a in range(num_stars):
            for a in range(num_squares):
                squares += "| "
                if(alternate % 2 == 0):
                    for a in range(num_stars):
                        squares += "* "
                    alternate += 1
                else:
                    for a in range(num_stars):
                        squares += "  "
                    alternate += 1
            squares += "|\n"
        alternate += 1
    for a in range(num_squares):
        squares += "+ "
        for a in range(num_stars):
            squares += "- "
    squares += "+\n"    
    return squares

