class Solution:
    def mergeKLists(self, lists):
        l=[]
        if lists==[] or lists==[[]]:
            return None
        else:
            for i in lists:
                h=i
                while h:
                    l.append(h.val)
                    h=h.next
            l.sort()
            head=None
            for i in l:
                if head is None:
                    head=list(i)
                    t=head
                else:
                    a=list(i)
                    t.next=a
                    t=t.next
        return head