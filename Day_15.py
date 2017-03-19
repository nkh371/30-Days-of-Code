    def insert(self,head,data): 
        if head == None:
            new_node = Node(data)
            return new_node
        else:
            trav = head
            while trav.next != None:
                trav = trav.next
            new_node = Node(data)
            trav.next = new_node
            return head
        
