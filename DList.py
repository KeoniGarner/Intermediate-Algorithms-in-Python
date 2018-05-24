class DLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def AddBack(self, value):
        if not self.head:
            self.head = DLNode(value)
            self.tail = self.head
            return self
        
        self.tail.next = DLNode(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

        return self

    def RemoveNode(self, value):
        if not self.head:
            return self
        runner = self.head
        while runner.next:
            if runner.next.value == value:
                tempNode = runner.next
                runner.next = runner.next.next
                runner.next.prev = tempNode.prev
                tempNode.next = None
                tempNode.prev = None
            runner = runner.next
        return self

    def InsertBefore(self, before, value):
        if not self.head:
            self.head = DLNode(value)
            self.tail = self.head
            return self
        newNode = DLNode(value)
        runner = self.head
        while runner:
            if runner.next.value == before:
                newNode.next = runner.next
                newNode.prev = runner
                newNode.next.prev = newNode
                runner.next = newNode
                break
            runner = runner.next
        return self

    def InsertAfter(self, after, value):
        if not self.head:
            self.head = DLNode(value)
            self.tail = self.head
            return self
        newNode = DLNode(value)
        runner = self.head
        while runner:
            if runner.value == after:
                newNode.next = runner.next
                newNode.prev = runner
                newNode.next.prev = newNode
                runner.next = newNode
                break
            runner = runner.next
        return self
    

list = DList()
list.AddBack("Val0").AddBack("Val1").AddBack("Val2").AddBack("Val3").RemoveNode("Val2").InsertAfter("Val1","Val2").InsertBefore("Val2","INSERT BEFORE")
print(list.head.next.next.value)