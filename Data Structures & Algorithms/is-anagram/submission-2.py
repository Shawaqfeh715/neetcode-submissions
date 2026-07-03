class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        word_hash={}

        for i in range(len(s)):
            word_hash[s[i]]=word_hash.get(s[i],0)+1
            word_hash[t[i]]=word_hash.get(t[i],0)-1

        return all(v==0 for v in word_hash.values())

        






        