n = int(input('n ='))
m = int(input('m ='))

if n <= m:
    print("n <= m")
elif n % m == 0:
    print("yes")
else:
    print("no")