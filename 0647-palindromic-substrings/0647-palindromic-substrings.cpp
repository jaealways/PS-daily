class Solution {
public:
    int countSubstrings(string s) {
        int n=s.length(),answer=0;
        
        auto palin=[&](int l, int r){
            while (l>=0 && r<n && s[l]==s[r]){
                answer++;
                l--;
                r++;
            }
        };
        
        for (int i=0; i<n; ++i){
            palin(i,i);
            palin(i,i+1);
        }
        
        return answer;
    }
    
};