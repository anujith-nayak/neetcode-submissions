class Solution:
    def reverseBits(self, n: int) -> int:
        bine=""
        for i in range(32):
            if n&(1<<i):
                bine+='1'
            else:
                bine+='0'
        res=0
        for i,bit in enumerate(bine[::-1]):
            if bit=="1":
                res |=(1<<i)
        return res     
        