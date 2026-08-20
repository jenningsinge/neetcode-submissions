class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                parens.append(c)
            elif len(parens) > 0:
                if self.matchingParens(c, parens[-1]):
                    parens.pop()
                else:
                    return False
            else:
                return False
        return len(parens) == 0

    def matchingParens(self, close: str, open: str) -> bool:
        if close == ")" and open == "(":
            return True
        if close == "}" and open == "{":
            return True
        if close == "]" and open == "[":
            return True
        return False
        