class Solution:
    def maxProduct(self, n: int) -> int:
        z = str(n)
        arr = []

        for i in z:
            arr.append(int(i))

        left = 0
        right = 1
        maxi = arr[0] * arr[1]

        while left < len(arr) - 1:

            if arr[left] * arr[right] > maxi:
                maxi = arr[left] * arr[right]

            right += 1
            if right == len(arr):
                left += 1
                right = left + 1

        return maxi