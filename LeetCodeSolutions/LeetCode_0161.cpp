class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int m = s.size(), n = t.size();
        if (m == n + 1) return isD(t, s);
        if(n == m + 1) return isD(s, t);
        if(m == n) return isR(s, t);
        return false;
    }

    bool isD(string &shorter, string &longer){
        int cnt = 0;
        int i = 0, j = 0;
        while(i < shorter.size() && j < longer.size()){
            if(shorter[i] != longer[j]) {++cnt; ++j;}
            else{ ++i; ++j;}
        }
        return cnt == 0 || cnt == 1;
    }
    bool isR(string &shorter, string &longer){
        int i =0, j = 0;
        int cnt = 0;
        while(i < shorter.size() && j < longer.size()){
            if(shorter[i] != longer[j]) ++cnt;
            ++i; ++j;
        }
        return cnt == 1;
    }

};