menuList = []
priceList = []

def showbill():
    print("---- MY SHOP ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    print("---- Total ----")
    total_price = sum(priceList)
    print("รวม", total_price, "บาท")



while True:
    menuName = input("Please Enter Menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Input Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)

showbill()



