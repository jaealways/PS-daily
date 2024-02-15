class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        long long n=nums.size(), answer=-1, nSum=0;
        for (int i=0; i<n; ++i){
            if (nums[i]<nSum){
                answer=nSum+nums[i];
            }
            nSum=nSum+nums[i];
        }
        return answer;
    }
};