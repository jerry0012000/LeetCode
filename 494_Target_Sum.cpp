class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        int left = 0,right = 0;
        for(int i=0;i<nums.size();i++) {    
            sum += nums[i];
        }
        if (abs(target) > sum) return 0; // 全加或减到一起也不够，此时没有方案
        if ((sum + target) % 2 == 1) return 0; // 找不出left - right = target，此时没有方案
        left = (sum + target) / 2;
        vector<int> dp(left+1, 0);
        //排列，背包为外层（先背包后物品）
        dp[0] = 1;
        for (int i=0;i<nums.size();i++) {
            for(int j=left;j>=nums[i];j--) { // 遍历背包
                dp[j] += dp[j - nums[i]]; 
            }
        }
        return dp[left];
    }
};
