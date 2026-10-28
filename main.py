import calendar

def paivia_kuukaudessa(v, k):
    p = 0
    if k in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif k in [4, 6, 9, 11]:
        return 30
    elif k == 2:
        if calendar.isleap(v):
            return 29
        else:
            return 28
    return 0

v = int(input('Anna vuosi: '))
k = int(input('Anna kuukauden numero 1-12: '))
p = paivia_kuukaudessa(v, k)
print(p)
