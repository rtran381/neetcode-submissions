class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "{" or bracket == "(" or bracket == "[":
                stack.append(bracket)
            else:
                print(stack)
                brackets = ""
                if stack:
                    brackets = stack.pop()
                brackets += bracket
                print(brackets)
                if brackets == "[]" or brackets == "()" or brackets == "{}":
                    continue;
                return False
        if stack:
            return False
        return True