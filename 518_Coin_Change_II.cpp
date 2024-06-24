class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount + 1, 0); //无法用任何数量的硬币凑出来的时候就返回0，因为一开始要凑出0块钱，所以列表长度比amount多1列。
        dp[0] = 1; //凑出0块钱有1种方法。
        // for (int i = 0; i < dp.size(); i++) {
        //     cout<<dp[i];
        //     cout<<"\t";
        // }
        // cout<<"\n";
        for (int i = 1; i <= coins.size(); i++) {
            // 拿出每一种钱试一下
            int v =coins[i - 1];
            for (int j = v; j <= amount; j++) {
                // 每一种目标面值查看是否能加一张这种面值的钱
                dp[j] += dp[j - v]; //从上一种状态过来新增1种取法
            }
        }
        // for (int i = 0; i < dp.size(); i++) {
        //     cout<<dp[i];
        //     cout<<"\t";
        // }
        // cout<<"\n";
        return dp[amount];
    }
};
