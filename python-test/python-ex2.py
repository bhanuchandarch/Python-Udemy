#Write a Program to print 1-50. multiples of 3 "Fizz", 5 "Buzz", 3 and 5 "FizzBuzz"

for value in range(1, 51):
	if value%3==0 and value%5==0:
		print("FizzBuzz")
	elif value%5==0:
		print("Buzz")
	elif value%3==0:
		print("Fizz")
	else:
		print(value)
