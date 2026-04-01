class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def back(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                subst = s[start:end+1]
                
                if isPalindrome(subst):
                    path.append(subst)
                    back(end + 1, path)
                    path.pop()
        back(0, [])
        return res