/*
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

*/

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int chars_read=0,r;
        while(chars_read<n){
            r=read4(buf+chars_read); //ensure there's no overflow! 
            if(r==0){
                //the file has no more chars! 
                break;
            }
            chars_read+=r;
        }
        return min(chars_read,n);
    }
};
