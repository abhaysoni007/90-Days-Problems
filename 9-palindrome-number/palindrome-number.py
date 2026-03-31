class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=list(str(x))
        b.reverse()
        a=list(str(x))
        if a==b:
            return True
        else:
            return False