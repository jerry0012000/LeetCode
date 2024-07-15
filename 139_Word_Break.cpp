class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        // cout << s.length() << endl;
        int dpLength = s.length() + 1;
        // cout << dpLength << endl;
        vector<bool> dp(n+1, false);
        dp[0] = true;
        for (int i=0;i<n+1;i++) { //背包
            for (string word: wordDict) { //物品
                // cout << word << endl;
                if (i >= word.length()) {
                    dp[i] = dp[i] or dp[i - word.length()] and word.compare(s.substr(i - word.length(), word.length())) == 0; //字符串匹配
                } 
            }
        }
        // cout << dp[0] << endl;
        return dp[n];
    }
};
