# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      head = ListNode()
      dummy = head
      extra_val = 0
      while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        sum = val1 + val2+extra_val
        actual = sum % 10
        extra_val = int(sum / 10)
        dummy.next = ListNode(actual)
        dummy = dummy.next
        
        if l1:
          l1 = l1.next
        if l2:
          l2 = l2.next
      if extra_val > 0:
        dummy.next = ListNode(extra_val)
      return head.next
          
          

# Input lists
# l1_list = [2, 4, 3]
# l2_list = [5, 6, 4]

l1_list = [9,9,9,9,9,9,9]
l2_list = [9,9,9,9]

def list_to_linked_list(l):
  head = ListNode(l[0])
  current  = head
  for item in l[1:]:
    current.next = ListNode(item)
    current = current.next
  return head    
    


# Convert input lists to linked lists
l1 = list_to_linked_list(l1_list)
l2 = list_to_linked_list(l2_list)

# Create Solution object and call the method
solution = Solution()
result_linked_list = solution.addTwoNumbers(l1, l2)
