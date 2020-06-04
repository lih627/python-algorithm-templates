unordered_map<int, string> to9{{1, "One"}, {2, "Two"}, {3, "Three"},
{4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};

unordered_map<int, string> to19{{10, "Ten"}, {11, "Eleven"}, {12, "Twelve"},
{13, "Thirteen"}, {14, "Fourteen"}, {15, "Fifteen"}, {16, "Sixteen"},
{17, "Seventeen"}, {18, "Eighteen"}, {19, "Nineteen"}};

unordered_map<int, string> to90{{2, "Twenty"}, {3, "Thirty"}, {4, "Forty"},
{5, "Fifty"}, {6, "Sixty"}, {7, "Seventy"}, {8, "Eighty"}, {9, "Ninety"}};

const int BILLIION = 1000000000;
const int MILLION = 1000000;
const int THOUSAND = 1000;

class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        string res;
        int billion = num / BILLIION;
        string str_bil = tostr(billion);
        bool before = false;
        if (str_bil != ""){
            if (!before) before = true;
            res += str_bil;
            res += " ";
            res += "Billion";
        }
        // cout << res<< " 1"<< endl;

        int million = num % BILLIION / MILLION;
        string str_mil = tostr(million);
        if (str_mil != ""){
            if (before) res += " ";
            if (!before) before = true;
            res += str_mil;
            res += " ";
            res += "Million";
        }
        // cout << res<< " 2" <<endl;

        int thousand = num % MILLION / THOUSAND;
        string str_tho = tostr(thousand);
        // cout << str_tho << endl;
        if (str_tho != ""){
            if (before) res += " ";
            if (!before) before = true;
            res += str_tho;
            res += " ";
            res += "Thousand";
        }

        int lst = num % THOUSAND;
        string str_lst = tostr(lst);
        if (str_lst!= ""){
            if (before) res += " ";
            if (!before) before = true;
            res += str_lst;
        }

        return res;

    }


    string tostr(int n){
        if (n == 0) return "";
        string res;
        int d3, d2, d1;
        d3 = n / 100;
        if (d3 > 0){
            res += to9[d3];
            res += " Hundred";
        }
        d2 = n % 100;
        if (d2 >= 10 && d2 < 20){
            if(res.length()) res += " ";
            res += to19[d2];
        }
        else if(d2 < 10 && d2 > 0){
            if(res.length()) res += " ";
            res += to9[d2];
        }
        else if(d2 >19){
            if(res.length()) res += " ";
            res += to90[d2/10];
            d3 = d2 % 10;
            if (d3 > 0){
                res += " ";
                res += to9[d3];
            }
        }
        return res;
    }

};