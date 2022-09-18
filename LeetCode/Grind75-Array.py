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