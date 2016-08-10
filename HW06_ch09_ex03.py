#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
fin = open('words.txt')

# Body
fin_string = fin.read()
fin_list = fin_string.split()

not_forbidden_word = []

def avoids(word, forbidden):
    """ return True if word NOT forbidden"""
    for letters in word:
        if letters not in forbidden:
            return True
        return False
    
def forbidden_prompt():    
    count = 0
    forbidden_letters = input("Enter a string of forbidden letters:")
    for word in fin_list:
        if avoids(word, forbidden_letters):
            not_forbidden_word.append(word)        
            count += 1
    print(count) 


#def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    ...


def forbidden_param(forbidden_letters):
    """ return count of words NOT forbidden by param"""
    return count 


def find_five():
    ...


##############################################################################
def main():
    print(forbidden_prompt())

if __name__ == '__main__':
    main()

    