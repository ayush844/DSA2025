class Solution:
    def isPalindrome(self, s: str) -> bool:
        text_arr = [char.lower() for char in s if char.isalnum()]
        left = 0
        right = len(text_arr)-1
        while left < right:
            if text_arr[left] != text_arr[right]:
                return False
            left+=1
            right-=1

        return True