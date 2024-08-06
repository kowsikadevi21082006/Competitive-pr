class Solution:
    def reverseList(self, head):
        temp = head
        prev = None
        value = None
        while temp != None:
            value = temp.next
            temp.next = prev
            prev = temp
            temp = value
        return prev