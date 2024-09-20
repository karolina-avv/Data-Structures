class Solution:
    def same(self, i1, i2):
        # Please write your code here
        if not i1 and not i2:
            return True
        if len(i1) != len(i2) or i1[0] != i2[0]:
            return False
        
        left1 = [i for i in i1 if i < i1[0]]
        right1 = [j for j in i1 if j > i1[0]]
        left2 = [i for i in i2 if i < i2[0]]
        right2 = [j for j in i2 if j > i2[0]]
        
        return self.same(left1, left2) and self.same(right1, right2)


def main():
    i1 = [15, 25, 20, 22, 30, 18, 10, 8, 9, 12, 6]
    i2 = [15, 10, 12, 8, 25, 30, 6, 20, 18, 9, 22]

    res = Solution().same(i1, i2)
    print(res)  # Should print true


if __name__ == '__main__':
    main()
