class Solution(object):
    def twoSum(self, nums, target):
        # Is the result in the first two elements?
        if nums[0] + nums[1] == target:
            return [0, 1]
        else:
            for first in range(len(nums)):
                for second in range(first + 1, len(nums)):
                    if nums[first] + nums[second] == target:
                        return [first, second]


# print(twoSum([3,2,4,7], 6))
# cHECKPOINT 1: Bruteforce without optimization runs in 20 ms

# Optimze with Hash map
# By fixing X to do inputvalue - X
# Find the lacking value Y and then access said value (if it exists) in a hash map
# the idea to accelerate the search is to have the value and make it a hash key to access it
# vALIDATE IF THERE IS SUCH KEY IN THE HASH MAP, AND IF THERE IS, GET ITS INDEX VALUE
# consider the worst posssible case, with larger lists