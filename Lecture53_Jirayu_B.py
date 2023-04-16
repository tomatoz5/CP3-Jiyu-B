def vatcal(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

inputdata = int(input("total price: "))
print(vatcal(inputdata))
