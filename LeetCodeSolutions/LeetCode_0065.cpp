class Solution {
public:
    bool isNumber(string s) {
        //  START 0, SIGN 1, INT 2, DOT 3, FLOAT 4, EXP 5, SIGNEXP 6, SCIENCE 7,  BLANK 8
        //
        vector<bool> finals{0, 0, 1, 0, 1, 0, 0, 1, 1};
            //B  +-  09   .  eE  others
        vector<vector<int> > transform{
            { 0,  1,  2,  3, -1, -1},
            {-1, -1,  2,  3, -1, -1},
            { 8, -1,  2,  4,  5, -1},
            {-1, -1,  4, -1, -1, -1},
            { 8, -1,  4, -1,  5, -1},
            {-1,  6,  7, -1, -1, -1},
            {-1, -1,  7, -1, -1, -1},
            { 8, -1,  7, -1, -1, -1},
            { 8, -1, -1, -1, -1, -1}
        };
        int state = 0;
        for(auto c: s){
            int _next = nxt(c);
            state = transform[state][_next];
            if (state == -1) return false;
        }
        return finals[state];

    }

    int nxt(char &c){
        if(c == ' ') return 0;
        if(c == '+' || c == '-') return 1;
        if(c >= '0' && c <= '9') return 2;
        if(c == '.') return 3;
        if(c == 'e' || c == 'E') return 4;
        return 5;
    }
};