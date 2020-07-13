class Solution {
public:
    vector<int> divingBoard(int shorter, int longer, int k) {
	vector<int> ret;
    if (k == 0) return {};
	int delta = longer - shorter;
	int base = shorter * k;
	ret.push_back(base);
	if(delta == 0) return ret;
	for(int i = 1; i < k + 1; ++i){
	    base += delta;
	    ret.push_back(base);
	}
	return ret;
    }
};