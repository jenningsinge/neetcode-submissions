class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] found = new int[26];
        Arrays.fill(found, 0);
        for (int i = 0; i < s.length(); i ++) {
            int indexS = s.charAt(i) - 'a';
            found[indexS] = found[indexS]+1;
            int indexT = t.charAt(i) - 'a';
            found[indexT] = found[indexT]-1;
        }
        for (int i = 0; i < found.length; i++) {
            if (found[i] != 0) return false;
        }
        return true;
    }
}
