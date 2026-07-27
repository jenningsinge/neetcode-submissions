class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        sortedFreqs = sorted(freqs.values())
        topKFreqs = sortedFreqs[-k:]
        print(topKFreqs)
        result = []
        for num, freq in freqs.items():
            for topKFreq in topKFreqs:
                if freq == topKFreq:
                    result.append(num)
                    break
        return result

        