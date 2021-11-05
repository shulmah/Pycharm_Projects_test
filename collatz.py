def collatz(num):
    if num % 2 == 0:
        return (num // 2)
    else:
        return (3*num + 1)

numm = int(input('numm?'))

a = collatz(numm)
print(a)
b = collatz(a)
print(b)
i=0
while abs(b-a)!= 1:
    # if abs(a-b) < 2:
    #     break
    a = collatz(b)
    print('a=',a)
    b = collatz(a)
    print('b=',b)

    i+=1
print('i =',2*i+1,'COLLATZ!!!')
