#скорость в питоне не главное ;), хотя дядя Лутц говорит, что генераторы быстрее в данном случае
def optimus_prime(val):
    return [x for x in range(2,val+1) if all((x%y for y in range(2,1+int(x**0.5))))]
    
print(optimus_prime(5500))
