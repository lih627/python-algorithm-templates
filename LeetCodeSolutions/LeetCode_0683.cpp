class Solution {
public:
    int kEmptySlots(vector<int>& bulbs, int K) {
        set<int> f;
        for(int i = 0; i < bulbs.size(); ++i){
            auto b = bulbs[i];
            auto it = f.insert(b).first;
            if(it != f.end()){
                auto nxt = next(it);
                if (*nxt - *it == K + 1) return i + 1;

            }
            if(it != f.begin()){
                auto pre = prev(it);
                if(*it - *pre == K + 1) return i + 1;
            }
        }
        return -1;
    }
};