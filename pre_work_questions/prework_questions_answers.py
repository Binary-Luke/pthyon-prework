# Question 1:

# 'Write a function to print "hello_USERNAME!" USERNAME is the input'


def hello_name(user_name):
        name = user_name.upper()
        print("hello_" + name + "!")

hello_name("Luke Sousa")

# Question 2:

# 'Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing'

def first_odds():
    odds = []
    for num in range(1,101):
        if num % 2 != 0:
            odds.append(num)
    print(odds)

print(first_odds())

# Question 3

# 'Please write a Python function, max_num_in_list to return the max number of a given list.'


def max_num_in_list(a_list):    
    max = a_list[0] 
    for x in a_list:
        if x > max:
            max = x
    return max

a_list = [1, 5, 6, 3]
print(max_num_in_list(a_list))

# Question 4

# 'Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.'

def is_leap_year(a_year):
    if (a_year % 400 == 0) and (a_year % 100 == 0):
        return True
    elif (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    else:
        return False
      
print(is_leap_year(1985))

# Question 5

# 'Write a function to check to see if all numbers in list are consecutive numbers'

def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    range_list = list(range(min(a_list), max(a_list) +1))
    if sorted_list == range_list:
        return True
    else:
        return False

my_list = [20,21,24,23,22]
print(is_consecutive(my_list))

