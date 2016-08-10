import random 

def write_random():
	num_file = open('Morgan.txt','w')
	counter = 0
	while counter <= 10: 
		num_file.write(str(random.random()) + '\n')
		counter = counter + 1
	num_file.close()
	num_file = open('Morgan.txt','r')
	return num_file.read()
	

def main():
    print(write_random())

if __name__ == '__main__':
    main()
