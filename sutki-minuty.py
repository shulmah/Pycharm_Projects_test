m = int(input("minuts=?"))
ch = m // 60
min = m % 60
sut = ch // 24
ch = ch % 24
print(sut, ch, min, sep='-')
print("vsego: sutok={} chasov={} minut={}".format(sut, ch, min))

