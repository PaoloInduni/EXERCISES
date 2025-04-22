s = "abc" 
t = "ahbgdc"

def isSubsequence(s, t):

        i = j = 0
        sub = ""

        while i < len(t) and j < len(s):
            if(t[i]==s[j]):
                sub+=t[i]
                i+=1
                j+=1
                if(sub==s):
                    return True
            else:
                i+=1

        return sub==s

print(isSubsequence(s,t))