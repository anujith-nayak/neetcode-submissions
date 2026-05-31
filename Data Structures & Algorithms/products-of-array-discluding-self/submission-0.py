class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        frwd=[]
        prd=1
        for i in nums:
            prd=prd*i
            frwd.append(prd)

        bkwd=[]
        prd=1
        for i in nums[::-1]:
            prd=prd*i
            bkwd.append(prd)
        bkwd=bkwd[::-1]

        op=[bkwd[1]]
        for i in range(1,len(nums)-1):
            op.append(frwd[i-1]*bkwd[i+1])
        op.append(frwd[-2])
        return op
      