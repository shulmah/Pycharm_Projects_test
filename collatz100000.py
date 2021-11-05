def get_collatz(n,qty):
    '''Функция get_collatz рекурсивно перебирает последовательность
    и возвращает количество итераций когда последовательность вышла на 1.
    Если число итераций > предыдущего записываем в переменную 'a' само число,
    а в 'n' длину его последовательности.'''
    if n == 1:
        return qty
    elif n%2 == 0:
        return get_collatz(int(n/2),qty+1)
    else:
        return get_collatz(3*n+1,qty+1)
n = 0
a = 0
for i in range(13,15):
    c = get_collatz(i,0) #steps to '1'
    if c > n:
        a,n = i,c
print(a,n)
