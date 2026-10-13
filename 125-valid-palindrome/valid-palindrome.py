class Solution:
    def isPalindrome(self, s: str) -> bool:
        text_arr = [char.lower() for char in s if char.isalnum()]
        low = 0
        high = len(text_arr) - 1

        while (low <= high):
            if text_arr[low] != text_arr[high]:
                return False
            low+=1
            high-=1

        return True