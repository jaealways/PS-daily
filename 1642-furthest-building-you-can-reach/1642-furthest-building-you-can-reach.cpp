#include <queue>
#include <functional>

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue <int, vector<int>, greater<int>> heap;
        int n = heights.size();
        for (int i=0; i<n-1; ++i){
            int diff = heights[i+1]-heights[i];
            if (diff<0) continue;
            heap.push(diff);
            if (heap.size()>ladders){
                bricks-=heap.top();
                heap.pop();
            }
            if (bricks<0) return i;
        }
        return n-1;
    }
};