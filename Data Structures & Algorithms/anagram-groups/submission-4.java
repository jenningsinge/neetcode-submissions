class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> found = new HashMap<>();
        for (String str : strs) {
            int[] freq = new int[26];
            for (char c : str.toCharArray()) {
                freq[c - 'a'] += 1;
            }
            String key = Arrays.toString(freq);
            List<String> anagrams = found.getOrDefault(key, new ArrayList<>());
            anagrams.add(str);
            found.put(key, anagrams);
        }
        List<List<String>> result = new ArrayList<>();
        for (List<String> value : found.values()) {
            result.add(value);
        }
        return result;
    }
}
