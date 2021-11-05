def sortix(a,b,c):
    '''sorting 3 numbers to upper'''
    if c <= b <= a:
        b, a = a, b
    if c <= a <= b:
        c, a = a, c
    if b <= c <= a:
        c, a = a, c
    if b <= a <= c:
        b, a = a, b
    if a <= c <= b:
        c, b = b, c
    if a <= b <= c:
        print('a={} b={} c={}'.format(a, b, c))
    return a,b,c

print('input triangle ?')
x,y,z = sortix(a=int(input()), b=int(input()), c=int(input()))

if z >= x + y:
    print('treuk unpossible')
elif z**2 == x**2+y**2:
    print('treug=pramoug {} {} {}'.format(x,y,z))
elif z**2 <= x**2 + y**2:
    print('treug=ostroug {} {} {}'.format(x,y,z))
elif z**2 >= x**2 + y**2:
    print('treug=tupoug {} {} {}'.format(x,y,z))


print()
print()
print(x**2,y**2,z**2)
