class Queue:

    def __init__(self, n):
        self.n = n
        self.queue = [0] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        try:
            if self.rear == self.n - 1:
                print('Queue เต็ม')
            else:
                if self.front == -1:
                    print('Add item : ', item)
                    self.front = 0
                    self.rear = 0
                    self.queue[self.rear] = item
                else:
                    print('Add item : ', item)
                    self.queue[self.rear+1] = item
                    self.rear = self.rear + 1
        except:
            print("ไม่สามารถป้อนข้อมูลเพิ่มได้")

    def dequeue(self):
        if (self.rear-self.front)+1 < 1:
            print('Queue ว่าง')
        else:
            if self.front == self.rear:
                self.queue.clear()
                self.front = -1
                self.rear = -1
                print('Queue ว่าง')
            else:
                self.queue[self.front] = 0
                self.front = self.front + 1

    def display(self):
        if(self.front == -1):
            print('No element in the Queue')
        else:
            for i in self.queue:
                print(i, end='   ')
            print()
        print('front = ', self.front, ', rear = ', self.rear)

    def end(self):
        if self.front == self.rear:
            print("ไม่สามารถแสดงผลรวมและค่าเฉลี่ยของจำนวนเต็มที่จัดเก็บใน Queue ได้เพราะ Queue ว่าง")
        else:
            sums = 0
            for i in self.queue:
                sums += i
            print("sum = {0}".format(sums))
            print("Count = {0}".format(len(self.queue)))
            average = 0
            for x in self.queue:
                if x != 0:
                    average += 1
                else:
                    continue
            print("Average = {0}".format(sums/average))
        print("\nสิ้นสุดการทำงาน")


q = Queue(int(input("โปรดระบุขนาดของ Queue = ")))
while True:
    print("\nโปรดระบุทางเลือกในการดำเนินการกับ queue")
    print("1. enqueue : รับข้อมูลจำนวนเต็มจัดเก็บใน stack")
    print("2. dequeue : ดึงข้อมูลจาก queue 1 ช่อง")
    print("3. display : แสดงข้อมูลที่จัดเก็บทั้งหมดใน queue ทางจอภาพ\n")
    select = int(input("ทางเลือกในการดำเนินการ = "))
    if select == 1:
        item = int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน queue = "))
        if item == 0:
            print("กรุณาป้อนตัวเลขที่ไม่เท่ากับ 0")
        else:
            q.enqueue(item)
    elif select == 2:
        q.dequeue()
    elif select == 3:
        q.display()
    else:
        q.end()
        break
