/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf);
 */

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int cnt = 0;
        char *tmp = buf;
        bool c = true;
        while (cnt < n && c){
            int offset = read4(tmp);
            if (offset < 4) c = false;
            cnt += offset;
            tmp += offset;
        }
        if (c) buf[n] = '\0';
        return min(cnt, n);
    }
};