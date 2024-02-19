class Solution {
public:
    bool isPowerOfTwo(int n) {
        int d=n/2;
        int r=n%2;
        while (d>0 && r==0){
            r=d%2;
            d=d/2;
        }
        if (d==0 && r==1){
            return true;
        }
        return false;
    }
};