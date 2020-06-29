class Solution {
public:
string shortestPalindrome(string s)
{
    int n = s.size();
    cout << n << endl;
    string rev(s.rbegin(), s.rend());
    string new_s = s + "#" + rev;
    int new_n = new_s.size();
    vector<int> f(new_n, 0);
    cout << f.size() <<endl;
    f[0] = -1;
    int i = 0, j = -1;
    while(i < new_n - 1){
        if(j == -1 || new_s[i] == new_s[j]){
            ++i;
            ++j;
            f[i] = j;
        }
        else j = f[j];
    }
    return rev.substr(0, n - f[new_n - 1] - 1) + s;
}
};