print (' стих построчно: ')
while (1):
	s=str(input())#ввод строки
	if (s=='ккк'):
		break		#конец ввода,выход
	i=0
	for x in s:
		if (x in 'аеëиоуыэюяАЕËИОУЭЮЯ'):
			i+=1	#подсчëт гласных
	print ('кол-во гласных: ', i)
