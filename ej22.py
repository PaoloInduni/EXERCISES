def countCompleteDayPairs(hours):
        dic = {}
        count = 0
        for i in hours:
            rem = i % 24
            complement = (24 - rem) % 24
            if complement in dic:
                count += dic[complement]
            dic[rem] = dic.get(rem, 0) + 1
        return count