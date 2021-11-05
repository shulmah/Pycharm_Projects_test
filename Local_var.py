def localsNo():
    return locals()

def localsYes():
    present = True
    number = 29
    return locals()

print('localsNo:',localsNo())
print('localsYes:',localsYes())

# localsNo: {}
# localsYes: {'present': True, 'number': 29}
