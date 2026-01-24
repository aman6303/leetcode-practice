class Solution:
    def reverseWords(self, s: str) -> str:
        # removing end spaces

        # s = s.strip()

        mylist = s.split()

        rev_list = mylist[::-1]
        return " ".join(rev_list)


# Note

# if we split on space and a string contain two or more consecutive spaces then it get splitted through space and none of the adjacent word will contain these extra spaces

# .split() normalizes whitespace for semantic tokenization, collapsing gaps and trimming boundaries to streamline downstream processing. In contrast, .split(" ") preserves whitespace fidelity for protocol-level scenarios where formatting is part of the data contract.
