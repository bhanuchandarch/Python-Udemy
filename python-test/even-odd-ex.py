#Write a program to count no.of even and odd numbers from a series

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0

for value in range(1, 10):
	if value%2==0:
		even = even + 1
	else:
		odd = odd + 1

print("Number of Even Numbers: ", even)
print("Number of Odd Numbers: ", odd)