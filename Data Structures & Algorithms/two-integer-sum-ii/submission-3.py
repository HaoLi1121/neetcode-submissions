class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i,x in enumerate(numbers):
            y = target - x
            if y in res:
                return [res[y] + 1, i + 1]
            res[x] = i
        