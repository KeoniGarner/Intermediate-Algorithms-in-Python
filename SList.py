class SLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def PrintAllVals(self):
        if not self.head:
            print ("No Values")
            return self
        
        runner = self.head
        while (runner):
            print (runner.value)
            runner = runner.next
        
        return self
    
    def SetTail(self):
        runner = self.head
        while (runner.next):
            runner = runner.next
        self.tail = runner
        return self

    def AddBack(self, value):
        if not self.head:
            self.head = SLNode(value)
            self.tail = self.head
            return self
        self.tail.next = SLNode(value)
        self.tail = self.tail.next
        return self

    def AddFront(self, value):
        if not self.head:
            self.head = SLNode(value)
            self.tail = self.head
            return self
        newNode = SLNode(value)
        newNode.next = self.head
        self.head = newNode
        return self

    def InsertBefore(self, before, value):
        if not self.head:
            self.head = SLNode(value)
            self.tail = self.head
            return self
        newNode = SLNode(value)
        runner = self.head
        while runner:
            if runner.next.value == before:
                newNode.next = runner.next
                runner.next = newNode
                break
            runner = runner.next
        return self
    
    def InsertAfter(self, after, value):
        if not self.head:
            self.head = SLNode(value)
            self.tail = self.head
            return self
        newNode = SLNode(value)
        runner = self.head
        while runner:
            runner = runner.next
            if runner.value == after:
                newNode.next = runner.next
                runner.next = newNode
                break
        return self

    def RemoveNode(self,  value):
        if not self.head:
            return self
        runner = self.head
        while runner.next:
            if runner.next.value == value:
                tempNode = runner.next
                runner.next = runner.next.next
                tempNode.next = None
                tempNode = None
            runner = runner.next
        return self

    def Reverse(self):
        if not self.head:
            return self
        prev = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev
        return self

list = SList()
list.head = SLNode('Val1')
list.head.next = SLNode('Val2')
list.head.next.next = SLNode('Val3')
list.head.next.next.next = SLNode('Val4')

list.SetTail().AddBack("Val5").AddFront("Val0").InsertBefore("Val3","INSERT").InsertAfter("INSERT","AFTER").RemoveNode("INSERT").RemoveNode("AFTER").Reverse().SetTail().PrintAllVals()