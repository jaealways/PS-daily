"""
t에 있는 것 모두 포함해서 minimum substing return

s에 대한 dict, t에 대한 dict 만들어서
왼쪽 올 때마다 하나씩 제거, if 없으면 거기서 stop 후 오른쪽부터 제거
오른쪽 오다가 없으면 stop 후 return

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        for char in t:
            dict_t[char]=dict_t.get(char,0)+1
        
        required = len(dict_t)
        formed=0
        
        l,r=0,0
        window_counts={}
        
        ans = float("inf"), None, None
        
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

                