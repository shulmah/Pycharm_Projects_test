abcd = int(input())
a = abcd//1000
#print(a)

bcd = abcd%1000
#print(bcd)
b = bcd//100
#print(b)
cd = bcd%100
#print(cd)
c = cd//10
#print(c)
d = cd%10
#print(d)
if a==d and b==c:
 print(1) # симметрия в числе из 4 знаков 1221
else:
 print(202)
