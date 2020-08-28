
#syntax

#for [variable_name] in [iterable datatype]:

#	statements

#Iterable datatypes
#str list tuple dict set

l = [10, 20, 30, 40, 50]

sum = 0
for value in l:
	sum = sum + value

print(sum)

for value in range(1, 11):
	print(value)

sum = 0
for value in range(1, 11):
	sum = sum + value	
print(sum)
