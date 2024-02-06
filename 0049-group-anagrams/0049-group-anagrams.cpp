class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> dictStr;
        
        for (const auto& s: strs){
            string tmpS=s;
            sort(tmpS.begin(), tmpS.end());
            dictStr[tmpS].push_back(s);
        }
        
        vector<vector<string>> result;
        for (const auto& pair: dictStr){
            result.push_back(pair.second);
        }
        
        return result;
    }
};