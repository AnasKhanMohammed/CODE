class Solution:
    def mergeKLists(self, lists):
        nums = []

        for head in lists:
            while head:
                nums.append(head.val)
                head = head.next

        nums.sort()

        dummy = ListNode(0)
        curr = dummy

        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next