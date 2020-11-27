class Solution {
public:
    vector<string> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_map<string, vector<string>> mp;
        bool findendWord = false;
        for(auto word: wordList){
            if (word == endWord) findendWord = true;
            for(int i = 0; i< word.size(); ++i){
                string tmp = word;
                tmp[i] = '*';
                mp[tmp].push_back(word);
            }
        }
        if (!findendWord) return {};
        unordered_set<string>  visited;
        deque<vector<string>> queue;
        queue.push_back({beginWord});
        visited.insert(beginWord);
        while (!queue.empty()){
            auto path = queue.front();
            queue.pop_front();
            string last = path.back();
            for (int i = 0; i < last.size(); ++i){
                string tmp = last;
                tmp[i] = '*';
                for (auto nxt: mp[tmp]){
                    if(visited.count(nxt)) continue;
                    vector<string> cp = path;
                    cp.push_back(nxt);
                    visited.insert(nxt);
                    if (nxt == endWord) return cp;
                    queue.push_back(cp);
                }
            }
        }
        return {};
    }
};