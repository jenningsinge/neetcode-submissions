class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            Character charS = s.charAt(i);
            mapS.put(
                charS,
                mapS.getOrDefault(charS, 0) + 1
            );
            Character charT = t.charAt(i);
            mapT.put(
                charT,
                mapT.getOrDefault(charT, 0) + 1
            );
        }
        return mapS.equals(mapT);
    }
}
