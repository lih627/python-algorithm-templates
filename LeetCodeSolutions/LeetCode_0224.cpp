class Solution {
public:
    void compute(vector<string> &equation){
        if (equation.size() < 2) return;
        int cur = stoi(equation.back());
        equation.pop_back();
        string op = equation.back();
        equation.pop_back();
        while (op != ")"){
            int nxt = stoi(equation.back());
            equation.pop_back();

            if (op == "+") cur += nxt;
            else if (op == "-") cur -= nxt;
            if (equation.empty()) break;
            op = equation.back();
            equation.pop_back();
        }
        equation.push_back(to_string(cur));
    }
    int calculate(string s) {
        vector<string> equation;
        reverse(s.begin(), s.end());
        int cur = 0;
        while (cur < s.size()){
            if (s[cur] == ' ' ||s[cur] == '+'|| s[cur] == '-' ){
                if (s[cur] != ' ') equation.push_back({s[cur]});
                ++cur;
                continue;
            }
            string tmp{s[cur]};
            if (tmp == ")"){
                equation.push_back(tmp);
            }
            else if (tmp == "("){
                compute(equation);
            }
            else{
                while (cur + 1 < s.size() && s[cur + 1] >= '0' && s[cur + 1] <= '9'){
                    tmp += s[cur + 1];
                    ++cur;
                }
                reverse(tmp.begin(), tmp.end());
                equation.push_back(tmp);
            }
            ++cur;
        }
        compute(equation);
        if (!equation.empty()) return stoi(equation.back());
        return 0;
    }
    void pr(vector<string> &tmp){
        for (auto c: tmp) cout << c << ' ';
        cout << endl;
    }
};