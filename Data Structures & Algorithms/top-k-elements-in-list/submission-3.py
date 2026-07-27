class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        arr = []
        for num, freq in freqs.items():
            arr.append([freq, num])
        arr.sort()
        topKFreqs = arr[-k:]
        result = []
        for freqPair in topKFreqs:
            result.append(freqPair[1])
        return result

        