where = int(input("how much to calculate=="))
odd = 0
even = 0
for i in range(1,where+1):
    if i%2 == 1:
        odd += i
    else:
        even += i/(where//2)
print(odd)
print(even)