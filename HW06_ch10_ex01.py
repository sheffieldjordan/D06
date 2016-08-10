# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
import math
def nested_sum(t):
	total_sum = 0
	for item in t:
		total_sum += sum(item)
	return total

# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# bus_stops = [1, 52, 25, [251, 252, 253], 14]
# countries = [4, 3, 1, [11, 12], 1, [14, 19], 17]


# print(nested_sum(bus_stops))
# print(nested_sum(countries))

def main():
	pass

if __name__ == '__main__':
    main()