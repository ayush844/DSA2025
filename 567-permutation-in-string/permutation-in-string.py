class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_1 = {}
        count_2 = {}

        m = len(s1)
        n = len(s2)

        if n < m:
            return False

        for i in range(m):
            ch = s1[i]
            count_1[ch] = count_1.get(ch, 0) + 1

        for i in range(m):
            ch = s2[i]
            count_2[ch] = count_2.get(ch, 0) + 1

        if count_1 == count_2:
            return True

        for i in range(m, n):
            ch = s2[i]
            count_2[ch] = count_2.get(ch, 0) + 1

            left_ch = s2[i-m]
            count_2[left_ch] -= 1

            if count_2[left_ch] == 0:
                del count_2[left_ch]

            if count_1 == count_2:
                return True

        return False