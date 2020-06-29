class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.size() - 1, j = b.size() - 1;
        string ret;
        int carry = 0;
        while(i >= 0 || j >= 0 || carry > 0){
            char a_ = i >= 0 ? a[i]: '0';
            char b_ = j >= 0 ? b[j]: '0';
            if(i >= 0)--i;
            if(j >= 0)--j;
            if (a_ != b_){
                if(carry) {
                    ret += '0';
                    carry = 1;
                }
                else{ret += '1'; carry = 0;}
            }
            else{
                if(a_ == '0'){
                    ret += carry? '1' : '0';
                    carry = 0;
                }
                else{
                    ret += carry? '1': '0';
                    carry = 1;
                }
            }
        }
        return {ret.rbegin(), ret.rend()};

    }
};