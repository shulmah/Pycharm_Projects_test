def summa(j,k):
	'''вернет сумму чисел от 1 до К, каждое в степени j'''
	summa = 0
	for i in range(1,k+1):
		summa += i**j
	return(summa)

#print(summa(2,3))
a = summa(2,5)
print(a)

