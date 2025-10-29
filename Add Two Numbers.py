def addTwoNumbers(l1, l2):
    head = cur = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        s = v1 + v2 + carry
        carry = s // 10
        
        cur.next = ListNode(s % 10)
        cur = cur.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return head.next
