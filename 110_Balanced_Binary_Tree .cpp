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
private:
    int getHeight(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        int leftHeight = getHeight(node->left);
        if (leftHeight == -1) {
            return -1;
        }
        int rightHeight = getHeight(node->right);
        if (rightHeight == -1) {
            return -1;
        }
        int result;
        if (abs(leftHeight - rightHeight)>1) {
            return -1;
        }
        else {
            result = 1+max(rightHeight,leftHeight);//节点的高度是左右子树里面高的+1
        }
        return result;
    }
public:
    bool isBalanced(TreeNode* root) {
        if (getHeight(root) == -1) {
            return false;
        }
        return true; 
    }
};