int insect[500][500];

class Solution {
public:
    vector<string> computeSimilarities(vector<vector<int>>& docs) {
        unordered_map<int, vector<int>> word2doc;
        memset(insect, 0, sizeof(insect));
        for (int i = 0; i < docs.size(); ++i){
            for (int word: docs[i]){
                word2doc[word].push_back(i);
            }
        }
        for (auto &w2c: word2doc){
            for (int i = 0; i < w2c.second.size(); ++i)
                for(int j = i + 1; j < w2c.second.size(); ++j)
                    ++insect[w2c.second[i]][w2c.second[j]];
        }

        vector<string> ans;
        for (int i = 0; i < docs.size(); ++i)
            for(int j = 1; j < docs.size(); ++j){
                if(insect[i][j]){
                    double sim = double(insect[i][j]) / double(docs[i].size() + docs[j].size() - insect[i][j]);
                    char res[1024];
                    sprintf(res, "%d,%d: %0.4lf", i, j, sim + 1e-9);
                    ans.push_back(res);
                }
            }

        return ans;
    }
};