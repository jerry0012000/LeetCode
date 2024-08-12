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
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // cout << p->val << endl;
        // cout << q->val << endl;
        if (p == nullptr && q == nullptr) {//处理叶子节点
            return true;
        }
        if (p == nullptr || q == nullptr) {//一边是空则不相同
            return false;
        }
        if (p->val == q->val) {
                return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);//值相同，继续看
        }
        return false;//值也不相同，树不一样
    }
};
