"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

 

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_table = dict()
        for i in range(len(nums)):
            if (nums[i] in hash_table) and ((i - hash_table[nums[i]])<=k):
                return True
            else:
                hash_table[nums[i]] = i
        return False


def main():

    line = input("Input array here: ")

    k = int(input("Input K: "))

    nums = [int(i) for i in line.split(',')]

    result = Solution().containsNearbyDuplicate(nums, k)

    print("Whether array contain eligible pair", result)