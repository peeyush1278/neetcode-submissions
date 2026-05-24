class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {item: nums.count(item) for item in set(nums)}
        rtn=[]
        for i in range(k):
            max_key = max(frequencies, key=frequencies.get)
            del frequencies[max_key]
            rtn.append(max_key)
        return rtn
