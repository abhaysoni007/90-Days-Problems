class Solution:
    def palindr(self,left,right,s):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True    
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            i=s[left]
            j=s[right]
            if i!=j:
                return self.palindr(left+1,right,s) or self.palindr(left,right-1,s)
            else:
                left+=1
                right-=1
        return True
        

