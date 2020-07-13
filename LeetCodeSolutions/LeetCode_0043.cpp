class Solution {
public:

    string add(string num1, string num2){
        string ret;
        int carry = 0;
        for(int i = num1.size() - 1, j = num2.size() - 1;
           i >= 0 || j >= 0; --i, --j){
            int n1 = i >= 0 ? num1[i] - '0': 0;
            int n2 = j >= 0 ? num2[j] - '0': 0;
            int tmp = n1 + n2 + carry;
            if(tmp > 9) {carry = 1; tmp %= 10;}
            else carry = 0;
            ret += '0' + tmp;
        }
        if (carry) ret += '1';
        return {ret.rbegin(), ret.rend()};
    }
    string multiply(string num1, string num2) {
        string ret = "0";
        if (num1.size() < num2.size()) swap(num1, num2);
        for(int i = num2.size() - 1; i >= 0; --i){
            string tmp = "0";
            string cur = num1;
            int add_num = num2[i] - '0';
            while (add_num > 0){
                if (add_num & 1) tmp = add(tmp, cur);
                cur = add(cur, cur);
                add_num >>= 1;
            }
            int j = i;
            while(j < num2.size() - 1){
                tmp += "0";
                ++j;
            }
            ret = add(ret, tmp);
        }
        return ret;
    }
};