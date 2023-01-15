class Solution:
    def reverseWords(self, s: str) -> str:
        val = s.split(" ")
        string = ""
        for i in range(0 , len(val)):
            string += val[i][::-1] + " "

        return string.strip()
