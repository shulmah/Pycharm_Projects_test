def maximum(x, y):
	if x > y:
		return x
	elif x == y:
		return 'числа равны',x
	else:
		return y
#print(maximum(6, 2))
#print(max(34,22))#встр.фция'max'
print('input two nums ?')
a = maximum(x=int(input()), y=int(input()))
print('maximum of two nums =',a)
print('input one num ?')
b = maximum(x=int(input()), y=a)
print('maximum of three nums =',b)
