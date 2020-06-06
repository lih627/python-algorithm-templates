const int INF = 1e9;
class Solution {
    vector<string> words;
    unordered_map<string, int> word2id;
    vector<vector<int> > edges;

public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        int id = 0;
        for (string & word: wordList){
            if (!word2id.count(word)){
                word2id[word] = id++;
                words.push_back(word);
            }
        }

        if (!word2id.count(endWord)) return {};
        if (!word2id.count(beginWord)){
            word2id[beginWord] = id++;
            words.push_back(beginWord);
        }
        edges.resize(words.size());

        for (int i = 0; i < words.size(); ++ i)
            for (int j = i + 1; j <words.size(); ++j){
                if (isEdge(words[i], words[j])){
                    edges[i].push_back(j);
                    edges[j].push_back(i);
                }
            }

        deque<vector<int> > que;
        vector<int> dist(words.size(), INF);
        vector<vector<string> > ret;

        que.push_back(vector<int>{word2id[beginWord]});
        dist[word2id[beginWord]] = 0;

        while (!que.empty()){
            vector<int>  path = que.front();
            que.pop_front();
            if (path.back() == word2id[endWord]){
                vector<string > p;
                for (auto &i: path){
                    p.push_back(words[i]);
                }
                ret.push_back(p);
                continue;
            }

            int cur_len = path.size();
            for (int &node: edges[path.back()]){
                if (dist[node] >= cur_len + 1){
                    vector<int> tmp(path);
                    tmp.push_back(node);
                    que.push_back(tmp);
                    dist[node] = cur_len + 1;
                }
            }
        }
        return ret;


    }


    bool isEdge(string &a, string &b){
        int diff = 0;
        for (int i =0; i < a.length(); ++i){
            if (a[i] != b[i]){
                ++diff;
                if (diff > 1) return false;
            }
        }
        return diff == 1;
    }
};