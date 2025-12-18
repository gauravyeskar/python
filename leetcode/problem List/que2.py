'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Example:Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Logic: 342 + 465 = 807  Output: 7 -> 0 -> 8  '''
def addtwonumbers(self,l1,l2):
        dummy = ListNode(0) # The "Engine"
        curr = dummy        # Our "current" position
        carry = 0
        
        # While there are still numbers to add OR a carry to process
        while l1 or l2 or carry:
            # 1. Get the digits (use 0 if the list ended early)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 2. Add them up
            column_sum = val1 + val2 + carry
            carry = column_sum // 10  # This gets the tens digit (the carry)
            digit = column_sum % 10   # This gets the ones digit (the result)
            
            # 3. Create the new node and move forward
            curr.next = ListNode(digit)
            curr = curr.next
            
            # 4. Move to the next "person" in the scavenger hunt
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next # Return everything AFTER the engine