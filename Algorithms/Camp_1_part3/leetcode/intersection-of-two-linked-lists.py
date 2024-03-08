# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # q1=headA
        # q2=headB
        # while q1!=q2:
        #     q1=q1.next if q1 else headA
        #     q2=q2.next if q2 else headB
        # return q1
        hashMap = defaultdict(int)
        while headA:
            hashMap[headA] = 1
            headA = headA.next
        
        while headB:
            if headB in hashMap:
                return headB
            headB = headB.next
        
        return None
        
        

        