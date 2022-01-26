def max2(x,y):        # максимум из 2-х чисел
	return x if x>y else y

spis= [8, 5, 9, 91,43,17,5,88,28,52,99] 

mem = max2(spis[0], spis[1])
for i in range(2,len(spis)):
	if i >= len(spis):
		break
	mem = max2(spis[i], mem)

print('max =',mem) # печать наибольшего из списка
