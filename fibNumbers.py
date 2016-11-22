fib = [1,2]

def fib_seq(number_of_elements_in_fib):
	index = 0
	while index < number_of_elements_in_fib:
		fib.append(fib[-2] + fib[-1])
		index += 1
	return fib

print fib_seq(10)
