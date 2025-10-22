class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_1 = {}
        for character in s:
            map_1[character] = map_1.get(character, 0) + 1
        map_2 = {}
        for character in t:
            map_2[character] = map_2.get(character, 0) + 1
        if(len(map_1) != len(map_2)): 
            return False
        else:
            for key in map_1:
                if map_2.get(key) != map_1[key]:
                    return False
        return True