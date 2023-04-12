Username = input("Enter your UserName: ")
Password = input("Enter your Password:")

if Username == "admin" and Password == "admin":
    print("Done")

    print("----- SHOPHEE-----")
    print("สินค้าในร้าน----------")
    print("1. ปลากระป๋อง    20฿")
    print("2. ปลาท่องโก๋    50฿")
    print("3. ออกจากโปรเเกรม  ")
    print("------------------")
    datainput = int(input(">>"))
    if datainput == 1:
        amount = int(input("เอากี่อันงับ: "))
        print("-------Total------")
        print("ปลากระป๋อง:", amount, "อัน")
        print("ทั้งหมดราคา",(20*amount),"บาท")
        print("------------------")
    elif datainput == 2:
        amount = int(input("เอากี่อันงับ: "))
        print("-------Total------")
        print("ปลาท่องโก๋:", amount, "อัน")
        print("ทั้งหมดราคา",(50*amount),"บาท")
        print("------------------")
    elif datainput == 3:
        print("Exit")
else:
    print("wrong Password")