class Solution:
    def insertionSortList(self, head):
        if head == None:
            return 

        tempArr = []
        temp = head
        while temp is not None:
            tempArr.append(temp.val)
            temp = temp.next

        i = 0
        tempArr.sort()
        temp = head
        while temp is not None:
            temp.val = tempArr[i]
            i = i + 1
            temp = temp.next

        return head
