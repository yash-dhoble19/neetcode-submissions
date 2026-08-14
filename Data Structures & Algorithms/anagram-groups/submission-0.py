class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h ={}

        for  word in strs:
            key = "".join(sorted(word))
            if key in h:
                h[key].append(word) 
            else:
                 h[key] = [word]

        h = list(h.values())

        return h
        

        