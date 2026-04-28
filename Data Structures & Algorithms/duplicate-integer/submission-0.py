class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute - TC(O(n^2)), SC(O(1))
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #Better - TC(O(N)), SC(O(1))
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        #Optimal - TC(O(N)), SC(O(N))

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False