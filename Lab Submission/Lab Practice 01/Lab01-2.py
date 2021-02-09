myStack = []*8


def isEmpty():
    if len(myStack) == 0:
        return 1
    else:
        return 0


def isFull():
    if len(myStack) == 8:
        return 1
    else:
        return 0


def stackPush():
    myStack.append(int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน stack = ")))


def stackPop():
    myStack.pop(-1)


while True:
    print("\nโปรดระบุทางเลือกในการดำเนินการกับ stack")
    print("1. PUSH : รับข้อมูลจัดเก็บใน stack")
    print("2. POP : ดึงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ stack ออก\n")
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
    else:
        sums = 0
        for i in myStack:
            sums = sums + i
        print("ผลรวมของจำนวนเต็มที่จัดเก็บใน stack = {0}".format(sums))
        break
