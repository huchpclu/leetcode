class Solution(object):
    def missingNumber(self, nums):

        n = len(nums)
        max_n = None
        i = 0
        while i < n:
            if nums[i] == n:
                max_n = nums[i]
                nums[i] = None
                i += 1
            elif nums[i] is not None and nums[i] != i:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        if not max_n:
                return n
        return nums.index(None)

class Solution2():
    def missingNumber(self, nums):
        return reduce(operator.xor, nums, \
                      reduce(operator.xor, xrange(len(nums) + 1)))

if __name__ == "__main__":
    s = Solution()
    a = s.missingNumber([0, 1, 3,4])
    print(a)