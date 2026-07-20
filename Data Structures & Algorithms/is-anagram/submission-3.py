class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        if len(s) != len(t):
            return False
        for cS, cT in zip(s, t):
            mapS[cS] = mapS.get(cS, 0)+1
            mapT[cT] = mapT.get(cT, 0)+1
        return mapS == mapT
        