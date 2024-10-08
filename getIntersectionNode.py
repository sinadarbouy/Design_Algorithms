class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      if not headA or not headB:
        return None
      pA,pB = headA,headB
      find = {}
      while pA or pB:
        if pA and pA in find:
          return pA
        else:
          find[pA] = 1
        if pB and pB in find:
          return pB
        else:
          find[pB] = 1
        
        if pA:
          pA = pA.next
        if pB:
          pB = pB.next
      return None
