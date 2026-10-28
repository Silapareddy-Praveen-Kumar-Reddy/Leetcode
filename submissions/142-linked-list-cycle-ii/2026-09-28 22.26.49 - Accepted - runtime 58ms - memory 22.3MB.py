class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Phase 1: detect
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                # Phase 2: find the start
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        return None   