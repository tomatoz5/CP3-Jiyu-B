number = int(input("input row: "))
for x in range(number):
    print(" "*(number-(x+1)) + "*"*((x*2)+1))