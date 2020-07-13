/*
 * @lc app=leetcode.cn id=211 lang=cpp
 *
 * [211] 添加与搜索单词 - 数据结构设计
 */

// @lc code=start
class TrieNode{
    public:
    TrieNode* Next[26];
    bool isEnd;
    TrieNode(){
        memset(Next, NULL, sizeof(Next));
        isEnd = false;
    }

    ~TrieNode(){
        for(int i =0; i < 26; ++i)
            if(Next[i]) delete Next[i];
    }
};

class WordDictionary {
    TrieNode *root;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new TrieNode();
        // add null string
        root->isEnd = true;
    }

    /** Adds a word into the data structure. */
    void addWord(string word) {
        TrieNode *cur = root;
        for(char &c: word){
            int idx = c - 'a';
            if (!cur->Next[idx]){
                cur->Next[idx] = new TrieNode();
            }
            cur = cur->Next[idx];
        }
        cur->isEnd = true;
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return dfs(0, word, root);

    }

    bool dfs(int cur, string &word, TrieNode *node){
        if (cur == word.size() && node->isEnd) return true;
        if (cur == word.size()) return false;
        char tmp = word[cur];
        if (tmp == '.'){
            for (auto next_node: node->Next){
                if(next_node){
                    auto r = dfs(cur + 1, word, next_node);
                    if(r) return true;
                }
            }
            return false;
        }
        else{
            if(! node->Next[tmp - 'a']) return false;
            return dfs(cur + 1, word, node->Next[tmp - 'a']);
        }
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
// @lc code=end

