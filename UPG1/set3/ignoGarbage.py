c=lambda n:str(n)if n<7else str(n%7)+c(n//7);[print("".join('0125986'[int(c)]for c in c(int(n))))for n in open(0)]
