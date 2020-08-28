#break
#continue
#enumerate

l = [10, 20, 30, 40, 50, 60]

key = 40

for value in l:
	print(value)
	if value == key:
		print("Element found")
		break
	else:
		continue
else:
	print("Element Not Found")

for index,value in enumerate(l):
	print(value)
	if value == key:
		print("Element found found at index: ", index)
		break
	else:
		continue
else:
	print("Element Not Found")
