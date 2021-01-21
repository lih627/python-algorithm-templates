class Solution {
public:
    string entityParser(string text) {
        unordered_map<string, string> mp = {
            {"&quot;", "\""}, {"&apos;", "'"}, {"&amp;", "&"},
            {"&gt;", ">"}, {"&lt;", "<"}, {"&frasl;", "/"}
        };
        string ret;
        int i = 0;
        while (i < text.size()){
            auto c = text[i];
            if (c != '&') ret += c;
            else{
                int start = i;
                bool valid = false;
                for (int len = 3; len < 8; ++len){
                    string tmp = text.substr(start, len);
                    if (mp.count(tmp)){
                        valid = true;
                        ret += mp[tmp];
                        i = start + len - 1;
                        break;
                    }
                }
                if (!valid) {
                    ret += c;
                }
            }
            ++i;
        }
        return ret;
    }
};