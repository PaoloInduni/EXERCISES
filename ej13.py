s = "()[]{}"

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        
        map = {")":"(","]":"[","}":"{"}
        stack = []

        for parentesis in s:
            if parentesis in map.values():
                stack.append(parentesis)
            elif parentesis in map.keys():
                if not stack or map[parentesis] != stack.pop():
                    return False

        return not stack
        
print(isValid(s))
