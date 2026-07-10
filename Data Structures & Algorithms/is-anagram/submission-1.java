class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<String, Integer> mapS = new HashMap<String, Integer>();
        Map<String, Integer> mapT = new HashMap<String, Integer>();
        for (int i = 0; i < s.length(); i++) {
            String charS = String.valueOf(s.charAt(i));
            mapS.put(
                charS,
                mapS.getOrDefault(charS, 0) + 1
            );
            String charT = String.valueOf(t.charAt(i));
            mapT.put(
                charT,
                mapT.getOrDefault(charT, 0) + 1
            );
        }
        if (mapS.size() != mapT.size()) return false;
        for (var entry : mapS.entrySet()) {
            Integer valueT = mapT.get(entry.getKey());
            if (valueT == null) return false;
            if (!valueT.equals(entry.getValue())) {
                return false;
            }
        }
        return true;
    }
}
