class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        complement = 0 

        for i in range(len(nums)): 
            complement = target - nums[i]
            
            #if target in the seen, return the index 
            if complement in seen: 
                return [seen[complement], i]
            else: 
                seen[nums[i]] = i

        return [0,0]


        