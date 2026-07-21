class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                x += 1
            elif x > 0:
                break

        return x