e_names_file = open('e_names.txt', 'w')
roster = open('roster.txt', 'r')

def letter_e():
	count = 1
	e_names = 0
	roster_string = roster.read()
	roster_list = roster_string.split()
	roster_fn_list = roster_list[:41:2] + roster_list[43::2]
	
	
	while count <= (len(roster_fn_list))-1:
		if 'e' in roster_fn_list[count]:
			e_names += 1
			e_names_file.write(str(roster_fn_list[count]) + ' ')
		if 'E' in roster_fn_list[count]:
			e_names += 1
			e_names_file.write(str(roster_fn_list[count]) + ' ')
		count += 1
	e_names_file.close()
	roster.close()
	# I tried to re-open the file to print it out using the code on lines 24-25, but kept getting this error >> 
	# UnboundLocalError: local variable 'e_names_file' referenced before assignment
	
	# e_names_file = open('e_names.txt', 'r')
	# print(e_names_file.read())		
	

def main():
    letter_e()

if __name__ == '__main__':
    main()