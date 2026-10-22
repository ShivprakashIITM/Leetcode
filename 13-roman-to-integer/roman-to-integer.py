class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dis = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1):
            if dis[s[i]] < dis[s[i+1]]:
                result -= dis[s[i]]
            else:
                result += dis[s[i]]  
        return result + dis[s[-1]]           
        
        
        