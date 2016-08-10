#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports
fin = open('words.txt')

# Body

fin_string = fin.read()
fin_list = fin_string.split()
no_e = []

def has_no_e():
	for word in fin:
		if 'e' not in word:
			no_e.append(word.strip())
			continue
			return True


def print_no_e():	
	print(no_e,'\n')
	percentage = (len(no_e)) / (len(fin_list)) * 100
	print(percentage, "percent of the words have no e.")

# I can't figure out why this does not run. But if I run the fin.read(),
# then the no_e list always returns empty. 
# However, if I don't run fin.read(), then the list no_e has the 37,000 words in it. 



# ##############################################################################
def main():
	has_no_e()
	print_no_e()
if __name__ == '__main__':
    main()


