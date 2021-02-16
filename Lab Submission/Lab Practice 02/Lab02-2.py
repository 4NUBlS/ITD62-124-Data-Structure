class CircularQueue:

    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear+1)% self.n == self.front:
            print('Circular queue เต็ม')
        else:     
            if self.front == -1:               
                print('Item : ', item)
                self.rear = self.rear + 1
                self.queue[self.rear] = item
                self.front = 0
            else:              
                print('Item : ', item)
                self.rear = (self.rear + 1)% self.n
                self.queue[self.rear] = item

    def dequeue(self):
        if (self.front == -1):
            print('ไม่สามารถดึงข้อมูลจาก Circular queue ได้เพราะ Circular queue ว่าง')
        else:
            if self.front == self.rear:
                self.queue[self.front]= '-'                
                self.front = -1
                self.rear = -1 
            else: 
                self.queue[self.front]= '-'
                self.front = (self.front+1) % self.n  

    def display(self):
        if(self.front == -1):
            print('No element in the circular queue')
        else:         
            for i in range(0, self.n):
                if self.queue[i] == None:
                    print(' - ', end = " ")
                else:
                    print(self.queue[i], end = " ")
            print( ) 

    def select(self):
        if self.queue[self.front] == None or self.queue[self.front] == "-":
            print("no element in the circular queue")
        else:
            print("ชื่อลูกค้ารายต่อไป = {0}".format(self.queue[self.front]))   


q = CircularQueue(int(input("โปรดระบุขนาดของ Circular Queue = ")))
while True:
    print("\nโปรดระบุทางเลือกในการดำเนินการกับ Circular queue")
    print("1. รับข้อมูลชื่อลูกค้าจัดเก็บใน Circular queue")
    print("2. ลบข้อมูลชื่อลูกค้าจาก Circular queue 1 ราย")
    print("3. แสดงข้อมูลชื่อลูกค้าที่จัดเก็บทั้งหมดใน Circular queue ทางจอภาพ")
    print("4. แสดงข้อมูลชื่อลูกค้ารายต่อไปทางจอภาพ\n")
    select = int(input("ทางเลือกในการดำเนินการ = "))
    if select == 1:
        q.enqueue(input("ข้อมูลที่ต้องการจัดเก็บใน Circular queue = "))
    elif select == 2:
        q.dequeue()
    elif select == 3:
        q.display()
    elif select == 4:
        q.select()
    else:
        print("สิ้นสุดการทำงาน")
        break