#include <unordered_map>
#include <vector>
#include <string>


class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freqMap;
        for (char c : s) {
            freqMap[c]++;
        }

        vector<pair<char, int>> freqVec(freqMap.begin(), freqMap.end());

        sort(freqVec.begin(), freqVec.end(), [](const pair<char, int>& a, const pair<char, int>& b) {
            return a.second > b.second || (a.second == b.second && a.first < b.first);
        });

        string result;
        for (const auto& e : freqVec) {
            result += std::string(e.second, e.first);
        }

        return result;
    }
};