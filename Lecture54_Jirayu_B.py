def login():
    print("------Login------")
    userName = input("UserName: ")
    Password = input("Password: ")
    if userName == "admin" and Password == str(1234):
        return showmenu()
    else:
        return login()

def showmenu():
    print("---- MINIMENU ----")
    print("1. Vat calculator")
    print("2. Price Calculator")
    print("3. Exit")
    return menuselect()
def menuselect():
    userSelected = int(input("Select: "))
    if userSelected == 1:
        price = int(input("ใส่ราคาเพื่อคิดออกมาเป็น VAT: "))
        return print(vatcal(price))
    elif userSelected ==2:
        return pricecal()
    elif userSelected ==3:
        print("THANK YOU")
def vatcal(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice*vat/100)
    return  result
def pricecal():
    price1 = int(input("ราคาที่1: "))
    price2 = int(input("ราคาที่2: "))
    return vatcal(price1+price2)

result = login()
if result:
    print(result)

