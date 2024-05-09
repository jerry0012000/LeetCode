class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0;i < nums.length;i++) {
            int remain = target-nums[i];
            for (int j = i+1;j < nums.length;j++) {
                if (nums[j] == remain) {
                    return new int[] {i,j};
                }
            }
        }
        System.out.println("No Solution");
        return new int[] {};
    }
}
