/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr) return {};
        queue<TreeNode*> que;
        que.push(root);
        string ret;
        while (!que.empty()){
            TreeNode * node = que.front();
            que.pop();
            if (node){
                ret += to_string(node->val);
                ret += " ";
                que.push(node->left);
                que.push(node->right);
            }
            else ret += "# ";
        }
        cout << ret << endl;
        return ret;
    }
    queue<string> split(string &s){
        int i = 0;
        queue<string > ret;
        while(i < s.size()){
            string tmp;
            while(i < s.size() && s[i] != ' '){
                tmp += s[i];
                ++i;
            }
            ret.push(tmp);
            ++i;
        }
        return ret;
    }
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.size() == 0) return NULL;
        queue<string> que = split(data);
        // while(!que.empty()) {cout << que.front() << endl; que.pop();}
        TreeNode *root = new TreeNode(stoi(que.front()));
        que.pop();
        queue<TreeNode *> nodes;
        nodes.push(root);
        while(!que.empty() && !nodes.empty()){
            TreeNode *cur = nodes.front();
            nodes.pop();
            // left // right
            string left = que.front();
            que.pop();
            string right = que.front();
            que.pop();
            if (left != "#"){
                cur->left = new TreeNode(stoi(left));
                nodes.push(cur->left);
            }
            if (right != "#"){
                cur->right = new TreeNode(stoi(right));
                nodes.push(cur->right);
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));