class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0;i < nums.length;i++) {
            if (nums[i] == target) {
                //System.out.println("["+ i + "," + i + "]");
                for (int k = 0;k < nums.length;k++) {
                    if (nums[i] == nums[k] && i != k) {
                        return new int[] {i,k};
                    }
                }
            }
            else {
                int remain = target-nums[i];
                for (int j = 0;j < nums.length;j++) {
                    if (nums[j] == remain && i != j) {
                        //System.out.println("["+ i + "," + j + "]");
                        return new int[] {i,j};
                    }
                }
            }
            //else {
                //
            //}
        }
        System.out.println("No Solution");
        return new int[] {};
    }
}
