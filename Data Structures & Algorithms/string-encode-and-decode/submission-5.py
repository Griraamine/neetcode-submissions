class Solution:

    def encode(self, strs: List[str]) -> str:
        ch = ""


        for word in strs:
            ch+= str(len(word)) + '#' + word
        return ch

    def decode(self, s: str) -> List[str]:
        result = []

        while '#' in s:
            pos = s.find('#')
            result.append(s[pos+1:pos + int(s[:pos]) + 1])
            s = s[pos +int(s[0:pos])+1:]
        return result
