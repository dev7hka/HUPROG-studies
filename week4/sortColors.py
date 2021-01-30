class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        ---------------------------------------------------------------
        #The solution is similar to 3-way quick sort

        firstPivot: pivot between "0" and "1"
        secondPivot: pivot between "1" and "2"
        start traversing until pivots cross or i cross with secondPivot
           if "0" is encountered, change it with firstPivot, increase firstPivot
           if "2" is encountered, change it with secondPivot, decrease secondPivot
           otherwise do nothing
        """
        firstPivot, secondPivot = 0, len(nums) - 1
        i = 0
        while i < len(nums) and firstPivot <= secondPivot and i <= secondPivot:
            if nums[i] == 0:
                nums[i], nums[firstPivot] = nums[firstPivot], nums[i]
                firstPivot += 1
                if i <= firstPivot:
                    i += 1
            elif nums[i] == 2:
                nums[i], nums[secondPivot] = nums[secondPivot], nums[i]
                secondPivot -= 1
            else:
                i += 1