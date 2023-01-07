class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for val in s:
            if (ord(val) > 64 and ord(val) < 91) or (ord(val) > 96 and ord(val) < 123) or (ord(val) > 47 and ord(val) < 58):
                palindrome += val.lower()
        return palindrome == palindrome[::-1] 
