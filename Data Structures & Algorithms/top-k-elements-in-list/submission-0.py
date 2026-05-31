class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mk=Counter(nums).most_common(k)
        op=[]
        for num,count in mk:
            op.append(num)
        return op
