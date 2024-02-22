class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        int answer=-1;
        if (n==1 && trust.size()==0){
            return 1;
        };
        vector<int> tracker(n+1,0);
        for (const auto& pair: trust){
            tracker[pair[0]]-=1;
            tracker[pair[1]]+=1;
        };
        for (int idx=1; idx<=n; ++idx){
            if (tracker[idx]==n-1){
                answer=idx;
                break;
            }
        };
        return answer;
    }
};