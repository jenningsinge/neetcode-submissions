class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        scores = []
        for op in operations:
            if op == "+":
                val = scores[-1] + scores[-2]
                score += val
                scores.append(val)
            elif op == "D":
                print(scores)
                val = scores[-1]*2
                score += val
                scores.append(val)
            elif op == "C":
                score -= scores[-1]
                scores.pop()
            else:
                val = int(op)
                score += val
                scores.append(val)
        return score


        