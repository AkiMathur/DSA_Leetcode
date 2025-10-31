class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_l = dict()
        ran_l = dict()

        for letters in magazine:
            if letters not in mag_l:
                mag_l[letters] = magazine.count(letters)
        for letters in ransomNote:
            if letters not in ran_l:
                ran_l[letters] = ransomNote.count(letters)
        for i in ran_l.keys():
            if i in mag_l and ran_l[i]<=mag_l[i]:
                continue
            else:
                return False
        return True