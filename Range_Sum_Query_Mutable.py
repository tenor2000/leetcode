class BIT:
    def __init__(self, n):
        self.sums = [0] * (n+1)
    
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res
    
class NumArray:

    def __init__(self, nums):
        self.bit = BIT(len(nums))
        for i, num in enumerate(nums):
            self.bit.update(i+1, num)
        self.nums = [0] + nums
            
    def update(self, index, val) -> None:
        self.bit.update(index+1, val - self.nums[index+1])
        self.nums[index+1] = val

    def sumRange(self, left, right) -> int:
        return self.bit.query(right+1) - self.bit.query(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)