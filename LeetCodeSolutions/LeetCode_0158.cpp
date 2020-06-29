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
    char local_buf[4] = {0};
    int l = 0;
    int r = 0;
    int read(char *buf, int n) {
        char *st = buf;
        int local_n = r - l;
        int cnt = 0;
        while(local_n < n){
            for(; l<r; ++l){
                st[cnt++] = local_buf[l];
                --n;
            }
            r = read4(local_buf);
            l = 0;
            local_n = r;
            if(local_n == 0) {break;}
        }
        int en = l + n;
        for(;l < en && l < r; ++l){
            st[cnt ++] = local_buf[l];
        }
        return cnt;


    }
};