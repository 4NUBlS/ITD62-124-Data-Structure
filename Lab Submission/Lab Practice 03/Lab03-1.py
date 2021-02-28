class Node:
    def __init__(self, info=None):
        self.info = info
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AtTheBegining(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode

    def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode

    def SLinkedList_Print(self):
        i = 1
        print("head = {0}".format(self.head.info))
        while self.head is not None:
            print("i = {0} , info = {1}".format(i, self.head.info))
            self.head = self.head.next
            i += 1
        print("tail = {0}".format(self.tail.info))


link_list_a = SLinkedList()
link_list_b = SLinkedList()
print("โปรดป้อนตัวเลขจำนวนเต็มเพื่อสร้าง Singly linkend list A โดยโปรแกรมจะหยุดการวนซ้ำเมื่อตัวเลขจำนวนเต็มที่ผู้ใช้ป้อนมีค่าเป็น 999")
while True:
    data_a = int(input("Data = "))
    if data_a == 999:
        break
    else:
        link_list_a.AtTheEnd(data_a)
print("โปรดป้อนตัวเลขจำนวนเต็มเพื่อสร้าง Singly linkend list B โดยโปรแกรมจะหยุดการวนซ้ำเมื่อตัวเลขจำนวนเต็มที่ผู้ใช้ป้อนมีค่าเป็น 999")
while True:
    data_b = int(input("Data = "))
    if data_b == 999:
        break
    else:
        link_list_b.AtTheEnd(data_b)
while link_list_a.head:
    link_list_b.AtTheBegining(link_list_a.head.info)
    link_list_a.head = link_list_a.head.next
link_list_b.SLinkedList_Print()
