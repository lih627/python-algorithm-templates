class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost){
        int i = 0, n = gas.size(), pgas = 0, pcost = 0;
        while(i < n){
            int start = i;
            int cgas = 0, ccost = 0;
            while(i < n){
                cgas += gas[i];
                ccost += cost[i];
                if (cgas >= ccost){
                    ++i;
                }
                else break;
            }
            pgas += cgas;
            pcost += ccost;
            if (i == n && pgas >= pcost){
                return start;
            }
            ++i;
        }
        return -1;
    }
};¬