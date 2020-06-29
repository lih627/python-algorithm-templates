class Solution {
public:
    vector<int> assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
    int n = workers.size();
    int m = bikes.size();

    if (m < 1 || n < 1) return {};
    vector<vector<pair<int, int>>> bucket(2001);


    for ( int i = 0; i < m; ++i) {
        for ( int j = 0; j < n; ++j) {
            int d = getD( workers[j][0], bikes[i][0],   workers[j][1] , bikes[i][1] );
            bucket[d].push_back( {i, j } );
        }
    }

    vector<int> res(n , -1);
    vector<int> bikeused(m , false);

    for (int i = 0; i < bucket.size(); ++i) {
        if (bucket[i].empty()) continue;
        for ( auto& p : bucket[i] ) {
            if ( bikeused[p.first] == false && res[p.second] == -1 ) {
                res[p.second] = p.first;
                bikeused[p.first] = true;
            }

        }

    }
    return res;
  }

  int getD(  int x1, int x2, int y1, int y2 ) {
    return abs(  x1 - x2 ) + abs( y1 - y2);
  }
};