import unittest


s = 'abcd'
fp = 0


def read4(buf: list[str]) -> int:

    global s
    global fp
    ans = 0
    for i in range(fp, fp + 4):
        if i < len(s):
            ans += 1
            buf[i-fp] = s[i]
    fp += 4
    return ans


class Solution:
    def read(self, buf: list[str], n: int):
        """
        :type buf: Destination buffer (list[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """

        buf4 = ['', '', '', '']

        file = ''
        last_read = 4
        while last_read>0 and len(file) < n:
            last_read = read4(buf4)
            file = file + ''.join(buf4[:last_read])
        
        file = file[:n]
        
        buf.clear()
        for c in file:
            buf.append(c)
        
        return len(file)


def test(testObj: unittest.TestCase, file: str,  n: int) -> None:
    global s
    global fp

    s = file
    fp = 0
    so = Solution()
    buf: list[str] = []
    so.read(buf,  n)
    actual = ''.join(buf)
    testObj.assertEqual(actual, file[:n])


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self, "abc", 4)

    def test_2(self):
        test(self, "abcde", 5)

    def test_3(self):
        test(self, "abcdABCD1234", 12)

    def test_4(self):
        test(self, "abcde", 3)

    def test_5(self):
        test(self, "abcd", 5)

if __name__ == '__main__':
    unittest.main()


'''
Runtime
32 ms
Beats
65.39%
'''
