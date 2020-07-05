class FileSharing {
    priority_queue<int, vector<int>, greater<int> > que;
    unordered_map<int, set<int> > id2chunk;
    unordered_map<int, set<int> > chunk2id;
    int max_size;
public:
    FileSharing(int m) {
        for(int i = 1; i < m + 1; ++i) que.push(i);
    }

    int join(vector<int> ownedChunks) {
        if(que.empty()) return -1;
        int ret = que.top();
        que.pop();
        for(auto chunk_id: ownedChunks){
            chunk2id[chunk_id].insert(ret);
            id2chunk[ret].insert(chunk_id);
        }
        return ret;
    }

    void leave(int userID) {
        que.push(userID);
        for(auto chunk_id: id2chunk[userID]){
            chunk2id[chunk_id].erase(userID);
        }
        id2chunk[userID].clear();
    }

    vector<int> request(int userID, int chunkID) {
        vector<int> ret;
        for(auto uid: chunk2id[chunkID]){
            ret.push_back(uid);
        }
        if(!ret.empty()){
            chunk2id[chunkID].insert(userID);
            id2chunk[userID].insert(chunkID);
        }
        return ret;
    }
};

/**
 * Your FileSharing object will be instantiated and called as such:
 * FileSharing* obj = new FileSharing(m);
 * int param_1 = obj->join(ownedChunks);
 * obj->leave(userID);
 * vector<int> param_3 = obj->request(userID,chunkID);
 */