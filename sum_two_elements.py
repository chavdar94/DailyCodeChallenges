'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


nums = [10, 15, 3, 7]
k = 17
flag = False

map = {
    'current_num': nums[0]
}

for i in range(1, len(nums)):
    if k - nums[i] in map:
        flag = True
        break
    else:
        map['current_num'] = nums[i]

print(flag)
