class Solution:
    def length(self,s):
        words=s.strip().split()
        return (len(words[-1]))
words="   fly me   to   the moon  "
solution=Solution()
result=solution.length(words)
print(result)