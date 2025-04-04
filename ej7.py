s = "A man, a plan, a canal: Panama"

def isPalindrome(s):

        clean_s = ''.join(char for char in s if char.isalnum())
        clean_s = clean_s.lower()

        for i in range(len(clean_s)//2 + 1):

            if clean_s[i] != clean_s[len(clean_s)-(i+1)]:
                return False
        return True

print(isPalindrome(s))