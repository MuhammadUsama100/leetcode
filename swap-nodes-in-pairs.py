class Solution(object):

    def swapNode(self, pre_node , node):
        next_node = node.next
        if pre_node == None:
            node.next = next_node.next
            next_node.next = node
        else:
            pre_node.next = next_node
            node.next = next_node.next
            next_node.next = node
        return next_node
            
    def swapPairs(self, head):
        pointer =  head
        previous_pointer = None
        if pointer == None or pointer.next == None : return head

        head = self.swapNode(previous_pointer,pointer )
        previous_pointer =  head.next
        pointer = previous_pointer.next

        while pointer != None and pointer.next != None:
            pointer = self.swapNode(previous_pointer,pointer )
            previous_pointer = pointer.next
            pointer = previous_pointer.next
        return head
            
        
