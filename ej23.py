def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1: return s
        
        window = len(s)
        
        while window >= 0:
            for i in range(len(s)-window+1):
                if isPalindrome(s[i:i+window]):
                    return s[i:i+window]
            window-=1

        return ""
        
def isPalindrome(s):
        return s == s[::-1]
    
print(longestPalindrome("babad"))