class Solution(object):
    def middleNode(self, head):
        
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow