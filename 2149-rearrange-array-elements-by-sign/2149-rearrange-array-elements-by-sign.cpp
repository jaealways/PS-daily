class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> res(nums.size(),0);
        int pi=0, ni=1;
        for (int num : nums){
            if (num>0){
                res[pi]=num;
                pi+=2;
            }
            else{
                res[ni]=num;
                ni+=2;
            }
        }
        return res;
    }
};