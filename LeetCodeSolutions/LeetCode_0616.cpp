class Solution {
public:
    string addBoldTag(string s, vector<string>& dict) {
        unordered_set<string> words;
        set<int, greater<int> > length;
        for(auto str: dict){
            length.insert(str.size());
            words.insert(str);
        }
        vector<pair<int, int> > intervals;
        for(int i = 0; i < s.size(); ++i){
            for(auto &len: length){
                if (i + len <= s.size())
                if(words.count(s.substr(i, len))){
                    intervals.push_back(make_pair(i, i + len));
                    break;
                }
            }
        }

        vector<int> st, en;
        if(intervals.size() == 0) return s;
        int _st = intervals[0].first;
        int _en = intervals[0].second;
        for(int i = 1; i < intervals.size(); ++i){
            auto &p = intervals[i];
            cout << _st << ' ' << _en << endl;
            if(p.first <= _en){
                _en = max(_en, p.second);
            }
            else{
                st.push_back(_st);
                en.push_back(_en);
                _st = p.first;
                _en = p.second;
            }
        }
        st.push_back(_st);
        en.push_back(_en);
        string ret;
        int pos = 0;
        for(int i =0; i < s.size(); ++i){
            int &_s = st[pos];
            int &_e = en[pos];
            if(i == _s){
                ret += "<b>";

            }
            if(i == _e){
                ret += "</b>";
                if(pos < st.size() -1) ++pos;
            }
            ret += s[i];
        }
        cout << s.size() << endl;
        if (en.back() == s.size()) ret += "</b>";
        return ret;

    }
};