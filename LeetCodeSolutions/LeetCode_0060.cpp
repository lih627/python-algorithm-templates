int fac(int x){
	int f;
	if(x==0 || x==1)
		f=1;
	else
		f=fac(x-1)*x;
	return f;
}


class Solution {
public:
    string getPermutation(int n, int k) {
        int num_used = 0;
        int ret = 0;
        vector<bool> used(n + 1, false);
        while(num_used < n){
            int interval = fac(n - num_used - 1);
            int start = 1;
            // cout << ret << ' ' << k << endl;
            for(int num = 1; num < n + 1; ++num){
                if(!used[num]){
                    int end = start * interval;
                    if(end >= k){
                        ret *= 10;
                        ret += num;
                        used[num] = true;
                        k -= interval * (start - 1);
                        ++num_used;
                        break;
                    }
                    ++start;
                }
            }
        }
        return to_string(ret);
    }
};