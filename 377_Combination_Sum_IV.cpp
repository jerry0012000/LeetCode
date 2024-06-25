class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        //排列问题，背包在外层（先背包后物品）。
        vector<unsigned long long> dp(target+1, 0);
        dp[0] = 1;
        for (int i=1;i<target+1;i++) {
            for (int j=0;j<nums.size();j++) {
                if (i-nums[j]>=0) {
                    dp[i] += dp[i-nums[j]];
                }
            }
        }
        return dp[target];
    }
};
