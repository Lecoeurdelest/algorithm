import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        parts = re.findall(r'[A-Za-z0-9]+', s)
        result = "".join(parts).lower()       
        return result == result[::-1]
