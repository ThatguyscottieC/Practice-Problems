class Solution(object):
    def containsDuplicate(self, nums):
        i = []
        for x in nums:
            if x in i:
                return True
            i.append(x)
        return False


print(Solution)
