class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        if target > nums[max]:
            return max+1

        while min<=max:
            mid = int((min + max)/2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                max = mid - 1
            else:
                min = mid + 1
        return min