a = int(input('secunds?:'))
h = a // 3600
m = a % 3600
k = m // 60
s = m % 60
# print(h,":",k,":",s,sep="")
x = str()
y = str()

if k < 10:
    y = '0' + str(int(k))
else: y = k

if s < 10:
    x = "0" + str(int(s))
else: x = s

print(h, ":", y, ":", x, sep="")
