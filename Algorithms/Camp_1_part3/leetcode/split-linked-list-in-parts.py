# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count,dummy=0,head
        while dummy:
            dummy=dummy.next
            count+=1
        split_len=count//k
        remain=count%k
        ans=[]
        dummy=head
        for i in range(k):
            ans.append(dummy)
            for x in range(split_len-1 + (1 if remain else 0)):
                if not dummy:
                    break
                dummy=dummy.next
            remain-= (1 if remain else 0)
            if dummy:
                dummy.next,dummy=None,dummy.next
        return ans
