class StringIterator {
    deque<pair<char, int>> q;
public:
    StringIterator(string compressedString) {
        int i = 0;
        while (i < compressedString.size()){
            char c = compressedString[i];
            int cnt = 0;
            while(i + 1 < compressedString.size() && compressedString[i + 1] >= '0' && compressedString[i + 1] <= '9'){
                cnt *= 10;
                cnt += compressedString[i + 1] - '0';
                ++i;
            }
            q.emplace_back(c, cnt);
            ++i;
        }
    }

    char next() {
        if (q.empty()) return ' ';
        char ret = q[0].first;
        q[0].second --;
        if(q[0].second == 0) q.pop_front();
        return ret;
    }

    bool hasNext() {
        return !q.empty();
    }
};

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator* obj = new StringIterator(compressedString);
 * char param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */