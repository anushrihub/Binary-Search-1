# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/

# This is an interactive problem.
# You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:
# * returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
# * returns 231 - 1 if the i is out of the boundary of the array.
# You are also given an integer target.
# Return the index k of the hidden array where secret[k] == target or return -1 otherwise.
# You must write an algorithm with O(log n) runtime complexity.
 
# Example 1:
# Input: secret = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in secret and its index is 4.
# Example 2:
# Input: secret = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in secret so return -1.
 
# Constraints:
# * 1 <= secret.length <= 104
# * -104 <= secret[i], target <= 104
# * secret is sorted in a strictly increasing order.


# if we use the while low <  high: 
# we have to consider the  below condition
# if reader.get(low) == target:
    # return low
# because the high is always going to be considered but the low can be missed. so add that whereas
# while low <= high:
# this loop searches low == high so no extra check is required


# In this problem we are finding doubling the index till we find the target element within it's range. Once we find the range we apply the binary search. Amd find the location of the target element. Complexity O(log n)
class Solution:
    # def search (self, reader : 'ArrayReader', target :int) -> int:
    def search (self, reader : list, target :int) -> int:
        low = 0
        high = 1

        # reader.get(high) returns the value the index. we are checking that value with the given target
        # while reader.get(high) < target:
        while reader[high] < target:
            # if the target is greater than the high value double the high index until we find the range of the target
            low = high
            high *= 2
        # dont let low cross the high if it then we have searched already and we didnt get required element
        while low <=  high:
            mid_index = (low + high) // 2
            # check the target is equal to the mid_index
            # if reader.get(mid_index) >= target:
            if reader[mid_index] == target:
                return mid_index
            # if the target is less than the mid element change the high
            if reader[mid_index] > target:
                high = mid_index - 1
            # if the target is greater than the mid element change the low
            else:
                low = mid_index +1 
        return -1
    
op = Solution()

print(op.search([-1,0,3,5,9,12],9))
print(op.search([-1,0,3,5,9,12],2))




