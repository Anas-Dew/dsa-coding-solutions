def findMid(head):
    # Code here
    # return the value stored in the middle node
    # we can have 2 element fast and slow and...
    # we can increase fast by 2 and slow by 1
    # so when fast reaches end slow will be at middle
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.data


# test here
link = 'https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1#'

# explanation
# Sure….here we go→

# First lets forget about linked list and just focus on maths, then we will apply it to our linked list:

# For EVEN numbers: → Suppose you have 10 numbers 1 to 10, first element or Head is “1” and last element is “10”. Now if you think about 2 “Kangaroos” who have named “fast” and “slow” (LOL just think). “fast” jumps 2 steps and slow jumps 1. Now what will happen is fast will jump from 1 to 3 to 5 to 7 to 9… now see after 9 if “fast” jumps it will reach to “None” b'coz after 9 is 10 and after 10 is None. which means fast = None. Here “fast”  took 5 jumps. At this point “slow” reached only till 1 to 2 to 3 to 4 to 5 to 6. and slow.data=6 is your ANSWER.


# For ODD numbers: → Suppose you have 11 numbers 1 to 11. now “fast” will jump 1 to 3 to 5 to 7 to 9 to 11. Notice One thing… here fast is at 11 (the last element) which also means fast.next = None …. and at this time slow reached 1 to 2 to 3 to 4 to 5 to 6. which is ANSWER.


# Thats why NOW COMING BACK TO CODE. we initialized both fast and slow at start of linked list, ran a simple while loop until there is value in both fast and fast.next, incremented fast by 2, slow by 1 and returned the slow.data.


# HOPE THIS HELPS…
# Regards,
# CriticAugen
