s = "loveleetcode"

def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        
        map = {}

        for char in s:
            map[char] = map.get(char, 0) + 1

        index = 0

        for i in s:
            if map[i] == 1:
                return index
            index+=1

        return -1

print(firstUniqChar(s))