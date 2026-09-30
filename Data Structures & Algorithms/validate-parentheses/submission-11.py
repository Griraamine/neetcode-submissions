class Solution:
    def isValid(self, s: str) -> bool:


        stack = []


        idk = { '(' : ')',
                '[' : ']',
                '{' : '}'}


        for letter in s:
            if letter in idk.keys() : stack.append(letter)
            elif not stack : return False    
            
            elif letter == idk[stack[len(stack)-1]]:
                stack.pop()
            else:
                return False
                



        return not stack