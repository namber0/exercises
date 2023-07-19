class Node:
   def __init__(self, data = None):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
        self.head = None

   def atBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

   def removeNode(self, Removekey):
        headVal = self.head

        if (headVal is not None):
            if (headVal.data == Removekey):
                self.head = headVal.next
                headVal = None
                return
         
        while (headVal is not None):
            if headVal.data == Removekey:
                break
         
        prev = headVal
        headVal = headVal.next

        if (headVal == None):
            return

        prev.next = headVal.next
        headVal = None

   def listPrint(self):
        printVal = self.head
        while printVal:
            print(printVal.data),
            printVal = printVal.next

llist = LinkedList()
llist.atBeginning("Mon")
llist.atBeginning("Tue")
llist.atBeginning("Wed")
llist.atBeginning("Thu")
llist.removeNode("Tue")
llist.listPrint()
