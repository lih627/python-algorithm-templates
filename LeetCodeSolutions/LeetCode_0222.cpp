
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        TreeNode *tmp = root;
        int depth = 0;
        while(tmp != nullptr){
            tmp = tmp->right;
            ++depth;
        }
        if (depth == 0) return 0;
        int prev = pow(2, depth) - 1;
        int l = 0, r = pow(2, depth) - 1, ret = -1;
        while (l <= r){
            int mid = l + (r - l) / 2;
            if (valid(root, depth, mid)){
                ret = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }
        // cout << ret << ' ' << depth<< endl;
        return prev + ret + 1;
    }

    bool valid(TreeNode *root, int &depth, int &cur){
        int tmp = 1 << (depth - 1);
        TreeNode *p = root;
        while(tmp){
            if(cur & tmp){
                p = p->right;
            }
            else{
                p = p->left;
            }
            tmp >>= 1;
            if (p == nullptr) return false;
        }
        return p != nullptr;
    }
};