#include <math.h>
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, n+1);// 从0到n的每一个数至少要几个平方数表示？
        // 0只能用0个平方数表示，1只能用1的平方表示。
        dp[0] = 0;
        dp[1] = 1;
        int l = 0; //需要用到的平方数的数组长度
        for (int i=1;i<=n;i++) {
            if (pow(i,2) > n) {
                break;
            }
            else {
                l++;
            }
        }
        vector<int> sqrtNum(l);
        for (int i=1;i<l+1;i++) {
            sqrtNum[i-1] = pow(i,2);
            // cout<<sqrtNum[i-1];
            // cout<<"\t";
        }
        // cout<<"\n";
        // cout<<l;
        for (int i=0;i<l;i++) {//物品，有哪些平方数
            for (int j=1;j<n+1;j++) {//背包，整数1到n分别至少需要多少个平方数相加？
                if (j-sqrtNum[i] < 0) continue;//一定不要把等号取进去了，不然dp[4] = dp[0] + 1无法识别到，就变成dp[3] + 1结果为4，以此类推最后结果会出问题。
                dp[j] = min(dp[j], dp[j-sqrtNum[i]]+1);
            }
        }
        // for (int i=0;i<n+1;i++) {
        //     cout<<dp[i];
        //     cout<<"\t";
        // }
        // cout<<"\n";
        return dp[n];
    }
};
