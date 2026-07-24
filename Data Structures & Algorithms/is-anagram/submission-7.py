class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        found = [0]*26
        for cS, cT in zip(s, t):
            indexS = ord(cS) - ord('a')
            found[indexS] = found[indexS]+1
            indexT = ord(cT) - ord('a')
            found[indexT] = found[indexT]-1
        for n in found:
            if n != 0:
                return False
        return True
        


        
        