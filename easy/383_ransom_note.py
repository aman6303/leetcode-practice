class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) == 1:
            return magazine == ransomNote

        for char in ransomNote:
            if char in ransomNote:
                if ransomNote.count(char) <= magazine.count(char):
                    continue
                else:
                    return False
            else:
                return False

        return True
