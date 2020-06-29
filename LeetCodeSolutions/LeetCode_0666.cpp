class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        int m = A.size(), n = B.size();
        if(m >= n){
            if (A.find(B) != A.npos) return 1;
            A +=A;
            if(A.find(B) != A.npos) return 2;
        }
        else{
            int i = (n - n % m) / m;
            if (n % m)  ++i;
            string tmp;
            int a = i;
            while(a--) tmp +=A;

            for (int k = i; k < i + 2; ++k){
                cout << tmp << endl;
                if(tmp.find(B) != tmp.npos) return k;
                tmp += A;
            }
        }
        return -1;

    }
};