/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
int maxDepth = 0;
private:
    int dps(TreeNode* root) {//深度优先搜索
        if (!root) {
            return 0;
        }
        int L,R;
        L = dps(root->left);
        R = dps(root->right);
        if (L+R > maxDepth) {//最长路径不一定经过根节点
            maxDepth = L+R;
        }
        return max(L,R)+1;
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        dps(root);
        return maxDepth;
    } 
};
