class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> charCount;
        unordered_map<char, int> firstIndex;
        int minIndex = numeric_limits<int>::max();
        
        for (int i = 0; i < s.length(); ++i) {
            charCount[s[i]]++;
            if (firstIndex.find(s[i]) == firstIndex.end()) {
                firstIndex[s[i]] = i;
            }
        }
        
        for (const auto& pair : firstIndex) {
            if (charCount[pair.first] == 1) {
                minIndex = min(minIndex, pair.second);
            }
        }
        
        if (minIndex == numeric_limits<int>::max()) {
            return -1;
        }
        
        return minIndex;
    }
};