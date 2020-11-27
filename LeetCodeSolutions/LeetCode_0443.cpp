class Solution {
public:
    int compress(vector<char>& chars) {
        int insert_idx = 0, cur = 0;
        while(cur < chars.size()){
            int nxt = cur + 1;
            while(nxt < chars.size() && chars[nxt] == chars[cur]){
                ++nxt;
            }
            int length = nxt - cur;
            chars[insert_idx] = chars[cur];
            ++insert_idx;
            // cout << length << endl;
            if (length > 1)
                for(auto c: to_string(length)){
                    chars[insert_idx] = c;
                    ++insert_idx;
                }
            cur = nxt;
        }
        return insert_idx;
    }
};