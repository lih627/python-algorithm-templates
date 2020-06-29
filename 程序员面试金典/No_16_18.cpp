class Solution {
public:
    bool patternMatching(string pattern, string value) {
        int n_a = 0, n_b = 0, n = value.size();
        for(char c: pattern){
            if (c == 'a') ++n_a;
            if (c == 'b') ++n_b;
        }
        // n_a * x + n_b * y = n;
        typedef pair<int, int> PII;
        vector<PII> combains;
        if (n_a == 0){
            if(n_b == 0) return n == 0;
            else if (n% n_b != 0) return false;
            else combains.push_back(make_pair(0, n / n_b));
        }
        else if(n_b == 0){
            if(n_a == 0) return n == 0;
            else if (n % n_a != 0) return false;
            else combains.push_back(make_pair(n / n_a, 0));
        }
        else{
            for(int _a =0; _a * n_a <= n; ++_a){
                int rest_n_b = n - _a * n_a;
                if(rest_n_b == 0){combains.push_back(make_pair(_a, 0));}
                else if(rest_n_b % n_b != 0) continue;
                else combains.push_back(make_pair(_a, rest_n_b / n_b));
            }
        }
        for(auto p: combains){
            if(isValied(p.first, p.second, pattern, value)) return true;
        }
        return false;
    }

    bool isValied(int &len_a, int &len_b, string &pattern, string &value){
        // cout << len_a << ' ' << len_b << ' '<< pattern << ' '<< value << endl;
        string str_a, str_b;
        if(len_a == 0){
            if(len_b == 0){
                // cout << value.size() << endl;
                if(value.size() != 0) return false;
                int i = 0, j = 0;
                for (char c: pattern){
                    if (c == 'a') ++i;
                    else ++j;
                    if(i && j) return false;
                }
                return true;
            }
            str_b = value.substr(0, len_b);
            // cout << str_b << endl;
            for(int i = 0; i < value.size() / len_b; ++i){
                string tmp = "";
                for(int j = len_b * i; j < len_b * (i + 1); ++j) tmp += value[j];
                if (tmp != str_b) return false;
            }
            return true;
        }
        else if(len_b == 0){
            str_a = value.substr(0, len_a);
            // cout << str_a << endl;
            for(int i = 1; i < value.size() / len_a; ++i){
                string tmp = "";
                for(int j = len_a * i; j < len_a *(i + 1); ++j) tmp += value[j];
                // cout << tmp << endl;
                // cout << str_a  << endl;
                if(tmp != str_a) return false;
            }
            return true;
        }
        else{
            int cnt_a = 0;
            int cnt_b = 0;
            int cnt = 0;
            while(cnt < pattern.size()){
                if(pattern[cnt] == 'a'){
                    if(cnt_a == 0) str_a = value.substr(cnt_a * len_a + cnt_b * len_b, len_a);
                    else{
                        if (str_a != value.substr(cnt_a * len_a + cnt_b * len_b, len_a)) return false;
                    }
                    ++cnt_a;
                    ++cnt;
                }
                else{
                    if(cnt_b == 0) str_b = value.substr(cnt_a * len_a + cnt_b * len_b, len_b);
                    else{
                        if(str_b != value.substr(cnt_a * len_a + cnt_b * len_b, len_b)) return false;
                    }
                    ++cnt_b;
                    ++cnt;
                }
            }
        return true;
        }
    }

};