stackSize = int(input("โปรดระบุขนาด stack = "))
myStack = []*stackSize


def isEmpty():
    if len(myStack) == 0:
        return 1
    else:
        return 0


def isFull():
    if len(myStack) == stackSize:
        return 1
    else:
        return 0


def stackPush():
    myStack.append(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน stack = "))


def stackPop():
    myStack.pop(-1)


def stackTopstack():
    print("Top of Stack = {0}".format(myStack[-1]))


def stackDisplay():
    print(myStack)


while True:
    print("\nโปรดระบุทางเลือกในการดำเนินการกับ stack")
    print("1. PUSH : รับข้อมูลจัดเก็บใน stack")
    print("2. POP : ดึงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ stack ออก")
    print("3. Top of Stack : แสดงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ stack ทางจอภาพ")
    print("4. Display : แสดงข้อมูลที่จัดเก็บทั้งหมดใน stack ทางจอภาพ\n")
    select = int(input("ทางเลือกในการดำเนินการ = "))
    if select == 1:
        if isFull() == 1:
            print("ไม่สามารถจัดเก็บข้อมูลใน stack ได้เพราะ stack เต็ม")
            continue
        else:
            stackPush()
    elif select == 2:
        if isEmpty() == 1:
            print("ไม่สามารถดึงข้อมูลออกจาก stack เพราะไม่มีข้อมูลจัดเก็บใน stack")
            continue
        else:
            stackPop()
    elif select == 3:
        if isEmpty() == 1:
            print("ไม่สามารถแสดงค่า Top of Stack เพราะไม่มีข้อมูลใน stack")
            continue
        else:
            stackTopstack()
    elif select == 4:
        stackDisplay()
    else:
        break
