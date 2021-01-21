struct TrieNode{
    TrieNode *next[26];
    bool isEND = false;
};

class Trie{
    private:
        TrieNode *head;
    public:
        Trie(){
            head = new TrieNode();
        }

        void insert(string s){
            TrieNode *cur = head;
            for(auto c: s){
                if(cur->next[c - 'a'] == nullptr){
                    cur->next[c - 'a'] = new TrieNode();
                }
                cur = cur->next[c - 'a'];
            }
            cur->isEND = true;
        }

        string search(string s){
            string tmp{};
            TrieNode *cur = head;
            for(auto c: s){
                if(cur == nullptr) return s;
                if (cur->isEND) break;
                tmp += c;
                cur = cur->next[c - 'a'];
            }
            return tmp;
        }


};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        Trie trie{};
        for(auto c: dictionary) trie.insert(c);
        int i = 0;
        vector<string> s;
        string tmp{};
        while (i < sentence.size()){
            int j = i;
            for(; j < sentence.size() && sentence[j] != ' '; ++j) tmp += sentence[j];
            s.push_back(tmp);
            tmp = "";
            i = j + 1;
        }
        string ret;
        for(int i = 0; i < s.size(); ++i){
            ret += trie.search(s[i]);
            if (i != s.size() - 1) ret += " ";
        }
        return ret;
    }
};