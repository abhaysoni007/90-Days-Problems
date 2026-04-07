class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        st=[]
        for c in s:
            if c in '({[':
                st.append(c)
            elif len(st)==0:
                return False
            elif (c==')' and st[-1] =='(') or (c=='}' and st [-1]=='{' )or  (c =="]" and st[-1]=='['):
                st.pop()
            else:
                return False
        if not st:
            return True
        else:
            return False