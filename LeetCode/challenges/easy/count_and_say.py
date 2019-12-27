class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        answer = ''
        prev = self.countAndSay(n - 1)
        i = 0
        j = 1
        while i < len(prev):
            while j < len(prev) and prev[i] == prev[j]:
                j += 1
            group_frequency = j - i
            answer += str(group_frequency) + prev[i]
            i = j
        return answer


if __name__ == '__main__':
    print(Solution().countAndSay(6))