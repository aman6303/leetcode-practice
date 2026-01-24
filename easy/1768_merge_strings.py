class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # method 1 - cause runtime error on leetcodde
        # len1 = len(word1)
        # len2 = len(word2)
        # mylist = []
        # if len1 > len2:
        #     rem = len1 - len2
        #     rem_chars = word1[rem:]

        # if len1 < len2:
        #     rem = len2 - len1
        #     rem_chars = word2[rem:]

        # for char1, char2 in zip(word1, word2):
        #     mylist.append(char1)
        #     mylist.append(char2)

        # return "".join(mylist) + rem_chars

        # method 2 - def mergeAlternately(self, word1: str, word2: str) -> str:
        out = []

        for a, b in zip(word1, word2):
            out.append(a)
            out.append(b)

        # append any remaining tail capacity
        return "".join(out) + word1[len(word2) :] + word2[len(word1) :]


print(Solution().mergeAlternately(word1="abcd", word2="pq"))
