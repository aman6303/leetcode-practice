class Solution:
    def reverseVowels(self, s: str) -> str:
        charlist = [char for char in s]

        vowels = []

        for char in charlist:
            if char.lower() in ["a", "e", "i", "o", "u"]:
                vowels.append(char)
        if len(vowels) == 0:
            return s
        breakpoint()
        # vowels = sorted(vowels, key=lambda x: x.lower())

        count = len(vowels) - 1
        for i, char in enumerate(charlist):
            if char.lower() in ["a", "e", "i", "o", "u"]:
                charlist[i] = vowels[count]
                count -= 1

        return "".join(charlist)


print(Solution().reverseVowels("leetcode"))
