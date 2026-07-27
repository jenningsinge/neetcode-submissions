class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for str in strs:
            sortedStr = "".join(sorted(str))
            anagrams = found.get(sortedStr, [])
            if len(anagrams) != 0 and self.isAnagram(str, anagrams[0]):
                anagrams.append(str)
                found[sortedStr] = anagrams
            else:
                found[sortedStr] = [str]
        result = []
        for anagrams in found.values():
            result.append(anagrams)
        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        found = [0] * 26
        for cS, cT in zip(s, t):
            found[ord(cS) - ord('a')] += 1
            found[ord(cT) - ord('a')] -= 1

        for n in found:
            if n != 0:
                return False
        
        return True
        