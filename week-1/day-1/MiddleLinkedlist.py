class Solution:
    def middleNode(self, head):
        count = 0
        dummyHead = head
        while dummyHead is not None:
            count += 1
            dummyHead = dummyHead.next
        for num in range(count // 2) :
            head = head.next
        return head
    







