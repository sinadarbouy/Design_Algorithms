# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
      head_odd = ListNode()
      odd= head_odd
      head_even = ListNode()
      even = head_even
      index = 0
      while head:
        if index%2 == 0:
          even.next=ListNode(head.val)
          even = even.next
        else:
          odd.next=ListNode(head.val)
          odd = odd.next

        index +=1
        head = head.next
      even.next = head_odd.next
      return head_even.next



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
