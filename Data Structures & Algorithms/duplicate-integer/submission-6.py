class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for value in seen.values():
            if value > 1:
                return True

        return False