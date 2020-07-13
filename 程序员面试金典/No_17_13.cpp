class TrieNode{
    public:
    bool isEnd = false;
    TrieNode* Next[26];

    TrieNode(){
        isEnd =false;
        memset(Next, NULL, sizeof(Next));
    }

    ~TrieNode(){
        for(auto p: Next) if(p) delete p;
    }
};


class Trie{
    public:
    TrieNode *root;

    Trie(){
	root = new TrieNode();
        root->isEnd = true;
    }

    void insert(string s){
        auto p = root;
        for(char c: s){
	    int idx = c - 'a';
    	    if(p->Next[idx]) p = p->Next[idx];
	    else{
		p->Next[idx] = new TrieNode();
		p = p->Next[idx];
	    }
	}
        p->isEnd = true;
    }

    ~Trie(){
	for(auto p: root->Next) if(p) delete p;
    }

};

class Solution {
public:
    int respace(vector<string>& dictionary, string sentence) {
        Trie trie;
	for(auto &s: dictionary) trie.insert({s.rbegin(), s.rend()});
        int l = sentence.size();
        vector<int> dp(l + 1, l);
        dp[0] = 0;
	for(int i = 1; i < l + 1; ++i){
            TrieNode *cur_pos = trie.root;
            dp[i] = dp[i - 1] + 1;
            for(int cur_idx = i; cur_idx > 0; --cur_idx){
                int c2idx = sentence[cur_idx - 1] - 'a';
                if(cur_pos->Next[c2idx]){
                    cur_pos = cur_pos->Next[c2idx];
                    if(cur_pos->isEnd) dp[i] = min(dp[i], dp[cur_idx - 1]);
                }
                else break;
            }
        }
	return dp[l];
    }
};