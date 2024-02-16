#include <map>
#include <vector>

class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        map<int,int> counter;
        for (int num : arr){
            ++counter[num];
        }
        vector<int> counts;
        for (const auto& pair: counter){
            counts.push_back(pair.second);
        }
        sort(counts.begin(),counts.end());
        int r=counter.size();
        for (int i:counts){
            if (k >= i){
                k-=i;
                --r;
            } else {
                break;
            }
        }
        return r;
    }
};