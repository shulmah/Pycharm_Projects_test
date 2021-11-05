def smallest(num):
	''' return index of (min_number)'''
	smallest = num[0]
	smallest_index = 0
	for i in range(1, len(num)):
		#print(num[i])
		if num[i] < smallest:
			smallest = num[i]
			smallest_index = i
			
	return smallest_index
		
num=[3,-5,-8, 2, -9, 1, 26, -2, -3, 0, 4]

print(num)
print(smallest(num))
		