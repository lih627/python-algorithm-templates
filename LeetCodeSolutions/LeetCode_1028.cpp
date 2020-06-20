/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 typedef pair<int, int> pii;
class Solution {
public:
    // pairt<val, depth>
    vector<pii> split(string S){
        int i = 0;
        string tmp;
        vector<pii> ret;
        while(i < S.size() && S[i] != '-') tmp += S[i++];
        ret.push_back(make_pair(stoi(tmp), 0));
        while(i < S.size()){
            int depth = 0;
            while(i<S.size() && S[i] == '-'){++depth; ++i;}
            tmp = "";
            while(i<S.size() && S[i] != '-'){tmp += S[i++];}
            ret.push_back(make_pair(stoi(tmp), depth));
        }
        return ret;
    }

    TreeNode* recoverFromPreorder(string S){
        if (S.size() == 0) return NULL;
        auto elems = split(S);
        TreeNode dummy(-1);
        stack<pair<TreeNode*, int> > st;
        for(auto pir: elems){
            if(st.empty()){
                dummy.left = new TreeNode(pir.first);
                st.push(make_pair(dummy.left, 0));
            }
            else{
                while(pir.second - st.top().second != 1){
                    st.pop();
                }
                if(st.top().first->left){
                    st.top().first->right = new TreeNode(pir.first);
                    st.push(make_pair(st.top().first->right, pir.second));
                }
                else{
                    st.top().first->left = new TreeNode(pir.first);
                    st.push(make_pair(st.top().first->left, pir.second));
                }
            }
        }
        return dummy.left;
    }
};