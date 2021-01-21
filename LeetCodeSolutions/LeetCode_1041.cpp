class Solution {
public:
    bool isRobotBounded(string instructions) {
        int dirs[4][2] = { {1, 0}, {0, -1}, {-1, 0}, {0, 1}};
        int x = 0, y = 0, d = 0;
        for(auto ins: instructions){
            if (ins == 'G'){
                x += dirs[d][0];
                y += dirs[d][1];
            }
            else{
                if (ins == 'L') d = (d + 3) % 4;
                else d = (d + 1) % 4;
            }
        }
        return (x == 0 && y == 0) || (d != 0);
    }
};