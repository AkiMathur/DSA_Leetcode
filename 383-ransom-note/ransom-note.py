class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cons = dict()

        for letters in magazine:
            cons[letters] = magazine.count(letters)
        for letters in ransomNote:
            if letters in cons and ransomNote.count(letters) <= cons[letters]:
                continue
            else:
                return False
        return True