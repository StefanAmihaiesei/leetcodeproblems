class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq1 = {}
        freq2 = {}
        for litera in s:
            if litera not in freq1:
                freq1[litera] = 0
            freq1[litera]+=1
        for litera in t:
            if litera not in freq2:
                freq2[litera] = 0
            freq2[litera]+=1
        if freq1 != freq2:
            return False
        else:
            return True
        