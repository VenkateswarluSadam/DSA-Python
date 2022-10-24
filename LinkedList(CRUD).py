class Node :
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        pass
    def createLL(self,elements):
        self.elements = elements
        self.linkedList = Node(elements[0])
        self.ll = self.linkedList
        for i in range(1,len(self.elements)):
            self.ll.next = Node(self.elements[i])
            self.ll = self.ll.next
        return self.linkedList
        
    
    def insertAtBegining(self,element,head):
        newNode = Node(element)
        current = head
        newNode.next = current
        current = newNode
        return current
    
    def insertAtEnding(self,element,head):
        newNode = Node(element)
        current = head
        while current.next is not None:
            current = current.next
        current.next = newNode
        return head
    
    def insertAtMiddleBeforeE(self,pos,element,head):
        current = head
        while current.next.data != pos:
            current = current.next
        newNode = Node(element)
        newNode.next = current.next
        current.next = newNode
        return head
    
    def insertAtMiddleAfterE(self,pos,element,head):
        current = head
        while current.data != pos:
            current = current.next
        newNode = Node(element)
        newNode.next = current.next
        current.next = newNode
        return head
    
    def printLL(self,head):
        node = head
        while node is not None:
            print(node.data)
            node = node.next
        print()
        
def main():
    elements = list(map(int,input().strip().split()))
    obj = LinkedList()
    linkedList = obj.createLL(elements)
    obj.printLL(linkedList)
    linkedList = obj.insertAtBegining(6,linkedList)
    obj.printLL(linkedList)
    linkedList = obj.insertAtEnding(7,linkedList)
    obj.printLL(linkedList)
    linkedList = obj.insertAtMiddleBeforeE(3,8,linkedList)
    obj.printLL(linkedList)
    linkedList = obj.insertAtMiddleAfterE(4,9,linkedList)
    obj.printLL(linkedList)


if __name__=="__main__":
    main()
