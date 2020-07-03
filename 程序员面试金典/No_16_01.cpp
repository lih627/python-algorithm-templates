class Solution {
public:
    vector<int> swapNumbers(vector<int>& numbers) {
        //  A = A ^ B
        //  B = A  ^ B
        //  A = A ^ B
        numbers[0] ^= numbers[1];
        numbers[1] ^= numbers[0];
        numbers[0] ^= numbers[1];
        return numbers;
    }
};