class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HASHMAP1 = {}
        HASHMAP2 = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            HASHMAP1[s[i]] =  1 +HASHMAP1.get(s[i],0)
            HASHMAP2[t[i]] =  1 +HASHMAP2.get(t[i],0)

        if HASHMAP1 == HASHMAP2:
            return True
        else:
            return False

      
        