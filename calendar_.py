numbers=list(range(1,10))
print(numbers)
for num in numbers:
	if num==1:
		print('\n1st')
	elif num==2:
		print('2nd')
	elif num==3:
		print('3rd')
	else:
		print(f'{num}th')
		
import calendar
print (calendar.month(2021,11))
