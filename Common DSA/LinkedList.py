# https://www.youtube.com/watch?v=FWQNMFHKz7A&list=PLPbgcxheSpE3NlJ30EDpxNYU6P2Jylns8&index=4

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        # iter = self.head # works the same way
        list_style = ''
        
        while self.head:
            suffix = ''
            if self.head.next:
                suffix = '---->'
            list_style += str(self.head.data) + suffix
            # print(self.head.data)
            # iter = iter.next
            self.head = self.head.next
        print(list_style)
        
    def length(self):
        length = 0
        iter = self.head
        while iter:
            length += 1
            iter = iter.next
        return length
        
    def insert_at_beginning(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
            
        iter = self.head
        
        while iter.next:
            iter = iter.next
        iter.next = Node(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.insert_at_beginning(data)
            return
            
        index_run = 0
        iter = self.head
        while iter:
            if index_run == index-1:
                node = Node(data, iter.next)
                iter.next = node
                break
                
            iter = iter.next
            index_run += 1
        
        iter = Node(data,iter.next)

    def delete(self, index):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.head = self.head.next
            return

        iter = self.head
        index_run = 0
        while iter:
            if index_run == index-1 :
                iter.next = iter.next.next
            iter = iter.next
            index_run += 1

    def fetch(self, index):
        iter = self.head
        index_run = 0

        while iter:
            if index_run == index:
                return iter.data
            index_run += 1
            iter = iter.next
        return None

    def remove(self, data):
        iter = self.head
        index_run = 0

        while iter:
            if self.fetch(index_run+1) == data:
                iter.next = iter.next.next
                return
            
            iter = iter.next
            index_run += 1
        return f'{data} not in linkedlist.'

    def reverse(self):
        pass
            
if __name__ == "__main__" :
    l = LinkedList()
    l.insert_at_beginning(12)
    l.insert_at_end(1)
    l.insert_at_end(2)
    l.insert_at_end(3)
    l.insert_at_beginning(11)
    l.insert_at(3, 'new item')
    # l.delete(2) # delete by index
    # print(l.fetch(5))
    l.remove(2) # delete by value
    l.reverse()
    l.show_list()
    
    # print(l.length())