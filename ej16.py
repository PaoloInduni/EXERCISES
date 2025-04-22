s = "badc"
t = "baba"

def isIsomorphic(s, t):
        
    if len(s) != len(t):
        return False

    dic = {}
    t_mapped = set()

    for index in range(len(s)):
        if s[index] in dic:
            if dic[s[index]] == t[index]:
                continue
            return False
        else:
            if t[index] in t_mapped:
                return False
            dic[s[index]] = t[index]
            t_mapped.add(t[index])
            
    return True
                 
print(isIsomorphic(s,t))