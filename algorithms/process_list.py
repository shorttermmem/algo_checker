from typing import List

def merge_sort_ver1():
    """ merge two incrementally sorted arrays A, B """

    pass

def findKthLargest(nums: List[int], k: int) -> int:
    def qselect(nums: List[int], l: int, r: int, k: int) -> None:
        p = partition(nums, l, r)

        if p < k:
            return qselect(nums, p + 1, r, k)
        if p > k:
            return qselect(nums, l, p - 1, k)

        return nums[p]

    def partition(nums: List[int], l: int, r: int) -> int:
        pivot, p = nums[r], r

        i = l
        while i < p:
            if nums[i] > pivot:
                nums[i], nums[p-1] = nums[p-1], nums[i]
                nums[p], nums[p-1] = nums[p-1], nums[p]
                i -= 1
                p -= 1
            i+=1
        return p

    return qselect(nums, 0, len(nums) - 1, len(nums) - k)


def findPermutations(nums: List[int], k: int) -> List[List[int]]:
    # P(n,k)
    res = []
    def backtracking(temp: List[int]):
        if len(temp) == k:
            res.append(temp.copy())
            return 
        
        for n in nums:
            if n not in temp:
                temp.append(n)
                backtracking(temp)
                temp.pop()
    backtracking([])
    return res

def findCombinations(nums: List[int], k: int):
    # C(n,k)
    res = []
    def backtracking(temp: List[int], start: int):
        if len(temp) == k:
            res.append(temp.copy())
            return

        for i in range(start, len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
                backtracking(temp, i+1)
                temp.pop()
    backtracking([])
    return res

def findPowerSets(nums: List[int]): 
    # C(n, 0) + C(n, 1) + ... + C(n,k)
    res = []
    for i in range(len(nums)):
        res.extend(findCombinations(nums, i))
    return res
