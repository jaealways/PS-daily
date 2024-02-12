#include <vector>

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int key=0, val=0;
        for (int i=0; i<nums.size(); i++){
            if (val==0){
                key=nums[i];
            }
            val+=(nums[i]==key) ?1 :-1;
        }
        return key;
    }
};