# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
      if not head or not head.next:
        return head
        
      odd = head  # Start of odd-indexed nodes
      even = head.next  # Start of even-indexed nodes
      evenHead = even  # Save the start of even-indexed nodes
      while even and even.next:
        odd.next = even.next  # Link odd to the next odd node
        odd = odd.next  # Move odd pointer
        even.next = odd.next  # Link even to the next even node
        even = even.next
      odd.next = evenHead
      return head

l1_list = [1,2,3,4,5]

def list_to_linked_list(l):
  head = ListNode(l[0])
  current  = head
  for item in l[1:]:
    current.next = ListNode(item)
    current = current.next
  return head    


# Convert input lists to linked lists
l1 = list_to_linked_list(l1_list)

# Create Solution object and call the method
solution = Solution()
result_linked_list = solution.oddEvenList(l1)
