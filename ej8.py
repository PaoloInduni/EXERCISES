s = "pwwkew"

def lengthOfLongestSubstring(s):
        
        if len(s) == 1:
              return 1

        longest = 0
        
        for i in range(len(s)):

            substring = []

            for j in range(i, len(s)):

                if substring.__contains__(s[j]) == False:
                    substring.append(s[j])
                    aux = substring
                    continue

                if(len(substring)>longest):
                    longest = len(substring)

                break
            
            if(len(aux)>longest):
                    longest = len(aux)

        return longest
            
print(lengthOfLongestSubstring(s))