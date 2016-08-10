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
			print(roster_fn_list[count])
		if 'E' in roster_fn_list[count]:
			e_names += 1
			print(roster_fn_list[count])
		count += 1
	print(e_names, "names with 'e' in them.")
	#roster_list = roster.split()
	


def main():
    letter_e()

if __name__ == '__main__':
    main()