c=lambda n:'0125986'[n%7]+(n>6and c(n//7)or"")
for n in open(0):print(c(int(n)))
