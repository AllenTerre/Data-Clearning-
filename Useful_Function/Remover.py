# -*- coding: utf-8 -*-
"""
Basic knowledge of data cleaning. 

First part: 
    
    Remove or keep characters in a long string. 
    
"""

# How to only keep the numbers in a string. 

message = "This is my telephone number: 4239870945"

def keep_numbers(string):
    filter_obj = filter(str.isdigit, string)
    withdraw = ''.join(list(filter_obj))
    return withdraw

new_message = keep_numbers(message)

# keep letters 

test_message = 'brave001'

def keep_letters(string):
    filter_obj = filter(str.isalpha, string)
    withdraw = ''.join(list(filter_obj))
    return withdraw


new_test_message = keep_letters(test_message)

# keep both numbers and letters 

test_message2 = 'Halifax\n.!001[]123'

def keepNL(string):
    filter_obj = filter(str.isalnum, string)
    withdraw = ''.join(list(filter_obj))
    return withdraw

new_test_message2 = keepNL(test_message2)
    
print(new_test_message2)
















