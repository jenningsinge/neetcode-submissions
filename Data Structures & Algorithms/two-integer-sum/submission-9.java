class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> found = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer complement = target - nums[i];
            if (found.get(complement) != null) {
                return new int[]{found.get(complement), i};
            }
            found.put(nums[i], i);
        }
        return new int[]{};
    }
}
