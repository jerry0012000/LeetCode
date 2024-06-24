class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // 数组大小为 amount + 1，初始值也为 amount + 1，至多需要用amount枚硬币，因为就算全用面值为1的也要那么多。
        vector<int> dp(amount + 1, amount + 1);
        for (int i = 0; i < dp.size(); i++) {
            cout<<dp[i];
            cout<<"\t";
        }
        cout<<"\n";
        // base case
        dp[0] = 0; // 凑出0元需要0个硬币，不用写if了。
        // 能凑出i块钱吗？
        for (int i = 0; i < dp.size(); i++) {
            // 拿出每一种钱试一下
            for (int coin : coins) {
                // 这个钱面值太大了，比要凑出的i块钱还大，跳过。
                if (i - coin < 0) continue;
                dp[i] = min(dp[i], 1 + dp[i - coin]); //拿了这个钱和不拿这种钱哪种使用的硬币数更少？
            }
            cout<<dp[i];
            cout<<"\t";
        }
        return (dp[amount] == amount + 1) ? -1 : dp[amount];
    }
};
