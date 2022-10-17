# Grind 75
# Array
# 2022-9-18


# 1 Two sum
# O(N^2) Brute Force
def twoSum(nums:list[int], target:int)-> list[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []


# O(N) Hash Table
# def twoSum(nums:list[int], target:int)-> list[int]:
# 	hashtable = dict()
# 	for i,num in enumerate(nums):
# 		if target - num in hashtable:
# 			return [hashtable[target - num],i]
# 		hashtable[nums[i]] = i
# 	return []


# Test case
# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,4],6))
# print(twoSum([3,3],6))
# print(twoSum([3,3],8))


# 2 Valid Parentheses
# O(N)
def isValid(s: str) -> bool:
	if len(s) % 2 == 1:
		return False

	pairs = {
		")": "(",
		"]": "[",
		"}": "{",
		}
	stack = list()
	for ch in s:
		if ch in pairs:
			if not stack or stack[-1] != pairs[ch]:
				return False
			stack.pop()
		else:
			stack.append(ch)
	return not stack

# Test case
# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("(]"))
# print(isValid("{()"))

# 3 Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
		
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
	if l1 is None:
		return l2
	elif l2 is None:
		return l1
	elif l1.val < l2.val:
		l1.next = mergeTwoLists(l1.next, l2)
		return l1
	else:
		l2.next = mergeTwoLists(l1,l2.next)
		return l2

# Test Case
l1 = [1,2,4]
l2 = [1,3,4]
L1 = ListNode(l1,next=l1)
L2 = ListNode(l2,next=l2)
print(L2.val)
print(mergeTwoLists(L1,L2).val)