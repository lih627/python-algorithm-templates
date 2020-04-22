#define PII pair<int, int>
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<PII> heap = {};
        for (int num: arr){
            heap.push_back(make_pair(abs(num - x), num));
            push_heap(heap.begin(), heap.end());
            if (heap.size() == k + 1){
                pop_heap(heap.begin(), heap.end());
                heap.pop_back();
            }
        }
        vector<int> res = {};
        for(PII p: heap){
            res.push_back(p.second);
        }
        sort(res.begin(), res.end());
        return res;
    }
};